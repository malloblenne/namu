# -*- coding: utf-8 -*-
"""
Load spritesheet for character and yml file containing box with position of sprites
"""


from __future__ import division, print_function, unicode_literals

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '../images'))


import cocos
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite

import pyglet
from pyglet import gl

spritesheet_img = pyglet.image.load('../images/spritesheet.png')

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

class SpriteLayer(Layer):
    
    def __init__(self):
        super(SpriteLayer, self).__init__()
        self.image = spritesheet_img
        self.x = self.image.width //2
        self.y = self.image.height //2
        #sprite = pyglet.sprite.Sprite(img)
        #self.image = pyglet.resource.image('spritesheet.png')

    def draw(self):
        super(SpriteLayer, self).draw()
        sprite = Sprite(self.image)
        self.add(sprite)



def main():
    sw = spritesheet_img.width#832
    sh = spritesheet_img.height#1344

    director.init(width=sw, height=sh, resizable=True)
    main_scene = cocos.scene.Scene()
    main_scene.add(SpriteLayer())

    main_scene.add(Square(color = (1, 0, 0, 0.2), x = 50, y = 50))
    director.run(main_scene)



if __name__ == "__main__":
    main()