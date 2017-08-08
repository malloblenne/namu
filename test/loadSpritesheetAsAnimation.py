
from __future__ import division, print_function, unicode_literals

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '../images'))

import yaml

import cocos
from cocos.director import director

import pyglet


def load_animation(list_coord, sprite_img):
    regions = []
    for coords in list_coord:
        x, top_y_img, width, height = coords
        bottom_y = sprite_img.height - top_y_img - height
        image_part = sprite_img.get_region(
            x=x, y=bottom_y, width=width, height=height)
        regions.append(image_part)
        # create an animation from the list of selected regions
    animation = pyglet.image.Animation.from_image_sequence(
        sequence=regions, period=0.1, loop=True)
    return animation


#batch = pyglet.graphics.Batch()

class AnimationNode(cocos.cocosnode.CocosNode):

    """Boxes (color, c, y, size=50) : A layer drawing a square at (x,y) of
    given color and size"""

    def __init__(self, dict_yml, tag_action, x, y, sprite_img):
        super(AnimationNode, self).__init__()

        self.x = x
        self.y = y
        self._dict_yml = dict_yml
        self.name = tag_action
        self.animation = load_animation(dict_yml[tag_action], sprite_img)
        self.sprite = pyglet.sprite.Sprite(
            img=self.animation, x=self.x, y=self.y)

    def draw(self):
        super(AnimationNode, self).draw()
        self.sprite.draw()

# Load YML


def load_yml(path):
    with open(path) as file:
        mystr = file.read()
        mydict = yaml.load(mystr)
        return mydict
    return []


def main(file_yml):

    dict_yml = load_yml(file_yml)

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
    dict_noimg = dict_yml['actions']
    # since dict is not sorted, sort alphabetically before plotting
    keys = sorted(list(dict_noimg.keys()))
    for i, k in enumerate(keys):
        row = i // 7
        col = i - row * 7

        print('row ', row, ' col ', col, ' k ', k)
        anim = AnimationNode(dict_yml['actions'], k, col * 64, row * 64, spritesheet_img)
        layer.add(anim)

    director.run(main_scene)


if __name__ == "__main__":
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    file_yml = 'spritesheet_test.yml' if len(sys.argv) < 2 else sys.argv[1]
    main(file_yml)
