# -*- coding: utf-8 -*-
"""
Load spritesheet for character and yml file containing box with position of sprites
"""

from __future__ import division, print_function, unicode_literals

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import gl

#import cocos


window = pyglet.window.Window()

@window.event
def on_draw():
    pass


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', [x, y, x-dx, y, x-dx, y-dy, x, y-dy]))
    print( x, y, dx, y, dx, dy, x, dy)
pyglet.app.run()
