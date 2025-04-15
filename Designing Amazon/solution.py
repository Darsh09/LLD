from abc import ABC, abstractmethod
    
class User(ABC):
    @abstractmethod
    def register():
        pass

    def login(self):
        if self.email == "EMAIL_FROM_DB" and self.password == "PASSWORD_FROM_DB":
            return True
        return False


class Buyer(User):
    def __init__(self, name, email, password, phone, shipping_address):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.shipping_address = shipping_address
    
    def register(self, email, password):
        print("add to db user ({email}, {password})")


class Seller(User):
    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    def register(self, email, password):
        # might need some additional verification
        print("add to db user ({email}, {password})")

class Payment(ABC):
    @abstractmethod
    def make_payment():
        pass

class CreditCardPayment(Payment):
    def __init__(self, user, name, card_number, cvv, expiration_date, zip_code):
        self.user = user
        self.name = name
        self.card_number = card_number
        self.cvv = cvv
        self.expiration_date = expiration_date
        self.zip_code = zip_code
    
    def make_payment():
        pass      

class BankPayment(Payment):
    def __init__(self, name, account_number, routing_number):
        self.name = name = name
        self.account_number = account_number
        self.routing_number = routing_number
    
    def make_payment():
        pass
    
class Review:
    def __init__(self, user, product, rating, description):
        self.user = user
        self.product = product
        self.rating = rating
        self.description = description

class Product(ABC):
    pass

class Book(Product):
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class Electronics(Product):
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class Notification(ABC):
    @abstractmethod
    def send_notification():
        pass

class OrderConfirmationNotification(Notification):
    def send_notification(msg, user):
        return "Send message '{msg}' to user '{user}'"

class PaymentConfirmationNotification(Notification):
    def send_notification(msg, user):
        return "Send message '{msg}' to user '{user}'"

class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
    
    def remove_from_cart(self, product):
        self.cart.pop(product)
    




        
        

    
