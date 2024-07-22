from ._anvil_designer import MainPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MainPage(MainPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    self.player_info = anvil.server.call('get_player_info')

    #if (properties['curr_page'] == 'CHARACTER'):
      #self.content_panel.open_form('CharacterContent')
      #self.character_headline_label.text = "Welcome, "+self.player_info['given_name']+"!"
      #self.character_name_label = self.player_info['character']['name']

  def nav_link_click(self, **event_args):
    """A generalised click handler that you can bind to any nav link."""
    # Find out which Form this Link wants to open
    open_form(event_args['sender'].tag.form_to_open)