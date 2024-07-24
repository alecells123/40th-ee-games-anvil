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

def get_contestant(contestant: int):
  if anvil.server.session[str(contestant)] is None:
    contestant_row = app_tables.contestants.get(ID=contestant)
    anvil.server.session[str(contestant)] = {
      'name': contestant_row['name'],
      
      'strength': contestant_row['strength'],
      'coord': contestant_row['coordination'],
      'intellect': contestant_row['intellect'],
      'social': contestant_row['social'],
  
      'convince': contestant_row['convince'],
      'engineer': contestant_row['engineer'],
      'know': contestant_row['know'],
      'perceive': contestant_row['perceive'],
      'utilize': contestant_row['utilize'],
      'subskills': contestant_row['subskills'],
      
      'brawl': contestant_row['brawl'],
      'shoot': contestant_row['shoot'],
      'strike': contestant_row['strike'],
      'throw': contestant_row['throw'],
  
      'drug': contestant_row['primary_drug'],
      'ability': contestant_row['ability'],
      'max_injuries': contestant_row['max_injuries'],
      'max_sanity': contestant_row['sanity'],
      'defense': contestant_row['defense'],
      'initiative': contestant_row['initiative']
      }
  return (anvil.server.session[str(contestant)])