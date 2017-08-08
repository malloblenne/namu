# -*- coding: utf-8 -*-
"""
Load spritesheet for character and yml file containing box with position of sprites
"""
#resources
# https://stackoverflow.com/questions/19428258/how-to-pan-and-zoom-properly-in-2d

from __future__ import division, print_function, unicode_literals

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import gl

#from collections import namedtuple
import yaml

#import cocos

# Define YAML
##ImageStruct = namedtuple("ImageStruct", "top_left_x, top_left_y, width, height")
walk_up = []
##walk_up.append(ImageStruct(top_left_x = 15, top_left_y = 524, width = 32, height = 48))
#walk_up.append([15, 524, 32, 48])
#walk_up.append([81, 524, 32, 48])
#walk_up.append([143, 524, 32, 48])
#all_moves = dict()
#all_moves['walk_up'] = walk_up
#str_yml = yaml.dump(all_moves)
#with open('spritesheet_example.yml','w') as writer:
#        writer.write(str_yml)

# Load YML
def load_yml(path):
    with open(path) as file:
        mystr = file.read()
        mydict = yaml.load(mystr)
        return mydict
    return []

my_yml_dict = load_yml('spritesheet_example.yml')

# Image to load
img = pyglet.image.load('../images/spritesheet.png')
sprite = pyglet.sprite.Sprite(img)

# window should refer to the loaded image
window = pyglet.window.Window(resizable = True, width = img.width, height = img.height)
COLOR_BOX = (0, 0, 255)




def plot_box(minx, maxx, miny, maxy):
    # gl is using default origin in bottom right
    gl.glColor3ub(*COLOR_BOX)
    gl.glBegin(gl.GL_LINE_STRIP)
    #vertexes = [(0.0, 0.0), (0.0, window.height//2), (window.width//2, window.height//2), (window.width//2, 0.0)]
    vertexes = [(minx, miny), (minx, maxy), (maxx, maxy), (maxx, miny)]
    for v in vertexes:
        gl.glVertex2f(*v)
    gl.glVertex2f(*vertexes[0])
    gl.glEnd()

def plot_test_box():
    gl.glColor3ub(*COLOR_BOX)
    gl.glBegin(gl.GL_LINE_STRIP)
    vertexes = [(0.0, 0.0), (0.0, window.height//2), (window.width//2, window.height//2), (window.width//2, 0.0)]
    for v in vertexes:
        gl.glVertex2f(*v)
    gl.glVertex2f(*vertexes[0])
    gl.glEnd()
    label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
    label.draw()  

def flip_origin_top_left():
    #https://stackoverflow.com/questions/30235563/opengl-change-the-origin-to-upper-left-corner
    # this flips also all the rest of the plots, e.g. labels etc
    ox = 0
    oy = 0
    width = window.width
    height = window.height
    gl.glViewport(ox, oy, width, height); # offsets
    gl.glMatrixMode(gl.GL_PROJECTION);
    gl.glLoadIdentity();
    #gl.glOrtho(0, width, 0, height, -1, 1); # origin bottom left
    gl.glOrtho(0, width, height, 0, -1, 1); # origin top left
    gl.glMatrixMode(gl.GL_MODELVIEW);
    gl.glLoadIdentity();


def plot_box_label_yml(yml_dict, scale_x, scale_y):
    for key, value in yml_dict['actions'].items():
        # the key will print a label
        print(key)
        i = 0
        for coord in value:
            if len(coord) is 4:
                top_left_x, top_left_y, width, height = coord
                # Plot (change coord for openGL)
                top_left_y = top_left_y + sprite.y
                minx = top_left_x
                maxx = top_left_x + width
                maxy = sprite.image.height - top_left_y
                miny = maxy - height
                plot_box(minx * scale_x,
                         maxx * scale_x,
                         miny * scale_y,
                         maxy * scale_y)
                label = pyglet.text.Label(key + '_' + str(i) ,
                                          font_name= 'Times New Roman',
                                          font_size= 8,
                                          x= minx * scale_x, y= (maxy + 2) * scale_y,
                                          anchor_x='left', anchor_y='bottom')
                label.draw()
            i = i + 1


@window.event
def on_draw():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    #flip_origin_top_left()
    #plot_test_box()
    sprite.scale = min(window.width / sprite.image.width, window.height / sprite.image.height)
    sprite.draw()
    plot_box_label_yml(my_yml_dict, sprite.scale_x, sprite.scale_y)


@window.event
def on_resize(width, height):
    print('The window was resized to %dx%d' % (width, height))
    
#@window.event
#def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
#    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', [x, y, x-dx, y, x-dx, y-dy, x, y-dy]))
#    print( x, y, dx, y, dx, dy, x, dy)


pyglet.app.run()
