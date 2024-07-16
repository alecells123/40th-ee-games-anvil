from ._anvil_designer import StartPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

#
# This is the Python code that makes this feedback form work.
# It's a Python class, with a method that runs when the user
# clicks the SUBMIT button.
#
# When the button is clicked, we send the contents of the
# text boxes to our Server Module. The Server Module records
# the feedback in the database, and sends an email to the
# app's owner (that's you!).
#
# To find the Server Module, look under "Server Code" on the
# left.
#


class StartPage(StartPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.state = "Start"

    # Any code you write here will run when the form opens.

  def clear_inputs(self):
    pass

  def new_player_button_click(self, **event_args):
    self.new_player_card.visible = True