####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Git Baked"
signature_flavors = ['tuna', 'salmon', 'red herring']
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print ("Our menu:")
    for m in menu:
        print ("-" + m + " KD %2d" % menu[m]) 

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for flavor in original_flavors:
        print ("-" + flavor)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for signat in original_flavors:
        print ("-" + signat)



def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if (order in menu) or( order in original_flavors) or (order in signature_flavors):
        return True
    else:
        return False 


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []

    # your code goes here!
    while True :
        user_input = input("whats your order? (Enter the exact spelling of the item you want. Type 'Exit' to end your order)")
        if(is_valid_order(user_input)):
            order_list.append(user_input)
        elif user_input == "Exit":
            break
        else: 
            print("erorr")
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if (total > 5):
        return True 
    else :
        return False




def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        if (order in menu):
            total += menu[order]
        elif (order in original_flavors):
            total += original_price
        elif (ordr in signature_flavors):
            total += signature_price 

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for order in order_list:
        print (order)
    price = get_total_price(order_list)
    print (price) 
    if accept_credit_card(price):
        print ("you can pay with cridet ")
    else:
        print ("you can pay cash only")
    print ("Thank you for shopping at %s" % cupcake_shop_name)


