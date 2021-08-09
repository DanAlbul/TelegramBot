from Data import *
from Website_class import Website
from Parser_class import Parser
import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space

TOKEN = "1401420511:AAHVAepv5rx0_jbD_k2Mn2ay6lLrBAhSlKA"
chat_id = "-444558045"

currentData = []  # actual info of the product in all shops
contentData = []  # updated info of the product in all shops

def get_help():
    msg = '''
    Use one of the following commands:
    
    help: To show this help
    screen: Provide Bot with necessary data for comparison
    monitor: Start monitoring shops comparing data form screen (push notification will be sent in case of any updates)
    '''
    return msg


def screen_data():
    """
    Function for identifying actual information about the product.
    Selectors are kept in selectorsData[]. Using structure of Website class
    - all data is parsed from # websites in Parser class. Then found data is saved in currentData[]
    for the future comparing with contentData[] (used in case if the data in shops would change)
    """
    parser = Parser()
    websites = []
    for row in selectorsData:
        websites.append(Website(row[0], row[1], row[2], row[3], row[4]))

    for i in range(len(selectorsData)):
        currentData.append(parser.parse(websites[i], linksData[i]))

    for innerlist in currentData:
        for item in innerlist:
            return '\n'.join(str(item) for innerlist in currentData for item in innerlist)

    parser.driver.close()


def monitor_shops():
    counter = 0
    while counter != 30:
        contentData.clear()
        parser = Parser()
        websites = []
        for row in selectorsData:
            websites.append(Website(row[0], row[1], row[2], row[3], row[4]))

        for i in range(len(selectorsData)):
            contentData.append(parser.parse(websites[i], linksData[i]))

        parser.driver.close()

        if contentData != currentData:
            for innerlist in contentData:
                for item in innerlist:
                    return '\n'.join(str(item) for innerlist in contentData for item in innerlist)

        time.sleep(600)
        counter += 1

    if counter == 30:
        currentData.clear()
    return "Iteration is done. Write 'monitor' again to continue."

COMMANDS = {
    'help': get_help,
    'screen': screen_data,
    'monitor': monitor_shops
}


class Telbot(telepot.helper.ChatHandler):

    def open(self, initial_msg, seed):
        self.sender.sendMessage(get_help())
        # prevent on_message() from being called on the initial message
        return True

    def on_chat_message(self, msg):
        # If the data sent is not test, return an error
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type != 'text':
            self.sender.sendMessage("I don't understand you. "
                                    "Please type 'help' for options")
            return

        # Make the commands case insensitive
        command = msg['text'].lower()
        if command not in COMMANDS:
            self.sender.sendMessage("I don't understand you. "
                                    "Please type 'help' for options")
            return

        message = COMMANDS[command]()
        self.sender.sendMessage(message)

    def on_idle(self, event):
        self.close()

    def on_close(self, event):
        # Add any required cleanup here
        pass

# Create and start the bot
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, Telbot, timeout=10),
])
MessageLoop(bot).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
