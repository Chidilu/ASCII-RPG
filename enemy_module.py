import random, json, os

enemyLocations = [[7, 7], [8, 8]]
enemyName = ["goblin", "orc"]

def setEnemyLocations(mapSize):
    global enemyLocations, enemyName
    names = ["goblin", "orc"]
    x1, y1 = mapSize
    for i in range(32):
        name = random.choice(names)
        x = random.randint(10, x1)
        y = random.randint(10, y1)
        if([x, y] in enemyLocations):
            i -= 1
            continue
        enemyLocations.append([x, y])
        enemyName.append(name)
    save()

def getEnemyLocations():
    return enemyLocations

def getEnemyNames():
    return enemyName

def removeEnemyLocation(location):
    global enemyLocations
    enemyLocations = [loc for loc in enemyLocations if loc != location]

def save():
    saveLoc = 'saves/enemy/enemyLocList.json'
    saveName = 'saves/enemy/enemyNameList.json'
    with open(saveLoc, 'w') as f:
        f.write(json.dumps(enemyLocations))
    with open(saveName, 'w') as f:
        f.write(json.dumps(enemyName))