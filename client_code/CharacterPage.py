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

    # Any code you write here will run when the form opens.
    self.player_info = anvil.server.call('get_player_info')
    self.character_headline_label.text = "Welcome, " + self.player_info['given_name'] + "!"
    self.character_name_label1.text = self.player_info['character']['name']
