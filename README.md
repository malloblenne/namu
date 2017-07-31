# Namu - 나무

This game is a beat'em up videogame inspired by diablo and with a fantasy setting (a bit like Ultima Online).
The main aim is to play around with python and the entity system component framework.

## Graphics

The graphics, sprite etc are coming from the [Liberated Pixel Cup](http://lpc.opengameart.org/lpc-blog) or compatible to those


## Idea

For simplicity, the game is single player.
There are multiple maps saved in tmx.
The map is isometric (like Ultima Online).
The user starts in a city, then moves out in woods.
In the map, embedded in tmx, there are spawn points. Monsters/enemies can be spawned.
Gates of the city, opening of caverns etc define the transitions between one tmx map and the other.
The character and enemies are defined by yml file.
In the file there are info such as name, items, drop for monsters, gold, and skills (such as move, attack melee, attack distance,...). The skills can be loaded by the entity system component, so it is easy to add new ones.
In the enemy file there is a field spritesheet with the name of another yml file defining the spritesheet.
That yml file contains the position of each frame of the different animations (e.g., walk north, run east...). In this way the same spritesheet might be reusable for different monsters (e.g., simple a chief).
Moreover, it will be easy to add a new enemy, connect it to a existing or new spritesheet and add property to it.
The damage system can be inspired by Dungeon & Dragons 3rd edition, simulating dice rolls.

## Libraries

- [pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home)
- [esper](https://github.com/benmoran56/esper)
- [cocos2d] (http://python.cocos2d.org/)
- [Tiled](http://www.mapeditor.org/)
- [pyYAML](http://pyyaml.org/)

## Resources

- [Liberated Pixel Cup](http://lpc.opengameart.org/lpc-blog)
- [Open Game Library](https://opengameart.org/)
