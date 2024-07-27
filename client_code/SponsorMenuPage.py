from ._anvil_designer import SponsorMenuPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class SponsorMenuPage(SponsorMenuPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.


  def update_tab(self, menu):
    self.menu_items = anvil.server.call('get_menu', menu)
    self.refresh_data_bindings()

  def dusty_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def delivery_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def drugs_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def information_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def medical_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def nutritional_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def survival_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
