import json

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
    'goat miik' : {
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
with open('recipes.json', 'w') as recipesFile:
    json.dump(recipes, recipesFile)

