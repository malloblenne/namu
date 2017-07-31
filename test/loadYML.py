# -*- coding: utf-8 -*-
"""
Test load a dump functionality of yaml module
"""
from __future__ import division, print_function, unicode_literals

import yaml

with open('example.yml') as file:
    mystr = file.read()
    mydict = yaml.load(mystr)
    print(mydict)
    print(mydict['name'])
    
    # Modify yml
    mydict['skills'].append('roar')
    newstr = yaml.dump(mydict)
    with open('example_add.yml','w') as writer:
        writer.write(newstr)
    
