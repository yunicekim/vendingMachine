import sys

PRICE_UNIT = 100

class texts:
    title = "#### This is class %s vending machine ####"
    product = "%s:%s(%s원)"
    insert_coin = "동전을 넣어 주세요 : "
    n_enough_coin = "동전이 부족합니다. \n 거스름돈은 %s원입니다."
    select_product = "원하시는 상품번호를 선택하세요."
    select_fault = "잘못 누르셨습니다."
    product_out = "선택하신 %s 입니다. 거스름돈은 %s원 입니다. \n 감사합니다."

class Product:
    #제품 종류, 가격을 코드변경 없이 데이터를 쉽게 추가하거나 변경할 수 있다.
    productType = {"1":"설탕커피", "2":"프림커피", "3":"원두커피"}
    productValue = {"1":200, "2":300, "3":400}

class CoffeeVM(Product):
    _name = "커피"

    def __init__(self):
        #사용자가 자판기 종류를 선택하면 _name을 출력한다.
        print(texts.title %self._name)

    def run(self):
        while True:
            try:
                inputCoin = float(input(texts.insert_coin))
            except ValueError:
                #잘못된 값을 입력받으면 에러 메시지를 출력한다.
                print(texts.select_fault)
            else:
                self.selectProduct(inputCoin)
    
    def selectProduct(self, coin):
        #제품 종류를 리스트로 선언하여 코드변경없이 데이터를 동적으로 보여준다.
        description = ''
        for selection, item in Product.productType.items():
             #제품 가격을 가져온다.
            price = self.getProductValue(selection)
            #  description += selection
            description += selection + ':' + item + '(' + str(price) + '원) ' 
            
        print(description)
        inputProduct = input( texts.select_product )
        productValue = self.getProductValue(inputProduct)

        if productValue:
            productName = self.getProductName(inputProduct)
            self.payment(coin, productName, productValue)
        else:
            print(texts.select_fault)
            self.selectProduct(coin)
        
    def getProductValue(self, product):
        returnValue = 0
        for selection, value in Product.productValue.items():
            if selection == product:
                returnValue = value
            
        return returnValue
    
    def getProductName(self, product):
        for selection, name in Product.productType.items():
            if selection == product:
                return name
            
    def payment(self, coin, name, value):
        coinValue = coin * PRICE_UNIT
        if(coinValue >= value):
            balance = coinValue -value
            print(texts.product_out %(name, int(balance)))
        else:
            print(texts.n_enough_coin %int(coinValue))
        #지불을 마치면 초기 메뉴로 이동한다.
        self.run()

#과자 클래스는 커피 클래스를 상속받는다.
class SnackVM(CoffeeVM):
    _name = "과자"

    def __init__(self):
        #Product 제품 종류, 가격을 Overriding한다.
        Product.productType = {"1":"오감자", "2":"오징어땅콩", "3":"빼빼로", "4":"칸초"}
        Product.productValue = {"1":400, "2":500, "3":600, "4": 500}
        print(texts.title %self._name)

if __name__ == '__main__':
    print("1:커피, 2:과자")
    select_vm = input("구동할 자판기를 선택하세요").strip()
    
    if select_vm == "1":
        vm = CoffeeVM()
    
    elif select_vm == "2":
        vm = SnackVM()
    else:
        print("잘못 누르셨습니다. 다시 선택해주세요")
        sys.exit(-1)
    
    try:
        vm.run()
    except KeyboardInterrupt as exc:
        print("판매를 종료합니다.")