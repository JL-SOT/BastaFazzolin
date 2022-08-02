# Defining the dictionary items menus
brunch = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}
# start_time and end_time = 24 hour clock(11 & 16)
early_bird = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00
}
# start_time and end_time = 15 & 18
dinner = {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00,
}
# start_time and end_time = 17 & 23
kids = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}
# start_time and end_time = 11 & 21

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"This {self.name} menu is avaible between {self.start_time} and {self.end_time} O'clock"

    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return(total)

# Menus:
brunch_menu = Menu("brunch", brunch, 11, 16)
early_bird_menu  = Menu("Early Bird", early_bird,15, 18)
dinner_menu = Menu("Dinner", dinner, 17, 23)
kids_menu = Menu("Kids", kids, 11, 21)
menus = brunch_menu, early_bird_menu, dinner_menu, kids_menu

# print(brunch_menu)
# print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

class Franchise:

    def __init__(self, name, address, menus):
        self.name = name
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f"Our {self.name} is located {self.address}"

    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
        return(available_menu)


flagship_store = Franchise("flagship store", "1232 West End Road", menus)
new_installment = Franchise("new installation", "12 East Mulberry Street", menus)

# print(flagship_store)
# print(new_installment)
print(new_installment.available_menus(12))
print(flagship_store.available_menus(17))

# ------NEW RESTAURANT-------
arepas_menu = {
  'arepa pabellon': 7.00,
  'pernil arepa': 8.50,
  'guayanes arepa': 8.00,
  'jamon arepa': 7.50
}

arepas_place = Franchise("Take a' Arepa franchise","189 Fitzgerald Avenue", arepas_menu)
print(arepas_place)

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

basta_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepa_business = Business("Take a' Arepa", arepas_place)
