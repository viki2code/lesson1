def format_price(price):
    price_int = int(price)
    result = 'Цена: '+str(price_int)+' руб.'
    return result
name_price = format_price(56.24)
print (name_price)