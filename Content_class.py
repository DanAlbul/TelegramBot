
class Content:
    def __init__(self, store_name, prod_url, prod_title, prod_code, prod_price, prod_status):  #prod_id/title etc. work like titleTag bodyTag (selectors)
        self.store_name = store_name
        self.prod_url = prod_url
        self.prod_title = prod_title
        self.prod_code = prod_code
        #self.prod_version = prod_version
        self.prod_price = prod_price
        self.prod_status = prod_status


    def get_store_name(self):
        store = "{}".format(self.store_name)
        return store

    def get_prod_title(self):
        title = "{}".format(self.prod_title)
        return title

    def get_prod_code(self):
        code = "{}".format(self.prod_code)
        return code

    def get_prod_price(self):
        price = "{}".format(self.prod_price)
        return price

    def get_prod_status(self):
        status = "{}".format(self.prod_status)
        return status


    def print_prod_info(self):
        print("\n")
        print("Страница: {}".format(self.prod_url))
        print("Продукт: {}".format(self.prod_title))
        print("Код продукта: {}".format(self.prod_code))
        #print("Версия: {}".format(self.prod_version))
        print("Цена: {}".format(self.prod_price))
        print("Наличие: {}".format(self.prod_status))
        print("\n")
