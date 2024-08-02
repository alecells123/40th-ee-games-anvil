from ._anvil_designer import ContestantsPrintRepeatableTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ContestantsPrintRepeatable(ContestantsPrintRepeatableTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.name_label.text = self.item.get('name', '')
    self.relationships_label.text = self.item.get('relationships', '')
    self.goals_label.text = self.item.get('goals', '')

    self.primary_drug_label.text = self.item.get('primary_drug', '')
    self.ability_name_label.text = self.item.get('ability_name', '')

    self.max_injuries_label.text = self.item.get('max_injuries', '')
    self.max_sanity_label.text = self.item.get('max_sanity', '')
    
    # Additional fields from the YAML file
    self.injuries_label.text = self.item.get('injuries', '')
    self.drug_label.text = self.item.get('drug', '')
    self.sanity_label.text = self.item.get('sanity', '')
    self.behavious_label.text = self.item.get('behavious', '')
    self.defense_label.text = self.item.get('defense', '')
    self.initiative_label.text = self.item.get('initiative', '')
    self.strength_label.text = self.item.get('strength', '')
    self.convince_label.text = self.item.get('convince', '')
    self.brawl_label.text = self.item.get('brawl', '')
    self.coordination_label.text = self.item.get('coordination', '')
    self.engineer_label.text = self.item.get('engineer', '')
    self.shoot_label.text = self.item.get('shoot', '')
    self.intellect_label.text = self.item.get('intellect', '')
    self.know_label.text = self.item.get('know', '')
    self.strike_label.text = self.item.get('strike', '')
    self.social_label.text = self.item.get('social', '')
    self.perceive_label.text = self.item.get('perceive', '')
    self.throw_label.text = self.item.get('throw', '')
    self.utilize_label.text = self.item.get('utilize', '')
    self.subskills_label.text = self.item.get('subskills', '')