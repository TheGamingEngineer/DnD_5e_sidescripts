# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:31:42 2021

@author: akba
"""
import random

##### Target roll table #####
target={1:"you",
        2:"nearest ally",
        3:"nearest enemy",
        4:"farthest ally",
        5:"farthest enemy",
        6:"your weapon",
        7:"nearest ally's weapon",
        8:"nearest enemy's weapon",
        9:"farthest enemy's weapon",
        10:"farthest ally's weapon",
        11:"nearest item in the enviroment",
        12:"farthest item in the enviroment",
        13:"one of your potions",
        14:"nearest ally's potions",
        15:"farthest ally's potions",
        16:"your clothes",
        17:"nearest ally's clothes",
        18:"nearest enemy's clothes",
        19:"farthest friend's clothes",
        20:"farthest enemy's clothes",
        21:"target within 5 ft.",
        22:"target within 10 ft.",
        23:"target within 15 ft.",
        24:"target within 20 ft.",
        25:"target within 25 ft. "}

##### Effect roll table #####
effect={1:"faint blue glow (5 ft radius)",
        2:"grows a big, pink moustasch",
        3:"grow 1d10 inches",
        4:"shrink 1d10 inches",
        5:"indifferent polymorph (roll on creature)",
        6:"fog cloud",
        7:"grows a feathered beard",
        8:"major image (roll on creature)",
        9:"grease",
        10:"hair turns bright green",
        11:"runic skin (advantage on spell saving throws)",
        12:"indifferent summon (roll on creature)",
        13:"mirror image",
        14:"third eye (advantage on perception rolls using sight)",
        15:"AC +2",
        16:"teleport 60 ft",
        17:"animal speech (roll on creature)",
        18:"regain 2d6 hp",
        19:"enlarge",
        20:"reduce",
        21:"regain lowest level spell slot",
        22:"honky shoes (disadvantage on stealth rolls)",
        23:"fear",
        24:"pinochio's nose (disadvantage on deception rolls)",
        25:"invisibility",
        26:"fireball",
        27:"confusion",
        28:"surrounded by illusionary music notes",
        29:"bubbles float out of every orifice",
        30:"magic missile",
        31:"takes extra action",
        32:"melee attacks from source deals an extra 1d4 force",
        33:"vulnerability to ",
        34:"haste",
        35:"sprout fruit that heals 2 hp for an action",
        36:"thunderwave",
        37:"i see everything: truesight",
        38:"arcane cold: roll at the end of each turn",
        39:"handsome face (advantage on persuasion rolls)",
        40:"sprouts a flower",
        41:"disguise self (roll on creature)",
        42:"darkvision",
        43:"gain 10 temporary hp",
        44:"next spell deals max damage",
        45:"next attack deals max damage",
        46:"a singing goblet of wine floats in front",
        47:"smells of perfume (others gain advantage on perception checks using scent)",
        48:"illusionary blue flames radiates from it",
        49:"self-cleaning",
        50:"must shout when speak",
        51:"guidance",
        52:"advantage on next attack",
        53:"advantage on next roll",
        54:"disadvantage on next attack",
        55:"disadvantage on next roll",
        56:"illusionary birds flies around the head",
        57:"alter self (semi-polymorph) (roll on creature)",
        58:"faerie fire",
        59:"heals a status condition",
        60:"max-level dispel magic",
        61:"hold monster",
        62:"grow thin fur",
        63:"slow",
        64:"drunk: disadvantage on charisma and attack rolls",
        65:"sleep",
        66:"hair changes color every second",
        67:"faint, changing light radiates in a 5-ft. radius",
        68:"eyes change colour",
        69:"must whisper when speaking",
        70:"grow feathers",
        71:"blindness",
        72:"deafness",
        73:"must sing when speaking",
        74:"AC -2",
        75:"hear faint music in his ears",
        76:"grow a green unibrow",
        77:"a ham sandwich floats on a plate next to ...",
        78:"levitate",
        79:"spell DC vs constitution save or be poisoned",
        80:"faint music can be heard from .....",
        81:"spell DC vs charisma save or smile",
        82:"spell DC vs charisma save or scowl",
        83:"immunity to intoxication",
        84:"speak abyssal, when speaking",
        85:"immunity to ",
        86:"bird twirping can be heard in a 5-ft radius",
        87:"gain swimming speed equal to walking speed",
        88:"gain climbing speed equal to walking speed",
        89:"water-breathing",
        90:"gain +1 to attacks and damage",
        91:"purple smoke rises from head",
        92:"walking speed increases by 10 ft.",
        93:"walking speed decreases by 10 ft.",
        94:"1 gp appears on the tongue at the start of every round.",
        95:"can read any language",
        96:"can understand any language",
        97:"Resistance to ",
        98:"gain 2d8 hp and temporary hp",
        99:"regain any spell slot",
        100:"roll twice"}

##### Duration roll table #####
duration={1:"until end of turn",
          2:"1 round",
          3:"2 rounds",
          4:"3 rounds",
          5:"1 min.",
          6:"10 min.",
          7:"8 h.",
          8:"until rest"}

##### Creature roll table #####
creature={1:"sheep",
          2:"owl",
          3:"frog",
          4:"boar",
          5:"pseudodragon",
          6:"flumph",
          7:"sprite",
          8:"flying snake",
          9:"mastiff",
          10:"reef shark",
          11:"riding horse",
          12:"unicorn"}

##### Direction roll table #####
direction={1:"east",
          2:"north-east",
          3:"north",
          4:"north-west",
          5:"west",
          6:"south-west",
          7:"south",
          8:"south-east",
          9:"up",
          10:"to own place",
          11:"no teleport",
          12:"roll twice"}

##### damage type roll table #####
damage_type={1:"acid",
             2:"bludgeoning",
             3:"cold",
             4:"fire",
             5:"force",
             6:"lightning",
             7:"necrotic",
             8:"piercing",
             9:"psychic",
             10:"radiant",
             11:"slashing",
             12:"thunder"}

# number of rolls
rolls=1

##### Roll the dices #####
targetRoll=random.randint(1,25)
effectRoll=random.randint(1,100)
if effectRoll==100:
    rolls+=1
durationRoll=random.randint(1,8)
extraRoll=random.randint(1,12)

##### Determine the results #####
# first the target, if any
while rolls!=0:
    if effectRoll!=12 and effectRoll!=100:
        print("Target:",target[targetRoll])
    # Determine effeect
    if effectRoll in [33,85,97]:
        print("Effect:",effect[effectRoll],damage_type[extraRoll]," damage")
    else:
        print("Effect:",effect[effectRoll])
    # for effects with a duration (meaning no damage/healing effects), roll duration
    if effectRoll not in [16,18,26,30,36,59,60,99,100]:
        print("Duration:",duration[durationRoll])
    # if the roll is a teleport, then roll a direction
    if effectRoll==16:
        print("Direction:",direction[extraRoll])
        while extraRoll==12:
            extraRoll=random.randint(1,12)
            print("60 ft.", extraRoll)
            extraRoll=random.randint(1,12)
            print("60 ft.", extraRoll)
    # if the roll requires a creature, determine creature
    if effectRoll in [5,8,12,17,41,57]:
        print("Creature:",creature[extraRoll])
    # for size-changes that are not enlarge/reduce, determine growth
    if effectRoll in [3,4]:
        print("size-change: ",random.randint(1,10))
    # for healing
    if effectRoll==18:
        print(random.randint(2,12)," healing")
    # for healning and temporary HP
    if effectRoll==98:
        print(random.randint(2,16)," healing and temporary HP")
    # for resistance, immunity and vulnerability
    
    # for effects that are spells, determine spell level and the extended effects based on that level
    if effectRoll in [6,25,26,27,30,36,41,61,63,65,71,72,78,79,81,82]:
        ##### Determine spell levels #####
        
        if effectRoll in [25,71,72]: # invisibility and blindness/deafness are 2nd level spells, so they start at level 2
            spellLevelRoll=random.randint(2,9)
        elif effectRoll==26:# fireball is a 3rd level spell, so start at level 3
            spellLevelRoll=random.randint(3,9)
        elif effectRoll==27: # confusion is a 4th level spell, so start at level 4 
            spellLevelRoll=random.randint(4,9)
        elif effectRoll==61: # hold monster is a 5th level spell, so start at level 5
            spellLevelRoll=random.randint(5,9)
        else:
            spellLevelRoll=random.randint(1,9) # roll standard level for 1st level spells
        if effectRoll not in [79,81,82]:
            print("spell level: ", spellLevelRoll) # print spell level
    
        ##### Determine spell DC #####
        spellDC=random.randint(1,20)
    
        ##### Expanded effects based on spells and spell level #####
        if effectRoll==6: # fog cloud (1st level) at higher levels
            print("Area: ", 20*spellLevelRoll, " ft.")
        elif effectRoll in [25,71,72] and spellLevelRoll>2: # invisibility and blindness/deafness (2nd level) at higher levels
            if effectRoll in [71,72]:
                print("DC: ",spellDC,"constitution saving throw",'\n',"on failed save: fall under the effects of the spell")
            while spellLevelRoll!=2:
                print("Extra target: ",target[random.randint(1,25)])
                spellLevelRoll-=1
        elif effectRoll==26: # fireball (3rd level) at higher levels
            damage=random.randint(8,48)
            while spellLevelRoll!=3:
                damage+=random.randint(1,8)
                spellLevelRoll-=1
            print(damage," fire damage",'\n',"Area: 20-ft. sphere centered on target",'\n',"DC: ",spellDC," Dexterity saving throw",'\n',"on failed save: full damage")
        elif effectRoll==27: # confusion (4th leve) at higher levels
            area=10
            while spellLevelRoll!=4:
                area+=5
                spellLevelRoll-=1
            print("Area: ",area," ft. sphere around target",'\n',"DC: ",spellDC," wisdom saving throw",'\n',"on failed save: fall under the effects of the spell")
        elif effectRoll==30: # magic missile (1st level) at higher levels
            damage=random.randint(6,15)
            while spellLevelRoll!=1:
                damage+=random.randint(2,5)
                spellLevelRoll-=1
            print(damage," force damage")
        elif effectRoll==36: # thunderwave (1st level) at higher levels
            damage=random.randint(2,16)
            while spellLevelRoll!=1:
                damage+=random.randint(1,8)
                spellLevelRoll-=1
            print(damage," thunder damage",'\n',"Area: 15-foot cube around target",'\n',"DC: ",spellDC," constitution saving throw",'\n',"on failed save: full damage and push 10 feet")
        elif effectRoll==41: # disguise self
            print("DC: ",spellDC," intelligence(investigation)")
        elif effectRoll==61 and spellLevelRoll>5: # hold monster (5th level) at higher levels
            while spellLevelRoll!=5:
                print("Extra target: ",target[random.randint(1,25)])
                spellLevelRoll-=1
            print("DC: ",spellDC," wisdom saving throw",'\n', "on failed save: fall under the effect of the spell")
        elif effectRoll==63: # slow
            print("DC: ", spellDC,'\n',"on failed save: fall under the effect of the spell")
        elif effectRoll==65: #sleep (1st level) at higher levels
            damage=random.randint(5,40)
            while spellLevelRoll!=1:
                damage+=random.randint(2,16)
                spellLevelRoll-=1
            print(damage," HP falls asleep on and around target, if necessary.")
        elif effectRoll==78:
            print("DC: ",spellDC," constitution saving throw",'\n',"on failed save: levitate ",random.randint(1,20),"ft. off the ground")
        elif effectRoll in [79,81,82]: # poisoned, smiling or scowling
            if effectRoll==79:
                save=" constitution"
            else:
                save=" charisma"
            print("DC: ",spellDC,save," saving throw")
    rolls-=1
    if rolls!=0:
        targetRoll=random.randint(1,25)
        effectRoll=random.randint(1,100)
        if effectRoll==100:
            rolls+=1
        durationRoll=random.randint(1,8)
        extraRoll=random.randint(1,12)
    print('\n')