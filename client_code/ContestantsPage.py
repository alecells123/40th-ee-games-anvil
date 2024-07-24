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
    self.contestant = anvil.server.call('get_contestant', new_contestant)
    self.contestant_name_label1.text = self.contestant['name']
    self.relationships_label.text = self.contestant.get('relationships')
    self.contestant_pic.source = self.contestant['picture']

  def get_attributes_graph():
    pass

  def get_basic_skills_graph():
    pass

  def get_combat_skills_graph():
    pass
  
  def ctab1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(1)
  
  def ctab2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(2)


  
 