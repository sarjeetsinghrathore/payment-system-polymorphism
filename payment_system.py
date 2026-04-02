# Zomato Payment System

class PaymentSystem:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def pay_amount(self):
        print("The Payment has been done!")

    def summary(self):
        print("This is the summary of the order!")
        print("Customer Name:", self.customer_name)


# Credit Card Payment
class CreditCard(PaymentSystem):
    def pay_amount(self):
        print("Payment has been done using Credit Card")


# UPI Payment
class UPIPayment(PaymentSystem):
    def pay_amount(self):
        print("Payment has been done through UPI")


# Create objects
card = CreditCard("Sarjeet Singh Rathore")
upi = UPIPayment("Sarjeet Singh Rathore")

# Call methods
card.pay_amount()
card.summary()

upi.pay_amount()
upi.summary()
