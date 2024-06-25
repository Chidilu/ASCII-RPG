import colours
from mapGeneration_module import get_map_Icon, get_Map_Descriptions, get_icon_colour, get_Map_Descriptions

class Tile():
    def __init__(self, x, y, tileName,
                 isWalkable = True, isTransparent = False, isBlocking = False, isDoor = False, doorDirection = -1,
                 isStair = False, stairDirection = -1, isExit = False, exitDirection = -1, isItem = False, itemID = -1,
                 isNPC = False, NPCID = -1, isEvent = False, eventID = -1, isTrigger = False, triggerID = -1):
        self.x = x
        self.y = y
        self.tileName = tileName
        self.tileType = get_map_Icon(self.tileName)
        self.tileDescription = get_Map_Descriptions(self.tileName)
        self.tileColour = get_icon_colour(self.tileName)
        self.isWalkable = isWalkable
        self.isTransparent = isTransparent
        self.isBlocking = isBlocking
        self.isDoor = isDoor
        self.doorDirection = doorDirection
        self.isStair = isStair
        self.stairDirection = stairDirection
        self.isExit = isExit
        self.exitDirection = exitDirection
        self.isItem = isItem
        self.itemID = itemID
        self.isNPC = isNPC
        self.NPCID = NPCID
        self.isEvent = isEvent
        self.eventID = eventID
        self.isTrigger = isTrigger
        self.triggerID = triggerID
        self.makeWorld()

    def makeWorld(self):
        if self.x == 1 and self.y == 1:
            self.tileName = "forest"
            self.update_tile()

    def update_tile(self):
        self.tileType = get_map_Icon(self.tileName)
        self.tileDescription = get_Map_Descriptions(self.tileName)
        self.tileColour = get_icon_colour(self.tileName)
        self.tileDescription = get_Map_Descriptions(self.tileName)

    def __dict__(self):
        return {
            'x': self.x,
            'y': self.y,
            'tileType': self.tileType,
            'tileName': self.tileName,
            'tileDescription': self.tileDescription,
            'isWalkable': self.isWalkable,
            'isTransparent': self.isTransparent,
            'isBlocking': self.isBlocking,
            'isDoor': self.isDoor,
            'doorDirection': self.doorDirection,
            'isStair': self.isStair,
            'stairDirection': self.stairDirection,
            'isExit': self.isExit,
            'exitDirection': self.exitDirection,
            'isItem': self.isItem,
            'itemID': self.itemID,
            'isNPC': self.isNPC,
            'NPCID': self.NPCID,
            'isEvent': self.isEvent,
            'eventID': self.eventID,
            'isTrigger': self.isTrigger,
            'triggerID': self.triggerID
            }