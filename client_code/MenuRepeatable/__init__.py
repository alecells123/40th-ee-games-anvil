from ._anvil_designer import MenuRepeatableTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MenuRepeatable(MenuRepeatableTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.menu_name_label.text = self.item['name']
    self.menu_affiliate_label.text = self.item['affiliate']
    self.menu_cost_label.text = self.item['cost']
    self.menu_description_label.text = self.item['description']