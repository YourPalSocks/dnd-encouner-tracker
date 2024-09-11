import tkinter as tk


# Small class to store current encounter state
class EncounterStorage:
    def __init__(self):
        self.characters = [] # Displayed on left side
        self.combatants = [] # Displayed on right side
        self.cur_combat = 0

    def next_turn(self):
        if (self.cur_combat + 1 >= len(self.combatants)):
            self.cur_combat = 0
        else:
            self.cur_combat += 1
        return self.combatants[self.cur_combat]
    
    def add_character(self, char):
        self.characters.append(char)
    

def create_encounter_instance() -> EncounterStorage:
    return EncounterStorage()