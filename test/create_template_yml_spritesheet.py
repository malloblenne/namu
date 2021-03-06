# -*- coding: utf-8 -*-
"""
Create template for spritesheet from LPC character generator. each img is 64x64
"""
#resources
# http://gaurav.munjal.us/Universal-LPC-Spritesheet-Character-Generator/
#

from __future__ import division, print_function, unicode_literals

import yaml


def main():
    WIDTH_CHAR = 64
    HEIGHT_CHAR = 64

    list_actions = ['spellcast', 'thrust', 'walk', 'slash', 'shoot']
    list_dir = ['_up', '_left', '_down', '_right']

    list_action_dir = [act + dir for act in list_actions for dir in list_dir]
    list_action_dir.append('hurt_down')

    list_img_per_action_dir = [7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 6, 6, 6, 6, 13, 13, 13, 13, 6]

    if len(list_img_per_action_dir) != len(list_action_dir):
        print('error different sizes ', len(list_img_per_action_dir), '  ', len(list_action_dir))

    dict_yml = {'image' : 'spritesheet.png'}
    dict_actions = dict()
    # animations
    for i, act in enumerate(list_action_dir):
        list_imgs = []
        for j in range(list_img_per_action_dir[i]):
            list_imgs.append([j * WIDTH_CHAR, i * HEIGHT_CHAR, WIDTH_CHAR, HEIGHT_CHAR])
        dict_actions[act] = list_imgs
    
    # static images (first of each animation e.g.)
    list_action_dir_still = [act + '_still' for act in list_action_dir]

    for i, act  in enumerate(list_action_dir_still):
        list_single = []
        list_single.append(dict_actions[list_action_dir[i]][0])
        dict_actions[act] = list_single

    # save all dict under 'action' and dump the file   
    dict_yml['actions'] = dict_actions
    str_yml = yaml.dump(dict_yml)

    with open('spritesheet_test.yml','w') as writer:
        writer.write(str_yml)





if __name__ == "__main__":
    main()
