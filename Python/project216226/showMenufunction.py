menu = {
    "Monday": {
        "Breakfast": "Paratha Chai",
        "Noon": "Mix Sabzi",
        "Dinner":"Alo Ghost"
    },
    "Tuesday":{
        "Breakfast": "Paratha Chai",
        "Noon":"Daal",
        "Dinner":"Mix Chawal"
    },
    "Wednesday":{
        "Breakfast": "Bread Jam",
        "Noon":"Lobia",
        "Dinner":"Microni"
    },
    "Thursday":{
        "Breakfast": "Paratha Chai",
        "Noon":"Sabzi",
        "Dinner":"Kabali Palow"
    },
    "Friday":{
        "Breakfast": "Bread Jam",
        "Noon":"Lobia",
        "Dinner":"Kaleji"
    },
    "Saturday":{
        "Breakfast": "Paratha Chai",
        "Noon":"Cholay",
        "Dinner":"Biryani"
    },
    "Sunday":{
        "Breakfast": "Paratha Anda Chai",
        "Noon":"Alo",
        "Dinner":"Ghost"
    },
}


def showMenu(menu:dict):
    # this function will show the weekly Menu which will be stored in Menu.json
    print(f"Day \t\t Breakfast \t\t Afternoon\t\t Dinner")
    # keyys = []
    for i in menu.keys():
        # for j in menu[i].key():
        #     keyys.append(i)
        print(f"{i}>---------<{menu[i]['Breakfast']}>---------<{menu[i]['Noon']}>---------<{menu[i]['Dinner']} ")

        



