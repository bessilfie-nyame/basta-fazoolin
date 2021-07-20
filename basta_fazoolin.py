from datetime import time ,datetime, timedelta 

def check_time_interval(time1, time2):
  fmt = '%H:%M:%S'
  # get time interval between time1 and time2 as timedelta object
  time_interval = datetime.strptime(str(time1), fmt) - datetime.strptime(str(time2), fmt)
  return (time_interval >= timedelta(0))

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items 
    self.start_time = start_time
    self.end_time = end_time

  def get_start_time(self):
    return self.start_time

  def get_end_time(self):
    return self.end_time

  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      bill += self.items[purchased_item]
    return bill

  def __repr__(self):
    return ("{} menu available from {} GMT to {} GMT".format(self.name, self.start_time, self.end_time))



brunch = Menu("brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, time(11), time(16))

early_bird = Menu("early_bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, time(15), time(18))

dinner = Menu("dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, time(17), time(23))

kids = Menu("kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, time(11), time(21))

print(brunch)
print(brunch.calculate_bill(["pancakes", "home fries","coffee"]))
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def available_menus(self, check_time):
    return [menu for menu in self.menus if (check_time_interval(time(check_time), menu.get_start_time()) and check_time_interval(menu.get_end_time(),time(check_time)))]

  def __repr__(self):
    return ("Welcome to Franchise at {}".format(self.address))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
  
flagship_store_menus_available_12pm = flagship_store.available_menus(12)

new_installment_menus_available_12pm = new_installment.available_menus(12)

print("menus at flagship_store at 12 noon: ")
for menu in flagship_store_menus_available_12pm:
  print(menu)
print(" ")
print("menus at new_installment at 12 noon: ")
for menu in new_installment_menus_available_12pm:
  print(menu)


flagship_store_menus_available_5pm = flagship_store.available_menus(17)
new_installment_menus_available_5pm = new_installment.available_menus(17)
print(" ")

print("menus at flagship_store at 5pm: ")
for menu in flagship_store_menus_available_5pm:
  print(menu)
print(" ")
print("menus at new_installment at 5pm: ")
for menu in new_installment_menus_available_5pm:
  print(menu)
print(" ")


class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = Menu("arepas_menu", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, time(10), time(20))

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

new_business = Business("Take a' Arepa", [arepas_place])

























