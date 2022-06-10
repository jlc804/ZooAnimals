""" json example showing how to dumps() custom and non-python
supported classes """
import json


# client (as a function) -----------------------------------------
def main():
    items = [
        RetailProduct("Borax Powder, 4 LBS", 3.99),
        Card(),
        3.5, [1, "two"], {"first": 1, "second": 2.2}, 3.3 - 4.4j,
        RetailProduct(),
        RetailProduct(22, 22),
        RetailProduct("bad", "Bad")
    ]

    print("\ndumps()ing each item individually:")
    for item in items:
        print("Python item:", item)
        json_item = json.dumps(item, cls=MultiTypeEncorder)
        print("JSON item:", json_item)
        print()
    print()

    print("The entire list:\n", items)
    json_all = json.dumps(items, cls=MultiTypeEncorder)
    print("\ndumps()ing the entire list:\n", json_all)
    print(json_all)


# BEGIN GLOBAL SCOPE FUNCTIONS -------------------------------------
# (none in this example)
# END GLOBAL SCOPE FUNCTIONS ----------------------------------------
# BEGIN CLASS RetailProduct   ---------------------------------------
import locale

locale.setlocale(locale.LC_ALL, '')


class RetailProduct:
    # class constants -------------------------------------
    DEFAULT_NAME = "-unnamed item-"
    MIN_NAME_LEN = 1
    MAX_NAME_LEN = 100
    DEFAULT_PRICE = 0.0
    MIN_PRICE = 0.0
    MAX_PRICE = 1.0e9

    # constructor -----------------------------------------
    def __init__(self, name=DEFAULT_NAME, price=DEFAULT_PRICE):
        # instance attributes (see mutator for details)
        if not self.set_name(name):
            self.name = self.DEFAULT_NAME

        if not self.set_price(price):
            self.price = self.DEFAULT_PRICE

    # mutator method(s) -----------------------------------
    def set_price(self, price):
        if not self.valid_price(price):
            return False
        # else
        self.price = price
        return True

    def set_name(self, name):
        if not self.valid_name(name):
            return False
        # else
        self.name = name
        return True

    # accessor method(s) ---------------------------------
    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    # stringizer -----------------------------------------
    def __str__(self):
        price = locale.currency(self.price, grouping=True)
        name = "\'" + self.name + "\'"

        ret_str = "[{}({})]".format(name, price)
        return ret_str

    # helper for vetting prices and names  ----------------
    @classmethod
    def valid_name(cls, test_str):
        # check that it's a string
        if not isinstance(test_str, str):
            return False

        # check length
        if not (cls.MIN_NAME_LEN <= len(test_str) <= cls.MAX_NAME_LEN):
            return False

        return True

    @classmethod
    def valid_price(cls, test_price):
        # check that it's a reasonable number
        if not (isinstance(test_price, int)
                or isinstance(test_price, float)):
            return False

        # check range
        if not (cls.MIN_PRICE <= test_price <= cls.MAX_PRICE):
            return False

        return True


# END CLASS RetailProduct   ---------------------------------------------
# BEGIN CLASS Card   ---------------------------------------
class Card:
    # constructor -----------------------
    def __init__(self, value="A", suit="spades"):
        # for this demo, we won't bother filtering w/mutators
        self.value = value
        self.suit = suit

    # instance helpers ------------------
    def to_string(self):
        ret_str = "Card = {} of {}".format(self.value, self.suit)
        return ret_str

    # stringizer -----------------------------------------
    def __str__(self):
        ret_str = "Card = {} of {}".format(self.value, self.suit)
        return ret_str


# END CLASS Card   ---------------------------------------------
# BEGIN CLASS RetailJsnEncoder   ---------------------------------------
class RetailJsnEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, RetailProduct):
            return {'__RetailProduct__': obj.__dict__}
        return {type(obj): obj.__dict__}


# END CLASS RetailJsnEncoder   -----------------------------------------
# BEGIN CLASS RetAndComlexEncoder   -----------------------------------
class RetAndComlexEncoder(RetailJsnEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {'__complex__': {"real": obj.real, "imag": obj.imag}}
        return super().default(obj)
    # END CLASS RetAndComlexEncoder   -----------------------------------


# BEGIN CLASS MultiTypeEncorder   -----------------------------------
class MultiTypeEncorder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, RetailProduct):
            return {'__RetailProduct__': obj.__dict__}
        if isinstance(obj, Card):
            return {'__Card__': obj.__dict__}
        if isinstance(obj, complex):
            return {'__complex__': {"real": obj.real, "imag": obj.imag}}
        return {type(obj): obj.__dict__}


# END CLASS MultiTypeEncorder   ---------------------------------------------

# -------------- main program -------------------
if __name__ == "__main__":
    main()