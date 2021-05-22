class Scene:
  def __init__(self, name, options, scene_text, items=[]):
    self.name = name
    self.options = self.build_options(options)
    self.scene_text = scene_text
    self.items = items

  def display_text(self):
    print(self.scene_text)

  def display_options(self, format_type):

    if format_type.lower() == "normal":
      self.print_normal_options()

  def print_normal_options(self):
    for idx, option_text in enumerate(self.options):
      print(f"{idx + 1}: {option_text}")

  def build_options(self, options):
    options.append("exit")
    options.append("inventory")
    options.append("search")
    return options
