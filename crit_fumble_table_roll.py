# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:05:24 2021

@author: akba
"""
import random
import sys
sucfail=input("are we looking for success or failure?")
if sucfail[0].lower()!="s" and sucfail[0].lower()!="f":
    sys.exit("ERROR: first input must be either (s)uccess or (f)ailure. Both fully written and abriviation can be used.")
magic_weapon=input("magic or weapon?")
if magic_weapon[0].lower()!="m" and magic_weapon[0].lower()!="w":
    sys.exit("ERROR: second input must be either (m)agic or (w)eapon. Both fully written and abriviation can be used.")

magicsuc={"a":"regular spel critical hit",
          "b":"you can choose to gain advantage on your next attack roll against your target, but all enemies have advantage on their attack rolls against you until the end of your next turn.",
          "c":"you can choose to gain advantage on your next attack roll against your target, your target has advantage on their attack rolls against you until the end of your next turn.",
          "d":"you are able to use the disengage action after your attack.",
          "e":"after your turn you move to the top of the initiative order.",
          "f":"your target's movement speed is cut in half for their next 2 turns.",
          "g":"your target is knocked prone.",
          "h":"your target is blinded until the end of their next turn.",
          "i":"your targets weapon is flung 1d6*5 feet away in a random direction. If the target is only using natural weapons, the target is knocked prone instead.",
          "j":"your target is frightened by you until you stop casting magic. you are able to discern the source of your targets fear.",
          "k":"your target is incapacitated until the end of their next turn",
          "l":"roll 10d8. if your targets current health is lower than the number rolled, they fall asleep for 1 minute.",
          "m":"your target is surprised untill the end of their next turn.",
          "n":"roll an additional set of spell damage dice above and beyond your normal critical roll.",
          "o":"roll an additional set of spell damage dice above and beyond your normal critical roll and the target suffers one unit of exhaustion.",
          "p":"roll an additional set of spell damage dice above and beyond your normal critical roll and the target suffers a permanent injury chosen by the DM. The permanent injury can be healed with extended rest of a length determined by the DM, but the attack leaves a scar.",
          "q":"roll an additional set of spell damage dice above and beyond your normal critical roll, the target suffers one unit of exhaustion and the target suffers a permanent injury chosen by the DM. The permanent injury can be healed with extended rest of a length determined by the DM, but the attack leaves a scar."}
magicfail={"a":"you miss your attack",
           "b":"your target has advantage on their first attack roll against you next round.",
           "c":"all enemies have advantage on their first attack roll against you next round.",
           "d":"all enemies have advantage on their attack rolls against you until the end of your next turn.",
           "e":"the area in a 5 foot radius around your location becomes heavily obscured for 1 minute. A strong breeze can blow away the smoke in 1 round.",
           "f":"you are knocked prone.",
           "g":"you have disadvantage on any spell attacks, and enemies ahve advantage against your spel saving throws until the end of your next turn.",
           "h":"your target is able to use their reaction to take an attack of opportunity on one of your allies in melee range.",
           "i":"you are unable to use material components to cast spells until the end of your next turn.",
           "j":"you are unable to use somatic components to cast spells untill the end of your next turn.",
           "k":"you are unable to use verbal components to cast spells until the end of your next turn.",
           "l":"end your turn and move to the bottom of the initiative order at the start of the next round.",
           "m":"end your current turn and you are surprised until the end of your next turn.",
           "n":"you fall prone. Roll a DC 10 constitution saving throw. On a failed save, you take 1d6 bludgeoning damage and are knocked unconscious for 1 minute or unt you recieve damage from any source. On a succeeded save, you take half the damage and you remain conscious.",
           "o":"you fall prone. roll a DC 15 constitution saving throw. On a failed save, you take 1d6 bludgeoning damage, 1d6 thunder damage and are knocked unconscious for 1 minute or until you recieve damage from any scource. On a succeeded save, you take half the damage and you remain conscious.",
           "p":"you hit yourself with your spell. If the spell effect is instant, you take the full effect. If the spell requires concentration, the effect persists until the end of your next turn. You also fall prone, take 1d6 bludgeoning damage, 1d6 thunder damage, and are knocked unconscious for 1 minute or until you recieve damage from any source."}
weaponsuc={"a":"regular critical hit",
          "b":"you can choose to gain advantage on all attacks against your target until the end of your next turn, but if you do, all enemies have advantage on their attack rolls against you until the end of your next turn.",
          "c":"you can choose to gain advantage on all attacks against your target next turn, your target has advantage on their attack rolls against you until the end of your next turn",
          "d":"you gain advantage on all attacks against your target until the end of your next turn",
          "e":"you are able to use the disengage action after your attack",
          "f":"after your turn, you move to the top of the initiative order",
          "g":"you gain +2 to your AC against your target and advantage on all saving throws from effects originating from your target until your next turn",
          "h":"after your attack, you can choose to attempt to grapple your opponent, if you have a free hand, or attempt to shove your opponent, if both hands are in use",
          "i":"after your attack, you can choose to automatically succeed in grappling your opponent, if you have a free hand, or shoving your opponent, if both hands are in use",
          "j":"you are able to take the disarm action after your attack. If the target only have natural weapons, the target is surprised until your next turn, instead.",
          "k":"you are able to take the disarm action after your attack and steal your opponents weapon, if you have a free hand. otherwise, you can knock it up to 20 feet away. If the target only have natural weapons, the target is surprised until your next turn, instead.",
          "l":"you are able to use the dodge action after your attack",
          "m":"your target is knocked prone",
          "n":"your target is surprised until the end of their next turn",
          "o":"roll an additional set of damage dice above and beyond your normal critical roll",
          "p":"roll an additional set of damage dice above and beyond your normal critical roll, and the target suffers one unit of exhaustion",
          "q":"roll an additional set of damage dice above and beyond your normal critical roll, and the target suffers a permanent injury chosen by the DM.  the permanent injury can be healed with extended rest of a length determined by the DM, but the attack leaves a scar",
          "r":"roll an additional set of damage dice above and beyond your normal critical roll and the target suffers 1 unit of exhaustion, and the target suffers a permanent injury chosen by the DM. The permanent injury can be healed with extended rest of a length determined by the DM, but the attack leaves a scar"}
weaponfail={"a":"you miss your attack",
           "b":"your target has advantage on their first attack roll against your next round.",
           "c":"your enemies have advantage on their first attack roll against you next round",
           "d":"your enemies have advantage on their attack rolls against you until the end of your next turn",
           "e":"MELEE: you are knocked prone and your movement is reduced to 0. your target must suceed a DC 10 dexterity check or they are also knocked prone.RANGED:you must use an action to organise the ammunition in its case before you can make another ranged attack.",
           "f":"you fall prone and your movement is reduced to 0.",
           "g":"you have disadvantage on your next attack roll against your target.",
           "h":"you have disadvantage on your next attack roll against any target.",
           "i":"roll a DC 10 dexterity check. On a failed check, you drop your weapon at your feet. If you fight unarmed, a failed check knocks you prone.",
           "j":"MELEE: the enemy that you were attacking is able to use their reaction to perform an attack of opportunity. RANGED: the target can perform an opportunity attack on any ally within melee range.",
           "k":"end your current turn and you are surprised until the end of your next turn.",
           "l":"end your turn and move to the bottom of the initiative order at the start of the next round.",
           "m":"you fall prone. Roll a DC 10 constitution saving throw. On a failed save, you take 1d6 damage and are knocked unconscious for 1 minute or until you recieve damage from any source. On a success, you take half damage and remain conscious",
           "n":"you fall prone. Roll a DC 15 constitution saving throw. on a failed save, you take 2d6 damage and are knocked unconscious for 1 minute or until you recieve damage from any source. On a success, you take half damage and you remain conscious.",
           "o":"you fall prone and take 3d6 damage and become unconscious for 1 minute or until you receive damage from any source."}

diceroll=random.randint(1,100)
tablecat=""
tableuse={}
if magic_weapon[0].lower()=="w":
    if sucfail[0].lower()=="s":    
        tableuse=weaponsuc
        if diceroll==1:
            tablecat="a"
        elif diceroll in range(2,6):
            tablecat="b"
        elif diceroll in range(6,10):
            tablecat="c"
        elif diceroll in range(10,15):
            tablecat="d"
        elif diceroll in range(15,20):
            tablecat="e"
        elif diceroll in range(20,25):
            tablecat="f"
        elif diceroll in range(25,30):
            tablecat="g"
        elif diceroll in range(30,40):
            tablecat="h"
        elif diceroll in range(40,50):
            tablecat="i"
        elif diceroll in range(50,60):
            tablecat="j"
        elif diceroll in range(60,70):
            tablecat="k"
        elif diceroll in range(70,75):
            tablecat="l"
        elif diceroll in range(75,80):
            tablecat="m"
        elif diceroll in range(80,85):
            tablecat="n"
        elif diceroll in range(85,90):
            tablecat="o"
        elif diceroll in range(90,95):
            tablecat="p"
        elif diceroll in range(95,100):
            tablecat="q"
        elif diceroll==100:
            tablecat="r"
    elif sucfail[0].lower()=="f":
        tableuse=weaponfail
        if diceroll==1:
            tablecat="a"
        elif diceroll in range(2,6):
            tablecat="b"
        elif diceroll in range(6,10):
            tablecat="c"
        elif diceroll in range(10,15):
            tablecat="d"
        elif diceroll in range(15,20):
            tablecat="e"
        elif diceroll in range(20,30):
            tablecat="f"
        elif diceroll in range(30,40):
            tablecat="g"
        elif diceroll in range(40,50):
            tablecat="h"
        elif diceroll in range(50,60):
            tablecat="i"
        elif diceroll in range(60,70):
            tablecat="j"
        elif diceroll in range(70,80):
            tablecat="k"
        elif diceroll in range(80,85):
            tablecat="k"
        elif diceroll in range(85,90):
            tablecat="l"
        elif diceroll in range(90,95):
            tablecat="m"
        elif diceroll in range(95,100):
            tablecat="n"
        elif diceroll==100:
            tablecat="o"
elif magic_weapon[0].lower()=="m":
    if sucfail[0].lower()=="s":
        tableuse=magicsuc
        if diceroll==1:
            tablecat="a"
        elif diceroll in range(2,6):
            tablecat="b"
        elif diceroll in range(6,10):
            tablecat="c"
        elif diceroll in range(10,15):
            tablecat="d"
        elif diceroll in range(15,20):
            tablecat="e"
        elif diceroll in range(20,30):
            tablecat="f"
        elif diceroll in range(30,40):
            tablecat="g"
        elif diceroll in range(40,50):
            tablecat="h"
        elif diceroll in range(50,60):
            tablecat="i"
        elif diceroll in range(60,70):
            tablecat="j"
        elif diceroll in range(70,75):
            tablecat="k"
        elif diceroll in range(75,80):
            tablecat="l"
        elif diceroll in range(80,85):
            tablecat="m"
        elif diceroll in range(85,90):
            tablecat="n"
        elif diceroll in range(90,95):
            tablecat="o"
        elif diceroll in range(95,100):
            tablecat="p"
        elif diceroll==100:
            tablecat="q"
    elif sucfail[0].lower()=="f":
        tableuse=magicfail
        if diceroll==1:
            tablecat="a"
        elif diceroll in range(2,6):
            tablecat="b"
        elif diceroll in range(6,10):
            tablecat="c"
        elif diceroll in range(10,15):
            tablecat="d"
        elif diceroll in range(15,20):
            tablecat="e"
        elif diceroll in range(20,30):
            tablecat="f"
        elif diceroll in range(30,40):
            tablecat="g"
        elif diceroll in range(40,50):
            tablecat="h"
        elif diceroll in range(50,60):
            tablecat="i"
        elif diceroll in range(60,70):
            tablecat="j"
        elif diceroll in range(70,80):
            tablecat="k"
        elif diceroll in range(80,85):
            tablecat="l"
        elif diceroll in range(85,90):
            tablecat="m"
        elif diceroll in range(90,95):
            tablecat="n"
        elif diceroll in range(95,100):
            tablecat="o"
        elif diceroll==100:
            tablecat="p"

print(diceroll)
print(tableuse[tablecat])
if tableuse==magicsuc:
    if tablecat=="i":
        print("distance flung =", random.randint(1,6)*5,"feet")
    elif tablecat=="l":
        print("HP sleep:",random.randint(10,80))
elif tableuse==magicfail:
    if tablecat=="n":
        print(random.randint(1,6)," bludgeoning damage")
    elif tablecat=="o" or tablecat=="p":
        print(random.randint(1,6)," bludgeoning damage")
        print(random.randint(1,6)," thunder damage")
elif tableuse==weaponfail:
    if tablecat=="m":
        print(random.randint(1,6)," damage")
    elif tablecat=="n":
        print(random.randint(2,12)," damage")
    elif tablecat=="o":
        print(random.randint(3,18)," damage")
        
        
        