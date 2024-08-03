from ._anvil_designer import AgendaAdminTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AgendaAdmin(AgendaAdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def act1_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def act2_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def act3_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
