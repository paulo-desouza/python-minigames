# EX 070: SUPER CHEAP STORE! Make a program that will ask the user what he bought, and how much it costs. Then, asks if
# the user wishes to keep going. After that, it should show what was the cheapest product, and how many products over
# 1000 dollars were bought.
print('-'*20)
print('SUPER CHEAP STORE')
print('-'*20)

count = count1 = total = 0
while True:
    product = str(input('Product Name:'))
    price = float(input('Product Price:'))

    total += price
    if count == 0:
        low = price
        count += 1
    if price < low:
        low = price
    if price > 1000:
        count1 += 1

    ask = str(input('Do you wish to proceed? [Y / N]')).strip().upper()[0]
    while ask not in 'YN':
        ask = str(input('Do you wish to proceed? [Y / N]')).strip().upper()[0]
    if ask == 'N':
        break
    print('-'*20)
print(f'\nYour total is {total:.2f}.\nYou bought {count1} product(s) over a thousand dollars;\n'
      f'The cheapest product you bought was ${low:.2f}.\n'
      f'Thanks for coming, we appreciate you stopping by SUPER CHEAP STORE!')
