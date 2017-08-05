# -*- coding: utf-8 -*-
"""
Load spritesheet for character and yml file containing box with position of sprites
"""


from __future__ import division, print_function, unicode_literals

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '../images'))

import yaml

import cocos
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite

import pyglet
from pyglet import gl

# See cocos2d samples/multiple_layers.py
class Square(cocos.layer.Layer):

    """Square (color, c, y, size=50) : A layer drawing a square at (x,y) of
    given color and size"""

    def __init__(self, color, x, y, size=50):
        super(Square, self).__init__()

        self.x = x
        self.y = y
        self.size = size
        self.layer_color = color

    def draw(self):
        super(Square, self).draw()

        gl.glColor4f(*self.layer_color)
        x, y = self.x, self.y
        w = x + self.size
        h = y + self.size
        gl.glBegin(gl.GL_QUADS)
        gl.glVertex2f(x, y)
        gl.glVertex2f(x, h)
        gl.glVertex2f(w, h)
        gl.glVertex2f(w, y)
        gl.glEnd()
        gl.glColor4f(1, 1, 1, 1)


def plot_box(bottom_left_x, bottom_left_y, width, height):
    COLOR_BOX = (0, 0, 255)
    gl.glColor3ub(*COLOR_BOX)
    gl.glBegin(gl.GL_LINE_STRIP)
    top_right_x = bottom_left_x + width
    top_right_y = bottom_left_y + height
    vertexes = [(bottom_left_x, bottom_left_y), (bottom_left_x, top_right_y), (top_right_x, top_right_y), (top_right_x, bottom_left_y)]
    for v in vertexes:
        gl.glVertex2f(*v)
    gl.glVertex2f(*vertexes[0])
    gl.glEnd()
    #label = pyglet.text.Label('Hello, world',
    #                      font_name='Times New Roman',
    #                      font_size=36,
    #                      x= top_right_x, y= top_right_y,
    #                      anchor_x='center', anchor_y='center')
    #label.draw()

def plot_box_label_yml(yml_dict, img_w, img_h):
    for key, value in yml_dict.items():
        # the key will print a label
        print(key)
        i = 0
        for coord in value:
            if len(coord) is 4:
                top_left_x_img, top_left_y_img, width, height = coord # Image coordinates
                # Plot (change coord for openGL), (0,0 is bottom left corner)
                top_left_x = top_left_x_img
                top_left_y = img_h - top_left_y_img
                bottom_left_x = top_left_x
                bottom_left_y = top_left_y - height
                
                plot_box(bottom_left_x = bottom_left_x, bottom_left_y = bottom_left_y, width = width, height = height)
                label = pyglet.text.Label(key + '_' + str(i) ,
                                          font_name= 'Times New Roman',
                                          font_size= 8,
                                          x = top_left_x, y = top_left_y + 2,
                                          anchor_x='left', anchor_y='bottom')
                label.draw()

                gl.glColor4f(*(1, 0, 1, 0.2))
                x, y = bottom_left_x, bottom_left_y
                w = x + width
                h = y + height
                gl.glBegin(gl.GL_QUADS)
                gl.glVertex2f(x, y)
                gl.glVertex2f(x, h)
                gl.glVertex2f(w, h)
                gl.glVertex2f(w, y)
                gl.glEnd()
                gl.glColor4f(1, 1, 1, 1)
            i = i + 1


class BoxesNode(cocos.cocosnode.CocosNode):

    """Boxes (color, c, y, size=50) : A layer drawing a square at (x,y) of
    given color and size"""

    def __init__(self, yml_dict, img_w, img_h):
        super(BoxesNode, self).__init__()

        self.x = 0
        self.y = 0
        self.yml_dict = yml_dict
        self.img_w = img_w
        self.img_h = img_h


    def draw(self):
        super(BoxesNode, self).draw()
        #print('X Y ', self.x, ' ', self.y)
        plot_box_label_yml(self.yml_dict, self.img_w, self.img_h)
        
class SquareNode(cocos.cocosnode.CocosNode):

    """Square (color, c, y, size=50) : A layer drawing a square at (x,y) of
    given color and size"""

    def __init__(self, color, x, y, size=50):
        super(SquareNode, self).__init__()

        self.x = x
        self.y = y
        self.size = size
        self.layer_color = color

    def draw(self):
        super(SquareNode, self).draw()

        gl.glColor4f(*self.layer_color)
        x, y = self.x, self.y
        w = x + self.size
        h = y + self.size
        gl.glBegin(gl.GL_QUADS)
        gl.glVertex2f(x, y)
        gl.glVertex2f(x, h)
        gl.glVertex2f(w, h)
        gl.glVertex2f(w, y)
        gl.glEnd()
        gl.glColor4f(1, 1, 1, 1)

class SpriteLayer(Layer):
    
    def __init__(self, spritesheet_img):
        super(SpriteLayer, self).__init__()
        self.image = spritesheet_img
        # Layer is positioned in (0,0)
        self.x = 0 #self.image.width //2
        self.y = 0 #self.image.height //2

    def draw(self):
        super(SpriteLayer, self).draw()
        # If position = (0, 0) sprite is centered in layer center. Give it an offset then
        sprite = Sprite(self.image, position = (self.image.width // 2, self.image.height // 2))
        self.add(sprite)


# Load YML
def load_yml(path):
    with open(path) as file:
        mystr = file.read()
        mydict = yaml.load(mystr)
        return mydict
    return []

def create_layer_box(scene, dict_yml):
    scene.add(Square(color = (1, 0, 0, 0.2), x = 50, y = 50))

def create_boxes(sprite_layer, dict_yml):
    #sprite_layer.add(SquareNode(color = (1, 1, 0, 0.2), x = 0, y = 0))
    #sprite_layer.add(SquareNode(color = (1, 0, 1, 0.2), x = 10, y = 10))
    box = BoxesNode(dict_yml, sprite_layer.image.width, sprite_layer.image.height)
    sprite_layer.add(box)

def main():

    dict_yml = load_yml('spritesheet_example.yml')


    spritesheet_img = pyglet.image.load('../images/' + dict_yml['image'])

    director.init(width = spritesheet_img.width, height = spritesheet_img.height, resizable = True)
    main_scene = cocos.scene.Scene()

    # Create layer with spritesheet
    sprite_layer = SpriteLayer(spritesheet_img)
    main_scene.add(sprite_layer)

    # Create nodes and append them to sprite layer
    create_boxes(sprite_layer, dict_yml)

    # Create layer with box and labels
    #create_layer_box(main_scene, dict_yml)
    
    director.run(main_scene)



if __name__ == "__main__":
    main()