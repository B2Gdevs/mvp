import os
import sys
from scene import Scene
import utils

class TextEngine():
  def __init__(self, scenes, player):
    self.scenes = scenes
    self.player = player
    self.current_scene = None

  def play(self):

    continue_playing = True
    self.current_scene = self.scenes["scene1"]
    while continue_playing:
      os.system('clear')
      # Display story text and options
      self.current_scene.display_text()

      # Display selection text
      print("\n\nWatch out what you choose.  You may reget it...here are your options.")

      # Retrieve user input
      self.current_scene.display_options("normal")
      option_key = input("\nSelection: ")

      # Select new scene
      result = self.use_option(option_key)

      if isinstance(result, Scene):
        self.current_scene = result

  def use_option(self, option):
    if option == "exit":
      sys.exit()

    if option == "inventory":
      self.player.display_inventory()
      utils.any_key_input()
      return

    if option == "search":
      self.player.search_scene(self.current_scene)
      utils.any_key_input()
      return

    return self.scenes[option]

      


