# 1. Write or draw about the problem.
# 2. Extract key concepts from 1 and research them.
# 3. Create a class hierarchy and object map for the concepts.
# 4. Code the classes and a test to run them.
# 5. Repeat and refine.

# 1. Write or draw about the problem.

# "In a magical forest, our hero has to solve a sorcerer's puzzle to get a magic bomb and
# retrieve a radiant gemstone to save Sylvan Vale from Zogtrons. Our hero has to go through
# different parts of the forest, face challenges, and take risks along the way. The game
# is a text-based adventure full of different forest parts/ rooms with text outputs and 
# funny ways to die. The game will involve an engine that runs a map full of rooms or
# scenes. Each forest part will prints its own description when the hero enters it and then
# tell the engine what room to run next out of the map."

# 2. Extract key concepts from 1 and research them.

# Hero
# Zogtrons
# Radiant gemstone
# blue stone forest
# Mystic Realms
# Map
# Death
# Scene

# 3. Create a class hierarchy and object map for the concepts.

# Map
# - next_scene
# - opening_scene
# Engine
# - play
# Scene
# - enter
# - Death
# - Blue Stone Forest
# - Mystic Realms
# - Sylvan Vale

# 4. Code the classes and a test to run them.

class Scene(object):

	def enter(self):
		pass
		
class Engine(object):
	
	def __init__(self, scene_map):
		pass
		
	def play(self):
		pass
		
class Death(Scene):

	def enter(self):
		pass
		
class BlueStoneForest(Scene):

	def enter(self):
		pass
		
class MysticRealms(Scene):

	def enter(self):
		pass
		
class SylvanVale(Scene):

	def enter(self):
		pass
		
class Map(object):

	def __init__(self, start_scene):
		pass
		
	def next_scene(self, scene_name):
		pass
		
	def opening_scene(self):
		pass
		
a_map = Map('blue_stone_forest')
a_game = Engine(a_map)
a_game.play()

