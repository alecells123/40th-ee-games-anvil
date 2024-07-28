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
    self.change_contestant(1)

  def change_contestant(self, new_contestant: int) -> None:
    self.current_contestant = new_contestant
    self.load_contestant(new_contestant)

  def load_contestant(self, new_contestant: int):
    self.contestant = anvil.server.call('get_contestant', new_contestant)
    self.contestant_name_label1.text = self.contestant['name']
    self.relationships_label.text = self.contestant.get('relationships')
    self.contestant_pic.source = self.contestant['picture']
    
    self.load_attributes_graph()
    
    self.load_basic_skills_graph()
    self.list_basic_subskills_label.text = self.contestant['subskills']
    
    self.load_combat_skills_graph()
    
    self.primary_drug_label.text = "Primary Drug: " + str(self.contestant['drug']).capitalize()
    self.ability_name_label.text = "Ability Name: " + str(self.contestant['ability']).capitalize()
    self.max_injuries_label.text = "Max Injuries: " + str(self.contestant['max_injuries'])
    self.max_sanity_label.text = "Max Sanity: " + str(self.contestant['max_sanity'])
    self.defense_label.text = "Defense: " + str(self.contestant['defense'])
    self.initiative_label.text = "Base Initiative: " + str(self.contestant['initiative'])

  def load_attributes_graph(self):
    y_set = [
            self.contestant['strength'], 
            self.contestant['coord'], 
            self.contestant['intellect'],
            self.contestant['social']
            ]
    
    self.attributes_plot.data = go.Bar(
      name = "Attributes Plot",
      x = ["Strength", "Coordination", "Intellect", "Social"],
      y = y_set,
      height = 5,
      marker_color = ['#FF2222','#22FF22','#2222FF','#FFFF22'],
      marker_line_color = "#000000",
      marker_line_width = 1,
      opacity = 0.8
    )

  def load_basic_skills_graph(self):
    y_set = [
            self.contestant['convince'], 
            self.contestant['engineer'], 
            self.contestant['know'],
            self.contestant['perceive'],
            self.contestant['utilize']
            ]
    
    self.basic_skills_plot.data = go.Bar(
      name = "Attributes Plot",
      x = ["Convince", "Engineer", "Know", "Perceive", "Utilize"],
      y = y_set,
      marker_line_color = "#000000",
      marker_line_width = 1,
      opacity = 0.8
    )

  def load_combat_skills_graph(self):
    y_set = [
            self.contestant['brawl'], 
            self.contestant['shoot'], 
            self.contestant['strike'],
            self.contestant['throw']
            ]
    
    self.combat_skills_plot.data = go.Bar(
      name = "Attributes Plot",
      x = ["Brawl", "Shoot", "Strike", "Throw"],
      y = y_set,
      marker_line_color = "#000000",
      marker_line_width = 1,
      opacity = 0.8
    )
  
  def ctab1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(1)
  
  def ctab2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(2)

  def ctab3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(3)
  
  def ctab4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(4)

  def ctab5_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(5)
  
  def ctab6_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(6)

  def ctab7_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(7)
  
  def ctab8_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(8)

  def ctab9_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(9)
  
  def ctab10_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(10)

  def ctab11_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(11)
  
  def ctab12_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(12)

  def ctab13_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(13)
  
  def ctab14_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(14)

  def ctab15_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(15)
  
  def ctab16_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(16)

  def ctab17_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(17)
  
  def ctab18_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(18)

  def ctab19_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(19)
  
  def ctab20_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(20)

  def ctab21_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(21)
  
  def ctab22_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(22)

  def ctab23_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(23)
  
  def ctab24_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.change_contestant(24)