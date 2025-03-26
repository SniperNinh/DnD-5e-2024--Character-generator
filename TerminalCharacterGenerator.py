#prompts through the terminal to make non-random character

import pyfiglet
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


commands = {"help" : dnd_help}


def main():
    print(pyfiglet.figlet_format("DnD  5e  C. S. G."))
    print('type "help" for list of commands')
    print('type "random" for a random chacter')
    print('type "start" to begin making a character\n')
    
    running = True
    
    while running:
        
        called = input()
        
        if called in commands:
            commands[called]()
        else:
            print(f'\nthe command {called} does not exist\ntype "help" for a full list of commands\n')





if __name__ == '__main__':
    main()