from ._anvil_designer import PlayersRepeatableTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class PlayersRepeatable(PlayersRepeatableTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.player_name_label.text = self.item['given_name'] + " " + self.item['family_name']
    self.character_name_label2.text = self.item['character']['name']
    self.corpo_label.text = self.item['character']['affiliate']['name']
    self.profile_picture.source = self.item['picture']
