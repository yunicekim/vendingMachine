import sys

class Product:
    productType={"1":"Milk coffee", "2":"Sugar coffee", "3":"Black coffee"}
    productValue={"1":2, "2": 3, "3":4}

class CoffeeVM(Product):
    _name = "Coffee"
    def __init__(self):
        print("This is {} vending machine\n".format(self._name))

    def run(self):
        
        while True:
            try:
                deposit = int(input("Insert coins : $"))
            except ValueError:
                print("Entered wrong input!")
            else:
                self.selectProduct(deposit)

    def selectProduct(self, deposit):
        while deposit >= 0 :
            self.showMenu()
            while True:
                selection = input("Select one to buy : ")
                # if not 1 <= int(selection) < 4:
                if int(selection) not in range(1, 4):
                    # print(selection)
                    print("Entered Wrong input")
                else:
                    if deposit < self.getProductValue(selection):
                        print("Balance is not enough. ")
                    else:
                        deposit = self.payment(deposit, selection)
                        print("Balance : ${} \n".format(deposit))
                        more = input("Want more? (y/n)")
                        if (more.lower() == 'n' ):
                            print("Thank you for buying!")
                            sys.exit(-1)

    def payment(self, deposit, selection):
        price = self.getProductValue(selection)        
        return deposit - price

    def showMenu(self):
        for number, item in Product.productType.items():
            price = self.getProductValue(number)
            print("{}. {} - ${}".format(number, item, price))

    def getProductValue(self, selection):
        for number, value in Product.productValue.items():
            if number == selection:
                return value

class SnackVM(CoffeeVM):
    _name = "Snack"

    def __init__(self):
        print("This is {} vending machine\n".format(self._name))
        Product.productType = {"1": "Cereal Bar", "2": "Layes", "3": "Nacho"}
        Product.productValue = {"1": 1, "2": 2, "3": 3}

if __name__=='__main__':
    print("1. Coffee, 2. Snack")
    option = input("Select to run : ").strip()

    if option == "1":
        vm = CoffeeVM()
    elif option == "2":
        vm = SnackVM()
    else:
        print("Pushed the wrong option. Try it again")
        sys.exit(-1)
    
    vm.run()