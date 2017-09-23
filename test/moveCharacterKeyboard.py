
from __future__ import division, print_function, unicode_literals

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '../images'))

import yaml

import cocos
from cocos.director import director

import pyglet
from pyglet.window import key

import loadSpritesheetAsAnimation


import esper


FPS = 60
WIDTH = 720
HEIGHT = 480


class CharacterNode(cocos.cocosnode.CocosNode):

    """Character (dict_yml, tag_action, x, y, sprite_img) : A layer drawing a character at (x,y) of
    given sprite, with number of actions defined by tag"""

    def __init__(self, dict_yml, x, y):
        super(CharacterNode, self).__init__()

        self._dict_yml = dict_yml
        self.name = "Hero"

        spritesheet_img = pyglet.image.load('../images/' + dict_yml['image'])
        self.animations = dict()
        for action in self._dict_yml['actions'].keys():
            self.animations[action] = loadSpritesheetAsAnimation.load_animation(dict_yml['actions'][action], spritesheet_img)

        self.sprite = pyglet.sprite.Sprite(
            img=self.animations['walk_down'], x=self.x, y=self.y)

    def draw(self):
        super(CharacterNode, self).draw()
        self.sprite.draw()

    def step(self, dt):
        super(CharacterNode, self).step(dt)
        if keyboard[key.UP]:
            self.sprite.img = self.animations['walk_up']
        elif keyboard[key.DOWN]:
            self.sprite.img = self.animations['walk_down']
        elif keyboard[key.LEFT]:
            self.sprite.img = self.animations['walk_left']
        elif keyboard[key.RIGHT]:
            self.sprite.img = self.animations['walk_right']

def main_cocos_only(file_yml):

    global keyboard # from test_tiles.py of cocos2d
    dict_yml = loadSpritesheetAsAnimation.load_yml(file_yml)

    spritesheet_img = pyglet.image.load('../images/' + dict_yml['image'])

    #director.init(width = spritesheet_img.width, height = spritesheet_img.height, resizable = True)
    director.init(width=WIDTH, height=HEIGHT, resizable=True)
    main_scene = cocos.scene.Scene()

    # Create layer with spritesheet
    layer = cocos.layer.Layer()
    main_scene.add(layer)

    # Create nodes and append them to sprite layer
    #create_boxes(sprite_layer, dict_yml)

    # Create layer with box and labels
    #create_layer_box(main_scene, dict_yml)

    # Test animation
    #dict_noimg = dict_yml['actions']
    # since dict is not sorted, sort alphabetically before plotting
    #keys = sorted(list(dict_noimg.keys()))
    #for i, k in enumerate(keys):
    #    row = i // 7
    #    col = i - row * 7

    #    print('row ', row, ' col ', col, ' k ', k)
    #    anim = loadSpritesheetAsAnimation.AnimationNode(dict_yml['actions'], k, col * 64, row * 64, spritesheet_img)
    #    layer.add(anim)

    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)


    character = CharacterNode(dict_yml, 20, 20)


    #character_sprite = cocos.sprite.Sprite()
    layer.add(character)

    director.run(main_scene)



##################################
#  Define some Components:
##################################
class Velocity:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Renderable:
    def __init__(self, sprite):
        self.sprite = sprite
        self.w = sprite.width
        self.h = sprite.height

class SpriteSheetAnimation:
    def __init__(self, dict_yml):
        self._dict_yml = dict_yml

        spritesheet_img = pyglet.image.load('../images/' + dict_yml['image'])
        self.animations = {}
        for action in self._dict_yml['actions'].keys():
            self.animations[action] = loadSpritesheetAsAnimation.load_animation(dict_yml['actions'][action], spritesheet_img)

        

