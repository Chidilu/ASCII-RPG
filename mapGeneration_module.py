import colours


_mapInfo = {
    'mountain': {
        'icon': '^',
        'elevation': 3,
        'description': "This is a mountain",
        'colour': "LIGHT_GRAY"
    },
    'forest': {
        'icon': '#',
        'elevation': 1,
        'description': "This is a forest",
        'colour': "GREEN"
    },
    'plain': {
        'icon': '.',
        'elevation': 1,
        'description': "This is a plain",
        'colour': "GREEN"
    },
    'water': {
        'icon': '~',
        'elevation': 0,
        'description': "This is water",
        'colour': "BLUE"
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

def generate_World(tile):
    if tile.x == 1 and tile.y == 1:
        return 'mountain'
    return tile.tileName