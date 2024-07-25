from ._anvil_designer import AgendasMgrPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AgendasMgrPage(AgendasMgrPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def hide_action_bar_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.center_column_panel.visible = False
