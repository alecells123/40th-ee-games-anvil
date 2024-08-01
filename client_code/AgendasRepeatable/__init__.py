from ._anvil_designer import AgendasRepeatableTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AgendasRepeatable(AgendasRepeatableTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.agenda_name_label.text = self.item['name']
    self.agenda_affiliate_label.text = self.item['affiliate']['name']
    self.agenda_flavor_label.text = self.item['flavor']
    self.agenda_description_label.text = self.item['description']
