from ._anvil_designer import CharacterPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CharacterPage(CharacterPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    player_info = anvil.server.call('get_player_info')
    self.given_name = player_info['given_name']
    self.middle_name = player_info['middle_name']
    self.family_name = player_info['family_name']
    self.picture = player_info['picture']
    self.affiliate = player_info['affiliate']
    self.character = player_info['character']

    # Any code you write here will run when the form opens.
    self.welcome_label.text = str("Welcome, "+self.given_name+" "+self.middle_name+" "+self.family_name+"!")
    self.character_name_label.text = str(self.character['name'])
    self.affiliate_name_label.text = str(self.affiliate['name'])
    self.profile_pic.source = self.picture
    
    
  def collapse_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.character_intro_panel.visible:
      self.character_intro_panel.visible = False
      self.collapse_button.text = "Stop...collapsing"
    else:
      self.character_intro_panel.visible = True
      self.collapse_button.text = "Collapse"