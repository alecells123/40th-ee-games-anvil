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

  def clear_inputs(self):
    pass

  def new_player_button_click(self, **event_args):
    self.start_card.visible = False
    self.new_player_card.visible = True

  def existing_player_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('CharacterPage')

  def picture_uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file.name.endswith(".jpg") or file.name.endswith(".jpeg") or file.name.endswith(".png"):
      self.pic_uploaded = True
      self.picture = file

  def new_player_continue_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.given_name_text_box.text == "":
      

    
    self.new_player_card.visible = False
    self.character_card.visible = True
    self.displayAffiliatePlot()

  def displayAffiliatePlot(self):
    self.current_team_spread_plot.data = go.Bar(
      x = anvil.server.call('get_player_count_data')[0],
      y = anvil.server.call('get_player_count_data')[1],
      name = anvil.server.call('get_player_count_data')[2]
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
    given_name = str(self.given_name_text_box)
    middle_name = str(self.middle_name_text_box)
    family_name = str(self.family_name_text_box)
    picture = self.picture

    if self.ee_radio.selected:
      affilliate = "Experience Everything Body Rentals"
    elif self.alpha_radio.selected:
      affilliate = "Alpha Computing and Data"
    elif self.itf_radio.selected:
      affilliate = "In The Feels Designer Drugs"
    elif self.fr_radio.selected:
      affilliate = "For Reals Nature Synthetics"
    elif self.trax_radio.selected:
      affilliate = "Trax's Terraforming"

    anvil.server.call('submit', given_name, middle_name, family_name, picture, affilliate)
