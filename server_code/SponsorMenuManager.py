import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_menu(menu):
  match menu:
    case 'advertising':
      return app_tables.menu_advertising.search()
    case 'drugs':
      return app_tables.menu_drugs.search()
    case 'dusty':
      return app_tables.menu_dusty_boxes.search()
    case 'information':
      return app_tables.menu_information.search()
    case 'medical':
      return app_tables.menu_medical.search()
    case 'nutritional':
      return app_tables.menu_nutritional.search()
    case 'survival':
      return app_tables.menu_survival.search()
    case 'traversal':
      return app_tables.menu_traversal.search()
    case 'weapons':
      return app_tables.menu_weapons.search()
    case _:
      return None