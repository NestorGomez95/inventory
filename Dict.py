Mystorage= "Electronic shop"

print(f"welcome to my: {Mystorage}")

stock_products = {"TV": 7, "MICROPHONE":15, "DRUMS": 20, "HAMMER": 12, "PC": 23, "MOUSE":  18 }

try:
    resp = ""

    while resp != "N":
        prod = input("enter the product that you want to buy: ").upper()
        if prod in stock_products: 
            Quant = int(input("enter the quantity of products to buy: "))
            actual_stock = stock_products[prod]
            if Quant>actual_stock:
                print("Not enough stock")
            else:
                stock_products[prod] -= Quant
                print("the actual stock is {}".format(stock_products[prod]))
        else:
            print("product does not exist")
        resp = input("would you like to buy another thing(Y/N)").upper()

except:
    print("try again")