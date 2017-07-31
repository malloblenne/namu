#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
#from pyglet.gl import *
from pyglet.window import key

import esper


FPS = 60
RESOLUTION = 720, 480
BGCOLOR = (0, 0, 0, 255)

def main():
    # Initialize the main window stuff
    window = pyglet.window.Window(width=RESOLUTION[0], height=RESOLUTION[1])
    window.set_caption("The game")
    pyglet.gl.glClearColor(*BGCOLOR)
    # pyglet graphics batch for efficient rendering
    renderbatch = pyglet.graphics.Batch()

    spritesheet = pyglet.image.load('../images/spritesheet.png')
    spritesheet_seq = pyglet.image.ImageGrid(spritesheet, 21, 13)
    spritesheet_tex_seq = image.TextureGrid(spritesheet_seq)


    @window.event
    def on_draw():
        # Clear the window:
        window.clear()
        # Draw the batch of Renderables:
        #renderbatch.draw()

    def update(dt):
        # A single call to world.process() will update all Processors:
        #world.process()
        pass

    pyglet.clock.schedule_interval(update, 1.0 / FPS)
    pyglet.app.run()