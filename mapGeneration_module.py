import colours


_mapInfo = {
    'mountain': {
        'icon': '^',
        'isWalkable': False,
        'elevation': 3,
        'description': "This is a mountain",
        'colour': "LIGHT_GRAY"
    },
    'forest': {
        'icon': '#',
        'isWalkable': True,
        'elevation': 1,
        'description': "This is a forest",
        'colour': "GREEN"
    },
    'plain': {
        'icon': '.',
        'isWalkable': True,
        'elevation': 1,
        'description': "This is a plain",
        'colour': "GREEN"
    },
    'water': {
        'icon': '~',
        'isWalkable': False,
        'elevation': 0,
        'description': "This is water",
        'colour': "BLUE"
    },
    'road': {
        'icon': '-',
        'isWalkable': True,
        'elevation': 1,
        'description': "This is a road",
        'colour': "WHITE"
    },
    'gate': {
        'icon': '▓',
        'isWalkable': True,
        'elevation': 2,
        'description': "This is a gate",
        'colour': "WHITE"
    },
    'walls': {
        'icon': '█',
        'isWalkable': False,
        'elevation': 2,
        'description': "This is a wall",
        'colour': "BLACK",
        'bg_colour': 'WHITE_BG'
    }
}

def get_map_info():
    return _mapInfo

def get_map_Icon(tile):
    return _mapInfo[tile]['icon']

def get_icon_colour(tile):
    return colours.colours_dict[_mapInfo[tile]['colour']]

def get_Map_Descriptions(tile):
    return _mapInfo[tile]['description']

def get_walkable(tile):
    return _mapInfo[tile]['isWalkable']

def get_bg_colour(tile):
    try:
        return colours.colours_bg_dict[_mapInfo[tile]['bg_colour']]
    except:
        return colours.DEFAULT