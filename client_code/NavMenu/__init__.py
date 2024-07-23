from ._anvil_designer import NavMenuTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class NavMenu(NavMenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def character_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    if properties['tab'] != 'CHARACTER':
      open_form('CharacterPage')

  def players_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    if properties['tab'] != 'PLAYERS':
      open_form('PlayersPage')
