from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

	def enter(self):
		print("This scene is not yet configured.")
		print("Subclass it and implement enter().")
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		# be sure to print out the last scene
		current_scene.enter()
		
class Death(Scene):

	quips = [
		"You died. You kinda suck at this.", 
		"Your Mom would be proud...if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this.",
		"You're worse than your Dad's jokes."
		
	]
	
	def enter(self):
		print(Death.quips[randint(0, len(self.quips)-1)])
		exit(1)
		
class BlueStoneForest(Scene):

	def enter(self):
		print(dedent("""
			You entered the magical blue stone forest. Your mission is to find the radiant gemstone from mystic realms and save your sylvan vale from zogtrons. Here, you have to meet the sorcerer and get a magic bomb from him to defeat the zogtrons if you answer the sorcerer's puzzle. If you do not answer, the sorcerer will kill you.
		"""))
		
		action = input("> ")
		
		if action == "blink!":
			print(dedent("""
				Sorcerer asks the puzzle; you don't know the answer to the puzzle. So you blink at it. Then the sorcerer comes near you, and he eats you.
				"""))
			return 'death'
			
		elif action == "solved":
			print(dedent("""
				You answered the sorcerer's puzzle, got a magic bomb from him, and moved towards mystic realms.
				"""))
			return 'mystic_realms'
			
		else:
			print("DOES NOT COMPUTE!")
			return 'blue_stone_forest'
			
class MysticRealms(Scene):

	def enter(self):
		print(dedent("""
			You enter the mystic realms. Here, you have to get the radiant gemstone from the big Dordan tree in this forest. There's a keypad lock on the Dordan tree, and you put the correct pin in it to get the radiant gemstone out. The pin has four digits. You have only three chances to open the lock.
			"""))
		
		code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}"
		guess = input("[keypad]> ")
		guesses = 0
		
		while guess != code and guesses < 3:
			print("BUZZED!")
			guesses += 1
			guess = input("[keypad]> ")
			
		if guess == code:
			print(dedent("""
				The keypad lock opens, and you can grab the radiant gemstone. Now you can escape from this place.
				"""))
			return 'sylvan_vale'
		else:
			print(dedent("""
				If you are not finding correct code upto 3 chances. Then you will die here.
				"""))
			return 'death'
			
class SylvanVale(Scene):

	def enter(self):
		print(dedent("""
			You rush to Sylvan Vale and face the Zogtrons. You have to throw the magic bomb in front of the zogtrons; this will kill only the Zogtrons, and it doesn't affect you. After that, place the radiant gemstone at the top of the palace.
			"""))
		
		if action == "booommm!":
			print(dedent("""
				Zogtrons comes near you and asks about the radiant gemstone from you. If they capture a radiant gemstone from you, then they will permanently stay in your Sylvan Vale. Then you will die.
				"""))
			return 'death'
		else:
			print(dedent(f"""
				You throw the magic bomb in front of the zogtrons, and then all of them die. and you are placed a radiant gemstone at the top of your sylvan vale palace. You won!
				"""))
			return 'finished'
			
class Finished(Scene):

	def enter(self):
		print("You won! Good job.")
		return 'finished'
		
class Map(object):

	scenes = {
		'blue_stone_forest': BlueStoneForest(),
		'mystic_realms': MysticRealms(),
		'sylvan_vale': SylvanVale(),
		'death': Death(),
		'finished': Finished(),
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
a_map = Map('blue_stone_forest')
a_game = Engine(a_map)
a_game.play()
		
