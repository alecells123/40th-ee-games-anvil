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
    self.load_attributes_graph()

  def load_attributes_graph(self):
    self.attributes_plot.data = go.Barpolar(
      name = "Attributes Plot",
      theta = ["Strength", "Coordination", "Intellect", "Social"],
      r = [1, 2, 3, 4],
      
      marker_color = ['#FF2222','#22FF22','#2222FF','#FFFF22'],
      marker_line_color = "#000000",
      marker_line_width = 1,
      opacity = 0.8
    )

  def load_basic_skills_graph(self):
    pass

  def load_combat_skills_graph(self):
    pass
  
  def ctab1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(1)
  
  def ctab2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(2)


  
 