import random

def add_cust(cust_name, number): # customer name as key, ID as value
    if cust_name in cust_dict:
### CHANGED return -> return cust_dict
        return cust_dict
    cust_dict[cust_name] = number
    return cust_dict

### CHANGED removed item_list parameter since we compute here
def add_order(number, item, cust_dict, cust_name): # not done yet, check if customer already in order_dict
    if cust_name in cust_dict:
        number = cust_dict[cust_name]
        if number in order_dict:
            #order_dict[number]=[item]
            order_dict[number].append(item)
            return order_dict
        else:
            order_dict[number] = [item]
            return order_dict

##    if number in cust_dict:             # if they are use the value from cust_dict
##        order_dict[number].append(item)
##        return order_dict
    order_dict[number] = item_list
##    if number in order_dict:
##        order_dict[number].append(item)
    return order_dict




cust_dict={}
order_dict={}
item_list=[]

print("Hello. Welcome to the shop.")
print("Inventory:\nSword: $10\nShield: $8\nArmor: $15\nPotion: $5")
item = str.lower(input("What would you like?\n"))
check=1
while check:
    
    flag = 1
    while flag:
        number = random.randint(10000, 99999)
        if number in cust_dict:
            number = random.randint(10000, 99999)
##        elif number in order_dict:

        else: flag = 0
# customer ID system

#shop_inv={sword: 10, shield: 8, armor: 15, potion: 5}


    #print("Inventory:\nSword: $10\nShield: $8\nArmor: $15\nPotion: $5")

    #item = str.lower(input("What would you like?\n"))
    if item=="sword":
        cust_name=str.upper(input("A sword huh? Alright, can I get your name?\n"))
        add_cust(cust_name, number)
        add_order(number, item, cust_dict, cust_name)
        print(cust_dict, order_dict)
        check=0
    elif item=="shield":
        cust_name=str.upper(input("A shield? Alright, can I get your name?\n"))
        add_cust(cust_name, number)
        add_order(number, item, cust_dict, cust_name)
        print(cust_dict, order_dict)
        check=0
    elif item=="armor":
        cust_name=str.upper(input("Some armor? Alright, can I get your name?\n"))
        add_cust(cust_name, number)
        add_order(number, item, cust_dict, cust_name)
        print(cust_dict, order_dict)
        check=0
    elif item=="potion":
        cust_name=str.upper(input("A potion? Alright, can I get your name?\n"))
        add_cust(cust_name, number)
        add_order(number, item, cust_dict, cust_name)
        print(cust_dict, order_dict)
        check=0
    else:
        item = str.lower(input("Sorry what would you like?\n"))
        
