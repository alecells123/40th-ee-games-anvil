from ._anvil_designer import ContestantsPageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ContestantsPage(ContestantsPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.current_contestant = 1

  def change_contestant(self, new_contestant: int) -> None:
    self.current_contestant = new_contestant
    self.load_contestant(new_contestant)

  def load_contestant(self, new_contestant: int): 
    anvil.server.call('get_contestant')
  
  def ctab1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(1)
  
  def ctab2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(2)


  
 