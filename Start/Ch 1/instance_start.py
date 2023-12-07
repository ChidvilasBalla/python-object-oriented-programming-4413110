# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"
        # TODO: add properties

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def set_discount(self, amount):
        self._discount = amount # "_" prefix is making a variable private


# TODO: create some book instances
b1 = Book("War and Peace","jaffa",145,12.3)
b2 = Book("The Catcher in the Rye","Kulfi",123,23.21)

# TODO: print the price of book1
# print(b1.get_price())

# # TODO: try setting the discount

# print("Price before discount:" , b2.get_price())
# b2.set_discount(0.25)
# print(b2.get_price())

# TODO: properties with double underscores are hidden by the interpreter

print(b2._Book__secret) #another way to hide attributes, by prefixing class anme