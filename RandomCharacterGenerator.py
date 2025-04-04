#randomly generate dnd 5e character sheet

import random
import math
import settings
from randomAbilityScores import randomAbilityScores
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



def race():
    racesSelection = {"dwarf":dwarf, "elf":elf, "halfling":halfling, "human":human, "dragonborn":dragonborn, "gnome":gnome, "halfelf":halfElf, "halforc":halfOrc, "tiefling":tiefling}
    ranRace = random.choice(list(racesSelection.values()))
    ranRace()
    print(settings.race)
    print(settings.alignment)


def classes():
    classSelection = {"barbarian":barbarian}#, "bard":bard, "cleric":cleric, "druid":druid, "fighter":fighter, "monk":monk, "paladin":paladin, "ranger":ranger, "rogue":rogue, "sorcerer":sorcerer, "warlock":warlock, "wizard":wizard}
    ranClass = random.choice(list(classSelection.values()))
    ranClass()
    print(settings.classes)



def background():
    backgroundSelection = {"acolyte":acolyte, "charlatan":charlatan, "criminal":criminal, "entertainer":entertainer, "folkhero":folkHero, "guildartisan":guildArtisan, "hermit":hermit, "noble":noble, "outlander":outlander, "sage":sage, "sailor":sailor, "soldier":soldier, "urchin":urchin}
    ranBackground = random.choice(list(backgroundSelection.values()))
    ranBackground()
    print(settings.background)
    print(settings.wealth)


def main():
    
    settings.init()
    randomAbilityScores()
    race()
    background()
    classes()

if __name__ == '__main__':
    main()