from ._anvil_designer import AgendaRepeatTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AgendaRepeat(AgendaRepeatTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.agendas = anvil.server.call('get_agendas')
    for everyAgenda in self.agendas:
      pass