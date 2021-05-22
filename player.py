class Player:
  def __init__(self, name, health, inventory):
    self.name = name
    self.health = health
    self.inventory = inventory

  def display_inventory(self):
    print("**************** INVENTORY ****************\n")

    for item in self.inventory:
      print(f"*{item}")


  def add_item_to_inventory(self, item_name):
    self.inventory.append(item_name)

  def search_scene(self, scene):
    print("\n\nYou begin searching and find...")
    
    if len(scene.items) == 0:
      print("nothing")
      return
    
    item = scene.items.pop()
    print(f"{item}!")
    
    self.add_item_to_inventory(item)


    

    