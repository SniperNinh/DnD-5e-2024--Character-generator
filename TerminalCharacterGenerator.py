#prompts through the terminal to make non-random character

import pyfiglet
import json
import os
import random
import math
import settings
from randomAbilityScores import randomAbilityScores
from util import *
#races
from races.dwarf import dwarf
from races.elf import elf
from races.halfling import halfling
from races.human import human
from races.dragonborn import dragonborn
from races.gnome import gnome
from races.halfElf import halfElf
from races.halfOrc import halfOrc
from races.tiefling import tiefling
#classes
from classes.barbarian import barbarian
#background
from background.acolyte import acolyte
from background.charlatan import charlatan
from background.criminal import criminal
from background.entertainer import entertainer
from background.folkHero import folkHero
from background.guildArtisan import guildArtisan
from background.hermit import hermit
from background.noble import noble
from background.outlander import outlander
from background.sage import sage
from background.sailor import sailor
from background.soldier import soldier
from background.urchin import urchin


commands = {"help" : dnd_help, "random" : create_random}


def main():
    print(pyfiglet.figlet_format("DnD  5e  C. S. G."))
    print('type "help" for list of commands')
    print('type "random" for a random chacter')
    print('type "start" to begin making a character\n')
    
    running = True
    
    while running:
        
        called = input(":")
        
        
        if called == '':
            continue
        elif called == "start":
            character_creator()
        elif called in commands:
            commands[called]()
        else:
            print(f'\nthe command {called} does not exist\ntype "help" for a full list of commands\n')
        
    


def character_creator(checkpoint = "start"):
    creating = True
    while creating:
        if checkpoint == "start":
            
            with open("data/defaults/character_sheet.json", "r") as template:
                character_sheet = json.load(template)
                template.close()
            
            checkpoint = "picking_class"
        
        if checkpoint == "picking_class":
            print("\nchoose a starting class from the following: ")
            print([json.load(open(class_file, "r"))["class_name"] for class_file in os.scandir("data/classes")]) #yeah idk mate, open each files in the classes folder and prints the "character_name" value
            picked_class = input("\n:")
            if picked_class in [json.load(open(class_file, "r"))["class_name"] for class_file in os.scandir("data/classes")]:
                character_sheet["class"] = picked_class
                
                checkpoint = "picking_race"
            
            else:
                print(f"\nthere is no {picked_class} class, you might have misstyped\n")
                continue
        
        if checkpoint == "picking_race":
            print("\nchoose a race from the following: ")
            print([json.load(open(race_file, "r"))["race_name"] for race_file in os.scandir("data/races")]) #yeah idk mate, open each files in the classes folder and prints the "character_name" value
            picked_race = input("\n:")
            if picked_race in [json.load(open(race_file, "r"))["race_name"] for race_file in os.scandir("data/races")]:
                character_sheet["race"] = picked_race
                
                checkpoint = "picking_subrace"
            
            else:
                print(f"\nthere is no {picked_race} race, you might have misstyped\n")
                continue
        
        if checkpoint == "picking_subrace":
            print("\n\n\n", character_sheet)
            creating = False
        
        

#character creation order:
"""
*-class
*-multiclasses
origin:
    *-species
    *-background
    *-feats
    *-languages
*-profeciencies:
    *-skill profeciencies
    *-tool profeciencies
    --saving throw profeciencies
    *-experties?
--profeciency bonus
*-ability scores
details:
    --class features
    x-saving throws
    x-skills
    --passive perception
    --hit points
    --hit die
    --ac
    --speed
    --initiative
    *-equipment:
    *-spells
    --spell slots
    --attacks
    **description:
        *-alignment
        gender?
        bonds?
        etc
--spell attack bonus
--spell save dc
"""

#things not in creation:
"""


equip...:
    attuned items
    

"""






if __name__ == '__main__':
    main()