################################
#  Define some Processors:
################################
class MovementProcessor(esper.Processor):
    def __init__(self, minx, maxx, miny, maxy):
        super().__init__()
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self, dt):
        # This will iterate over every Entity that has BOTH of these components:
        for ent, (vel, rend) in self.world.get_components(Velocity, Renderable):
            # Update the Renderable Component's position by it's Velocity:
            # An example of keeping the sprite inside screen boundaries. Basically,
            # adjust the position back inside screen boundaries if it is outside:
            new_x = max(self.minx, rend.sprite.x + vel.x)
            new_y = max(self.miny, rend.sprite.y + vel.y)
            new_x = min(self.maxx - rend.w, new_x)
            new_y = min(self.maxy - rend.h, new_y)
            rend.sprite.position = new_x, new_y


class PlayerKeyProcessor(esper.Processor):
    def __init__(self,keyboard):
        super().__init__()
        self.keyboard = keyboard
        # Key pressed in previous iteration
        self.up = False
        self.down = False
        self.left = False
        self.right = False


    def process(self, dt):
        # This will iterate over every Entity that has BOTH of these components:
        for ent, (vel, rend, sprit) in self.world.get_components(Velocity, Renderable, SpriteSheetAnimation):
            # Trick to restart the animation
            rend.sprite.image.frames[0].duration = rend.sprite.image.frames[1].duration
            # Choose correct animation
            if self.keyboard[key.UP] and not self.up:
                rend.sprite.image = sprit.animations['walk_up']
                self.up = True
            elif self.keyboard[key.DOWN] and not self.down:
                rend.sprite.image = sprit.animations['walk_down']
                self.down = True
            elif self.keyboard[key.LEFT] and not self.left:
                rend.sprite.image = sprit.animations['walk_left']
                self.Left = True
            elif self.keyboard[key.RIGHT] and not self.right:
                rend.sprite.image = sprit.animations['walk_right']
                self.right = True
            
            self.up = self.keyboard[key.UP]
            self.down = self.keyboard[key.DOWN]
            self.left = self.keyboard[key.LEFT]
            self.right = self.keyboard[key.RIGHT]

            # Stop animation if no key pressed (e.g., by pausing one of the frame)
            if not(self.up or self.down or self.left or self.right):
                rend.sprite.image.frames[0].duration = None
            else:
                rend.sprite.image.frames[0].duration = rend.sprite.image.frames[1].duration


def main(file_yml):

    global keyboard # from test_tiles.py of cocos2d
    dict_yml = loadSpritesheetAsAnimation.load_yml(file_yml)

    spritesheet_img = pyglet.image.load('../images/' + dict_yml['image'])

    #director.init(width = spritesheet_img.width, height = spritesheet_img.height, resizable = True)
    director.init(width=WIDTH, height=HEIGHT, resizable=True)
    main_scene = cocos.scene.Scene()

    # Create layer with spritesheet
    layer = cocos.layer.Layer()
    main_scene.add(layer)

    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    # Initialize Esper world, and create a "player" Entity with a few Components:
    world = esper.World()
    player = world.create_entity()
    world.add_component(player, Velocity(x=0, y=0))
    player_animation = SpriteSheetAnimation(dict_yml)
    world.add_component(player, player_animation)
    player_sprite = cocos.sprite.Sprite(player_animation.animations['walk_down'],(WIDTH//2, HEIGHT//2))
    world.add_component(player, Renderable(sprite=player_sprite))

    # Create some Processor instances, and asign them to the World to be processed:
    movement_processor = MovementProcessor(minx=0, miny=0, maxx=WIDTH, maxy=HEIGHT)
    player_key_processor = PlayerKeyProcessor(keyboard)
    world.add_processor(player_key_processor)
    world.add_processor(movement_processor)


    layer.add(player_sprite)

    pyglet.clock.schedule_interval(world.process, interval=1.0/FPS)
    director.run(main_scene)




if __name__ == "__main__":
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    file_yml = 'spritesheet_test.yml' if len(sys.argv) < 2 else sys.argv[1]
    main(file_yml)
