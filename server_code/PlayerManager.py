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
  affiliate_row.update(player_count=)
  
  character_results = app_tables.characters.search(q.all_of(affiliate=affiliate_row, has_player=False))
  character_row = character_results[0]
  character_row['has_player'] = True

  # Strip all the things
  first = first.strip(" ,./!@#$%^&*()-_=+{}[];")
  middle = middle.strip(" ,./!@#$%^&*()-_=+{}[];")
  family = family.strip(" ,./!@#$%^&*()-_=+{}[];")

  
  # Add the data row and add it to the session
  anvil.server.session["player_info"] = app_tables.players.add_row(given_name=first, middle_name=middle, family_name=family, picture=picture, affiliate=affiliate_row, character=character_row)

@anvil.server.callable
def get_player_info():
  if "player_info" in anvil.server.session:
    player_info = anvil.server.session["player_info"]
    print(f"Player info found in session: {player_info}")
    return player_info
  else:
    print("No player info found in session.")
    return None

@anvil.server.callable
def get_agendas():
  # Get player from database
  session_data = get_player_info()
  if session_data is None:
    print("No session data available.")
    return None

  player_info = app_tables.players.get(
    given_name=session_data['given_name'], 
    middle_name=session_data['middle_name'], 
    family_name=session_data['family_name']
  )
  
  if player_info is None:
    print("No player info found in database.")
    return None

  print(f"Player info retrieved: {player_info}")
  return player_info['agendas']

@anvil.server.callable
def get_players():
  return app_tables.players.search()

@anvil.server.callable
def add_agenda(name, affiliate, flavor, description, reward):
  app_tables.agendas.add_row(name=name, affiliate=affiliate, flavor=flavor, description=description, reward=reward)

@anvil.server.callable
def assign_agenda(agenda):
  player_info = get_player_info()
  player_info['agendas'] = agenda
  player_info.save()

@anvil.server.callable
def attempt_login(first, middle, last):
  player_row = app_tables.players.get(q.all_of(given_name=first, middle_name=middle, family_name=last))
  if player_row is not None:
    anvil.server.session['player_info'] = player_row
    return True
  else:
    return False