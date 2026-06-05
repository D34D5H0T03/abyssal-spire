from abc import ABC, abstractclassmethod
from util import *

class Entity(ABC):
    def __init__(self, name, max_hp, attack_power, defence):
        super().__init__()
        self._name = name
        self._max_hp = max_hp
        self._attack_power = attack_power
        self._defence = defence
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def max_hp(self):
        return self._max_hp
    
    @max_hp.setter
    def max_hp(self, value):
        self._max_hp = value
    
    @property
    def attack_power(self):
        return self._attack_power
    
    @attack_power.setter
    def attack_power(self, value):
        self._attack_power = value
    
    @property
    def defence(self):
        return self._defence
    
    @defence.setter
    def defence(self, value):
        self._defence = value
        

class Player(Entity):
    
    def __init__(self, name, max_hp, attack_power, defence, hp, stats, archetype):
        super().__init__(name, max_hp, attack_power, defence)
        self._hp = hp
        self._stats = stats
        self._archetype = archetype
        
    @classmethod
    def create_knight(cls, name):
        
        knight_stats = Stat(strength = 16, speed = 10, constitution = 15, luck = 8)
        
        return cls(
            name = name,
            max_hp = 150,
            attack_power = 15,
            defence = 10,
            hp = 150,
            stats = knight_stats,
            archetype = "knight"
        )
        
    @classmethod
    def create_rogue(cls, name):
        
        rogue_stats = Stat(strength = 10, speed = 16, constitution = 10, luck = 14)
        
        return cls(
            name = name,
            max_hp = 150,
            attack_power = 15,
            defence = 10,
            hp = 150,
            stats = rogue_stats,
            archetype = "Rogue"
        )
    