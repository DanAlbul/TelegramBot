
class Website:
    """
    Contains information about website structure
    """
    def __init__(self, store_name, selector_title, selector_code, selector_price, selector_status):  # prod_id/title etc. work like titleTag bodyTag (selectors)
        self.store_name = store_name
        self.selector_title = selector_title
        self.selector_code = selector_code
        self.selector_price = selector_price
        self.selector_status = selector_status
