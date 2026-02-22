# how to use in dictionary 

tea_prices = {
    "Masala Chai" : 40,
    "Green Tea" : 50,
    "Lemon Tea" : 200,
}

tea_prices_usd = {tea:price / 80 for tea,price in tea_prices.items()}
# here we are mentionning both as expressions and using items() to display both key value pair


print(tea_prices_usd)