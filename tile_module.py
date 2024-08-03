import colours
from mapGeneration_module import get_map_Icon, get_Map_Descriptions, get_icon_colour, get_Map_Descriptions, get_walkable
from NPCGeneration_module import get_NPC_Icon, get_NPC_description, get_NPC_colour
from enemy_module import getEnemyLocations, getEnemyNames

class Tile():
    def __init__(self, x, y, tileName, isTransparent = False, isBlocking = False, isDoor = False, doorDirection = -1,
                 isStair = False, stairDirection = -1, isExit = False, exitDirection = -1, isItem = False, itemID = -1,
                 isNPC = False, nPCID = -1, isEvent = False, eventID = -1, isTrigger = False, triggerID = -1):
        self.x = x
        self.y = y
        self.tileName = tileName
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
        self.nPCID = nPCID
        self.isEvent = isEvent
        self.eventID = eventID
        self.isTrigger = isTrigger
        self.triggerID = triggerID
        self.NPCName = self.checkName()
        self.isEvent = self.checkEvent()
        self.isWalkable = get_walkable(self.tileName)
        if self.isEvent and self.NPCName != '-1' and self.isWalkable:
            self.tileType = get_NPC_Icon(self.NPCName)
            self.tileDescription = get_NPC_description(self.NPCName)
            self.tileColour = get_NPC_colour(self.NPCName)
        else:
            self.tileType = get_map_Icon(self.tileName)
            self.tileDescription = get_Map_Descriptions(self.tileName)
            self.tileColour = get_icon_colour(self.tileName)

    def update_tile(self):
        self.isWalkable = get_walkable(self.tileName)
        if self.isEvent and self.NPCName != '-1' and self.isWalkable:
            self.tileType = get_NPC_Icon(self.NPCName)
            self.tileDescription = get_NPC_description(self.NPCName)
            self.tileColour = get_NPC_colour(self.NPCName)
        else:
            self.tileType = get_map_Icon(self.tileName)
            self.tileDescription = get_Map_Descriptions(self.tileName)
            self.tileColour = get_icon_colour(self.tileName)

    def checkName(self):
        selfPosition = [self.x, self.y]
        enemyPosition = getEnemyLocations()
        enemyName = getEnemyNames()
        for i in range(len(enemyPosition)):
            if selfPosition == enemyPosition[i]:
                return enemyName[i]
        return '-1'
    
    def setEvent_flag(self, event):
        self.isEvent = event
        self.update_tile()

    def checkEvent(self):
        selfPosition = [self.x, self.y]
        enemyPosition = getEnemyLocations()
        for i in enemyPosition:
            if i == selfPosition:
                return True
        return False

        if self.isDoor or self.isStair or self.isExit:
            return True

    def getEvent(self):
        return self.isEvent

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
            'nPCID': self.nPCID,
            'isEvent': self.isEvent,
            'eventID': self.eventID,
            'isTrigger': self.isTrigger,
            'triggerID': self.triggerID
            }