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
  # Get player counts for every table
  ee_row = app_tables.affiliates.get(name="Experience Everything Body Rentals")
  ee_count = ee_row['player_count']

  alpha_row = app_tables.affiliates.get(name="Alpha Computing and Data")
  alpha_count = alpha_row['player_count']

  itf_row = app_tables.affiliates.get(name="In The Feels Designer Drugs")
  itf_count = itf_row['player_count']

  fr_row = app_tables.affiliates.get(name="For Reals Nature Synthetics")
  fr_count = fr_row['player_count']

  trax_row = app_tables.affiliates.get(name="Trax's Terraforming")
  trax_count = trax_row['player_count']
  
  return [["EE", "Alpha", "ITF", "FR", "Trax"], [ee_count, alpha_count, itf_count, fr_count, trax_count], 'Bar Chart Example']

@anvil.server.callable
def submit(first, middle, family, picture, affiliate): 
  affiliate_row = app_tables.affiliates.get(name=affiliate)
  character_row = app_tables.characters.get(q.any_of(affiliate=affiliate_row, has_player=False))
  character_row['has_player'] = True
  # Add the data row and add it to the session
  anvil.server.session["player_info"] = app_tables.players.add_row(given_name=first, middle_name=middle, family_name=family, picture=picture, affiliate=affiliate_row, character=character_row)

@anvil.server.callable
def get_player_info():
  return anvil.server.session["player_info"]

@anvil.server.callable
def get_agendas():
  player_info = get_player_info()
  
  return 