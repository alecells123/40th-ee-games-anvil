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
def get_player_count_data():
  ee_row = app_tables.affiliates.get(name="Experience Everything Body Rentals")
  ee_count = ee_row['player_count']
  return [["Experience Everything Body Rentals", "Alpha Computing and Data", "In The Feels Designer Drugs", "For Reals Nature Synthetics", "Trax's Terraforming"], [ee_count, 1, 6, 2, 4], 'Bar Chart Example']