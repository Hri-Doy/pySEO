# price = 300
# discount = 0.10 # 10%
# total_discount = price * discount
# print (total_discount)
# discount_price = price - total_discount
# print(discount_price)

#def calculate_price(price, discount = .20): #deafult value

def calculate_price(price, discount):
    """
    :param price: any number
    :param discount: discount will be 10% or 0.10
    :return: new price after discount
    """
    total_discount = price * discount
    discount_price = price - total_discount
    return discount_price
item1 = calculate_price(300, 0.15)
print(item1)

#print(help(calculate_price))