import colorama
from colorama import Fore
colorama.init(autoreset=True)

products_0VAT = {'fish':2.0, 'meat': 3.0, 'carrot':1.5, 'tomatoe':1.2}
products_5VAT = {'book': 5.0, 'magazine':3.0, 'towel':2.5}
products_8VAT = {'chips':2.1, 'water':1.0, 'mustard':1.7}
products_23VAT = {'table':24.0, 'chair':18.0, 'tv':36.0}
cart = {}


def show_products():
# adding products lists
    products = {**products_0VAT, **products_5VAT, **products_8VAT, **products_23VAT}
# different way -> products = products_0VAT | products_5VAT | products_8VAT | products_23VAT
    for key, value in products.items():
        print('Product: ', key, '|Price: ', value)
    return products


def show_menu():
    print(Fore.GREEN + '------- Menu ----------')
    print('0. Show products.')
    print(Fore.GREEN + '1. Add product to cart.')
    print('2. Remove product from cart.')
    print(Fore.GREEN + '3. Show cart.')
    print('4. Show total amount to pay after tax.')
    print(Fore.GREEN + '5. Exit.')
    print(Fore.GREEN + '----------------------')


def make_action_in_menu():
    action = input(Fore.BLUE + 'What do you want to do? Press 0-5.')
    return action


def navigate(cart):
    while True:
        show_menu()
        action = make_action_in_menu()
        if action == '0':
            show_products()
            continue
        elif action == '1':
            show_products()
            add_to_cart(cart)
            continue
        elif action == '2':
            show_cart(cart)
            remove_from_cart(cart)
            continue
        elif action == '3':
            show_cart(cart)
            continue
        elif action == '4':
            show_amount_to_pay(cart)
            continue
        elif action == '5':
            break
        else:
            print(Fore.RED + 'Wrong value, try again.')
            continue


def show_cart(cart):
    print(cart)


def show_amount_to_pay(cart):
    total = 0
    for key in cart:
        if key in products_5VAT:
            total += products_5VAT[key] * cart[key] * 1.05
        elif key in products_8VAT:
            total += products_8VAT[key] * cart[key] * 1.08
        elif key in products_23VAT:
            total += products_23VAT[key] * cart[key] * 1.23
        else:
            total += products_0VAT[key] * cart[key]
    print(round(total, 2))


def add_to_cart(cart):
    products = {**products_0VAT, **products_5VAT, **products_8VAT, **products_23VAT}
    product = input(Fore.BLUE + 'What item do you want to add?')
    quantity = input(Fore.BLUE + 'How many of the items do you want to add?')
    if product in products:
        if product in cart:
            cart[product] += int(quantity)
        else:
            cart[product] = int(quantity)
    else:
        print(Fore.RED + 'You messed up something. Try again.')


def remove_from_cart(cart):
    if cart == {}:
        print(Fore.RED + 'There are no products in cart')
    else:
        product = input(Fore.BLUE + 'What item do you want to remove?')
        if product in cart:
            quantity = input(Fore.BLUE + 'How many of the items do you want to remove?')
            cart[product] -= int(quantity)
            if cart[product] <= 0:
                del cart[product]
        else:
            print(Fore.RED + 'No products in cart.')


def main():
    while True:
        navigate(cart)
        break

main()
