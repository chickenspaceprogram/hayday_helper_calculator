

recipes = {
    'egg' : {
        'wheat' : 2 / 3,
        'corn' : 1 / 3
    },
    'milk' : {
        'corn' : 1 / 3,
        'soybean' : 2 / 3
    },
    'bacon' : {
        'carrot' : 2 / 3,
        'soybean' : 1 / 3
    },
    'wool' : {
        'wheat' : 1,
        'soybean' : 1 / 3
    },
    'goat milk' : {
        'wheat' : 1 / 3,
        'carrot' : 2 / 3,
        'corn' : 1 / 3
    },
    'brown sugar' : {
        'sugarcane' : 1
    },
    'white sugar' : {
        'sugarcane' : 2
    },
    'syrup' : {
        'sugarcane' : 4
    },
    'cream' : {
        'corn' : 1 / 3,
        'soybean' : 2 / 3
    },
    'butter' : {
        'corn' : 2 / 3,
        'soybean' : 4 / 3
    },
    'cheese' : {
        'corn' : 1,
        'soybean' : 2
    },
    'goat cheese' : {
        'wheat' : 2 / 3,
        'carrot' : 4 / 3,
        'corn' : 2 / 3
    }
}

crops = {
    'wheat' : 0,
    'corn' : 0,
    'carrot' : 0,
    'soybean' : 0,
    'sugarcane' : 0
}

helpers_used = input("If you are using both helpers, enter 'both'. If you are using just Ernest or Rose, enter 'e' or 'r' respectively.\n").lower()

while helpers_used not in {'both', 'e', 'r'}:
    helpers_used = input("If you are using both helpers, enter 'both'. If you are using just Ernest or Rose, enter 'e' or 'r' respectively.\n").lower()

item_amounts = {}

if helpers_used == 'both' or helpers_used == 'r':
    print("Enter the max number of each item Rose will produce: ")
    item_amounts['egg'] = int(input("Eggs: ")) + 18
    item_amounts['milk'] = int(input("Milk: ")) + 15
    item_amounts['wool'] = int(input("Wool: ")) + 15
    item_amounts['bacon'] = int(input("Bacon: ")) + 15
    item_amounts['goat milk'] = int(input("Goat milk: ")) + 12
    print("\nEnter the amount of each item currently in Rose's storage: ")
    item_amounts['egg'] -= int(input("Eggs: "))
    item_amounts['milk'] -= int(input("Milk: "))
    item_amounts['wool'] -= int(input("Wool: "))
    item_amounts['bacon'] -= int(input("Bacon: "))
    item_amounts['goat milk'] -= int(input("Goat milk: "))
    print()
if helpers_used == 'both' or helpers_used == 'e':
    print("Enter the max number of each item Ernest will produce: ")
    item_amounts['cream'] = int(input("Cream: "))
    item_amounts['butter'] = int(input("Butter: "))
    item_amounts['cheese'] = int(input("Cheese: "))
    item_amounts['goat cheese'] = int(input("Goat cheese: "))
    item_amounts['brown sugar'] = int(input("Brown sugar: "))
    item_amounts['white sugar'] = int(input("White sugar: "))
    item_amounts['syrup'] = int(input("Syrup: "))
    print("\nEnter the amount of each item currently in Ernest's storage: ")
    item_amounts['cream'] -= int(input("Cream: "))
    item_amounts['butter'] -= int(input("Butter: "))
    item_amounts['cheese'] -= int(input("Cheese: "))
    item_amounts['goat cheese'] -= int(input("Goat cheese: "))
    item_amounts['brown sugar'] -= int(input("Brown sugar: "))
    item_amounts['white sugar'] -= int(input("White sugar: "))
    item_amounts['syrup'] -= int(input("Syrup: "))

for item in item_amounts: 
    for crop in recipes[item]:
        crops[crop] += item_amounts[item] * recipes[item][crop]
print('\n')
for crop in crops:
    print(f"{crop}:\t\t{crops[crop]}")