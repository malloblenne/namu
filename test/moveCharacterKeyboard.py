
from __future__ import division, print_function, unicode_literals

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '../images'))

import yaml

import cocos
from cocos.director import director

import pyglet

import loadSpritesheetAsAnimation




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



def main(file_yml):

    dict_yml = loadSpritesheetAsAnimation.load_yml(file_yml)

    spritesheet_img = pyglet.image.load('../images/' + dict_yml['image'])

    #director.init(width = spritesheet_img.width, height = spritesheet_img.height, resizable = True)
    director.init(width=800, height=600, resizable=True)
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

    character = CharacterNode(dict_yml, 20, 20)
    layer.add(character)

    director.run(main_scene)


if __name__ == "__main__":
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    file_yml = 'spritesheet_test.yml' if len(sys.argv) < 2 else sys.argv[1]
    main(file_yml)
