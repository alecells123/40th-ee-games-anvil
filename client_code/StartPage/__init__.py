from ._anvil_designer import StartPageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

#
# This is the Python code that makes this feedback form work.
# It's a Python class, with a method that runs when the user
# clicks the SUBMIT button.
#
# When the button is clicked, we send the contents of the
# text boxes to our Server Module. The Server Module records
# the feedback in the database, and sends an email to the
# app's owner (that's you!).
#
# To find the Server Module, look under "Server Code" on the
# left.
#


class StartPage(StartPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.picture = Media()
    self.continue_flow = True

  def clear_inputs(self):
    pass

  def new_player_button_click(self, **event_args):
    self.start_card.visible = False
    self.new_player_card.visible = True

  def existing_player_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ReturningPage')

  def picture_uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.uploaded_picture_display.source = self.picture_uploader.file
    self.uploaded_picture_display.visible = True

  def new_player_continue_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.given_name_text_box.text == "":
      self.given_blank_message.visible = True
      self.continue_flow = False
    else: 
      self.given_blank_message.visible = False
      self.continue_flow = True

    if self.middle_name_text_box.text == "":
      self.middle_blank_message.visible = True
      self.continue_flow = False
    else: 
      self.middle_blank_message.visible = False
      self.continue_flow = True

    if self.picture_uploader.file is None:
      self.picture_blank_message.visible = True
      self.continue_flow = False
    else: 
      self.picture_blank_message.visible = False
      self.continue_flow = True

    if self.continue_flow:
      self.new_player_card.visible = False
      self.character_card.visible = True
      self.displayAffiliatePlot()

  def displayAffiliatePlot(self):
    args = anvil.server.call(('get_player_count_data'))
    self.current_team_spread_plot.data = go.Bar(
      x = args[0],
      y = args[1],
      name = args[2]
    )
  
  def back_new_player_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.new_player_card.visible = False
    self.start_card.visible = True

  def ee_info_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.ee_description.visible:
      self.ee_description.visible = False
      self.ee_info_button.text = "info"
    else:
      self.ee_description.visible = True
      self.ee_info_button.text = "close"

  def alpha_info_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.alpha_description.visible:
      self.alpha_description.visible = False
      self.alpha_info_button.text = "info"
    else:
      self.alpha_description.visible = True
      self.alpha_info_button.text = "close"

  def itf_info_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.itf_description.visible:
      self.itf_description.visible = False
      self.itf_info_button.text = "info"
    else:
      self.itf_description.visible = True
      self.itf_info_button.text = "close"

  def fr_info_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.fr_description.visible:
      self.fr_description.visible = False
      self.fr_info_button.text = "info"
    else:
      self.fr_description.visible = True
      self.fr_info_button.text = "close"

  def trax_info_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.trax_description.visible:
      self.trax_description.visible = False
      self.trax_info_button.text = "info"
    else:
      self.trax_description.visible = True
      self.trax_info_button.text = "close"

  def refresh_plot_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.displayAffiliatePlot()

  def submit_affiliate_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    given_name = str(self.given_name_text_box.text)
    middle_name = str(self.middle_name_text_box.text)
    family_name = str(self.family_name_text_box.text)
    picture = self.picture_uploader.file
    
    affiliate = ""
    if self.ee_radio.selected:
      affiliate = "Experience Everything Body Rentals"
    elif self.alpha_radio.selected:
      affiliate = "Alpha Computing and Data"
    elif self.itf_radio.selected:
      affiliate = "In The Feels Designer Drugs"
    elif self.fr_radio.selected:
      affiliate = "For Reals Nature Synthetics"
    elif self.trax_radio.selected:
      affiliate = "Trax's Terraforming"
    
    anvil.server.call('submit', given_name, middle_name, family_name, picture, affiliate)

    open_form('CharacterPage')
