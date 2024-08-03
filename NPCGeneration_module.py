import colours

_npcInfo = {
    "mayor": {
        "name": "Mayor",
        "description": "The mayor of the town, he is a very nice man and is always willing to help out the town.",
        "icon": "M",
        "colour": 'WHITE'
        },
    "blacksmith": {
        "name": "Blacksmith",
        "description": "The blacksmith of the town, he creates and maintains the tools of the town.",
        "icon": "B",
        "colour": 'WHITE'
        },
    "goblin": {
        "name": "Goblin",
        "description": "A goblin that has jumped you to steal your loot.",
        "icon": "G",
        "colour": 'RED'
        },
    "orc": {
        "name": "Orc",
        "description": "A strong and fierce orc that will attack you on sight.",
        "icon": "O",
        "colour": 'GREEN'
        }
}




def get_NPC_Icon(npcID):
    return _npcInfo[npcID]["icon"]

def get_NPC_description(npcID):
    return _npcInfo[npcID]["description"]

def get_NPC_colour(npcID):
    return colours.colours_dict[_npcInfo[npcID]['colour']]

def get_agressive(npcID):
    return _npcInfo[npcID]["aggressive"]