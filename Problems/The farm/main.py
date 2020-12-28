def print_quantity(item, price, money):
    quantity = money // price
    if quantity == 1:
        print(f'1 {item}')
    else:
        if item == 'sheep':
            print(f"{quantity} {item}")
        else:
            print(f"{quantity} {item}s")


def get_price(item):
    units = {'chicken': 23,
             'goat': 678,
             'pig': 1296,
             'cow': 3848,
             'sheep': 6769}
    return units[item]


user_money = int(input())

if user_money < get_price('chicken'):
    print("None")
elif user_money < get_price('goat'):
    print_quantity('chicken', get_price('chicken'), user_money)
elif user_money < get_price('pig'):
    print_quantity('goat', get_price('goat'), user_money)
elif user_money < get_price('cow'):
    print_quantity('pig', get_price('pig'), user_money)
elif user_money < get_price('sheep'):
    print_quantity('cow', get_price('cow'), user_money)
else:
    print_quantity('sheep', get_price('sheep'), user_money)
