from ._anvil_designer import StartPageTemplate
from anvil import *
import anvil.users
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
    self.start_state = self.start_state_label
    self.create_player_state = self.create_player_state_label
    self.starting_character = self.start

    # Any code you write here will run when the form opens.

  def clear_inputs(self):
    pass

  def new_player_button_click(self, **event_args):
    self.start_card.visible = False
    self.new_player_card.visible = True
    self.generate_new_player_card()

  def generate_new_player_card(self):
    self.given_name = self.given_name_text_box
    self.middle_name = self.middle_name_text_box
    self.family_name = self.family_name_text_box
    self.picture = self.picture_uploader
    print("yay")

  def change_state(self, new_state):
    self.state = new_state
    match self.state:
      case "Start":
        self.start_state_label.background.default
      case "":
        pass