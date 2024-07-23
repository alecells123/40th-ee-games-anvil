from ._anvil_designer import CharacterContentTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CharacterContent(CharacterContentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.player_info = anvil.server.call('get_player_info')
    self.character_headline_label.text = "Welcome, "+self.player_info['family_name']+"!"
    self.character_name_label = self.player_info['character']['name']