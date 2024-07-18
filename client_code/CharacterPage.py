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
    #self.column_panel_1.col_spacing = None

  def collapse_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.character_intro_panel.visible:
      self.character_intro_panel.visible = False
      self.collapse_button.text = "Stop...collapsing"
    else:
      self.character_intro_panel.visible = True
      self.collapse_button.text = "Collapse"
