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
    open_form('CharacterPage')

  def players_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('PlayersPage')

  def agendas_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('AgendasPage')

  def corporations_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('CorposPage')

  def contestants_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ContestantsPage')

  def sponsor_menu_tab_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('SponsorMenuPage')
