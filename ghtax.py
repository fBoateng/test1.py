# calculating the tax on an item purchased
priceOfItem = int(input('Please enter the price of item? '))

# calculating nhis and getfund @ 5%
nhisGetfund = priceOfItem * 5 / 100
Covid_19Levy = priceOfItem * 1/100

# calculating VAT12% on item
VAT = (nhisGetfund+Covid_19Levy+priceOfItem)*12.5/100
actualPriceofItem = priceOfItem - VAT

print(f'Your total is {actualPriceofItem} cedis. VAT is {VAT} cedis \n'
      f'{nhisGetfund} cedis for NHIS and COVID-19 is {Covid_19Levy} cedis.\n'
      f'Thank you for your purchase, please come again.')