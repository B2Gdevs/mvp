import utils
from scene import Scene
from TextEngine import TextEngine
from player import Player

data = utils.load_file("story.json")

scenes = {} # Retrieve scense for story
for scene in data["scenes"]:
  scenes[scene["name"]] = Scene(scene["name"], scene["options"], 
                                scene["scene_text"], scene["items"])

player = data["player"]
player = Player(player["name"], 
                player["health"],
                player["inventory"],)

engine = TextEngine(scenes, player)

engine.play()












