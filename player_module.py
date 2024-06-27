import character_module

class Player(character_module.Character):
    def __init__(self, name, x = 5, y = 5, health =10, damage =1, defense =0, speed =10, luck =5, gold =0
                 ,inventory ={}, skills ={}, level =0, experience =0, max_health =100, max_damage =100
                 ,max_defense =100, max_speed =100, max_luck =90, max_gold =100):
        super().__init__(name, 'hero', x, y, gold, inventory, health, damage, defense)
        self.speed = speed
        self.luck = luck
        self.skills = skills
        self.level = level
        self.experience = experience
        self.max_health = max_health
        self.max_damage = max_damage
        self.max_defense = max_defense
        self.max_speed = max_speed
        self.max_luck = max_luck
        self.max_gold = max_gold
    
    def __dict__(self):
        return {
            'x': self.x,
            'y': self.y,
            'name': self.name,
            'health': self.health,
            'damage': self.damage,
            'defense': self.defense,
            'speed': self.speed,
            'luck': self.luck,
            'gold': self.gold,
            'inventory': self.inventory,
            'skills': self.skills,
            'level': self.level,
            'experience': self.experience,
            'max_health': self.max_health,
            'max_damage': self.max_damage,
            'max_defense': self.max_defense,
            'max_speed': self.max_speed,
            'max_luck': self.max_luck,
            'max_gold': self.max_gold
        }