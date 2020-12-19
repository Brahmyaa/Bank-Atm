class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def checkBalance(self):
        print("Your balance is 50000")

def main():
    card_number = input("enter your card number: ")
    pin_number  = input("enter your pin number: ")

    new_user =  Atm(card_number, pin_number)

if __name__ == "__main__":
    main()