from ._anvil_designer import ReturningPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ReturningPage(ReturningPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def join_button_click(self, **event_args):
    """This method is called when the button is clicked"""

    first = self.given_name.text
    middle = self.middle_name.text
    last = self.last_name.text
    if anvil.server.call('attempt_login', first, middle, last):
      open_form(('PlayerPages.CharacterPage'))
    else: 
      self.error_message.visible = True
      

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('PlayerPages.StartPage')
