# from config import *
from telnetlib import GA
from colorama import Fore, Back, Style
import os
import json

from numpy import true_divide

# from scenery import scenery
from src.input import Get, input_to
import src.movingchar as mc
import src.building as b
import src.global_variable as gv
import src.scenery as scenery
import time

os.system("clear")
input_file = input("Enter saved game name: ")
with open("replays/" + input_file + '.json') as json_file:
    replay = json.load(json_file)

loop_num = 0

for input_ in replay:
    loop_num += 1
    if(loop_num == 1):
        player_char = input_  # special input (char determining)
        # close file
        json_file.close()
        break


loop_num = 0
level_1_mark = 0
level_2_mark = 0
# print(replay)
# exit()

if(player_char == "queen" or player_char == "king"):
    with open("replays/" + input_file + '.json') as json_file:
        replay = json.load(json_file)
    
    game_score = 0

    for level in range(3):
        Game_Map = scenery.GameBoard()
        Universal_array = []
        townhall = b.Townhall(Game_Map.array, Game_Map.pseudo_array)
        townH = []
        townH.append(townhall)
        Universal_array.append(townH)

        list_hut = []
        list_hut.append(b.Huts(6, 13, Game_Map.array,
                        Game_Map.pseudo_array, 0))
        list_hut.append(b.Huts(14, 23, Game_Map.array,
                        Game_Map.pseudo_array, 1))
        list_hut.append(b.Huts(8, 25, Game_Map.array,
                        Game_Map.pseudo_array, 2))
        list_hut.append(b.Huts(14, 43, Game_Map.array,
                        Game_Map.pseudo_array, 3))
        list_hut.append(b.Huts(6, 38, Game_Map.array,
                        Game_Map.pseudo_array, 4))
        Universal_array.append(list_hut)

        canon_list = []
        canon_list.append(
            b.Canon(6, 25, Game_Map.array, Game_Map.pseudo_array, 0))
        canon_list.append(
            b.Canon(12, 45, Game_Map.array, Game_Map.pseudo_array, 1))

        if(level == 1):
            canon_list.append(
                b.Canon(14, 44, Game_Map.array, Game_Map.pseudo_array, 2))
        if(level == 2):
            canon_list.append(
                b.Canon(14, 44, Game_Map.array, Game_Map.pseudo_array, 2))
            canon_list.append(
                b.Canon(15, 44, Game_Map.array, Game_Map.pseudo_array, 3))
        Universal_array.append(canon_list)

        wizard_tower_list = []
        wizard_tower_list.append(b.Wizard_tower(
            6, 27, Game_Map.array, Game_Map.pseudo_array, 0))
        wizard_tower_list.append(b.Wizard_tower(
            14, 25, Game_Map.array, Game_Map.pseudo_array, 1))

        if(level == 1):
            wizard_tower_list.append(b.Wizard_tower(
                7, 14, Game_Map.array, Game_Map.pseudo_array, 2))
        if(level == 2):
            wizard_tower_list.append(b.Wizard_tower(
                7, 14, Game_Map.array, Game_Map.pseudo_array, 2))
            wizard_tower_list.append(b.Wizard_tower(
                13, 34, Game_Map.array, Game_Map.pseudo_array, 3))
        Universal_array.append(wizard_tower_list)

        wall = []
        count = 0
        i = int(gv.m/5)
        for j in range(int(gv.n/5), int(4*gv.n/5)):
            wall.append(b.Wall(i, j, Game_Map.array,
                        Game_Map.pseudo_array, count))
            count += 1

        i = int(4*gv.m/5)
        for j in range(int(gv.n/5), int(4*gv.n/5)):
            wall.append(b.Wall(i, j, Game_Map.array,
                        Game_Map.pseudo_array, count))
            count += 1

        j = int(gv.n/5)
        for i in range(int(gv.m/5), int(4*gv.m/5)):
            wall.append(b.Wall(i, j, Game_Map.array,
                        Game_Map.pseudo_array, count))
            count += 1

        j = int(4*gv.n/5)
        for i in range(int(gv.m/5), int(4*gv.m/5)):
            wall.append(b.Wall(i, j, Game_Map.array,
                        Game_Map.pseudo_array, count))
            count += 1

        Universal_array.append(wall)

        if(player_char == "queen"):
            king = mc.Archer_Queen(2, 2, Game_Map.array, Game_Map.pseudo_array)
        elif(player_char == "king"):
            king = mc.king(2, 2, Game_Map.array, Game_Map.pseudo_array)

        barbarians = []
        barbarian_count = 0

        archers = []
        archer_count = 0

        balloons = []
        balloon_count = 0

        universal_iterator = 0
        timeout = 0.24

        quit_game_bool = False
        queen_leviathan = False
        game_over = False
         
        while(1):
            # print(input_)
            input_ = replay[loop_num]
            loop_num += 1
            if(loop_num >= len(replay)):
                game_over = True
                break

            time.sleep(timeout)

            os.system("clear")
            universal_iterator = universal_iterator + 1
            universal_iterator = universal_iterator % 100
            Game_Map.print_board()
            # Game_Map.print_pseudo_array()
            if king.health > 0:
                king.health_bar(Game_Map.array, Game_Map.pseudo_array)
                print(king.health)

            print(king.type)
            if(gv.Nuke == True and gv.Nuke_count == 0 and townhall.health > 0):
                print(Fore.LIGHTMAGENTA_EX +
                        "Nuke is launched" + Style.RESET_ALL)
                Nuke = mc.Nuke(int(gv.m/2), 3, Game_Map.array,
                                Game_Map.pseudo_array)
                gv.Nuke_count += 1

            elif gv.Nuke == True and gv.Nuke_count == 1 and gv.Nuke_isdestroyed == False and townhall.health > 0:
                Nuke.move(Game_Map.array, Game_Map.pseudo_array,
                            Universal_array)
                print("Nuke is approaching the townhall")
            elif gv.Nuke_isdestroyed == True:
                print("Destruction Done\n")
                gv.Nuke_count += 1
                for i in range(gv.m):
                    for j in range(gv.n):
                        if(Game_Map.pseudo_array[i][j] == "N"):
                            Game_Map.array[i][j] = " "
                            Game_Map.pseudo_array[i][j] = " "

            # spells-variables
            gv.Rage_step += 1
            if(gv.Rage_step == 25):
                gv.Rage_spell = False
                gv.Rage_step = 0
                if king.health > 0:
                    king.attack_power = gv.attack_power_king
                for i in barbarians:
                    if i.health > 0:
                        i.attack_power = gv.attack_power_barbarians
                for i in archers:
                    if i.health > 0:
                        i.attack_power = gv.attack_power_archers
                for i in balloons:
                    if i.health > 0:
                        i.attack_power = gv.attack_power_balloons
                timeout = 0.24

            # Health Bar

            for i in barbarians:
                i.health_bar(Game_Map.array, Game_Map.pseudo_array)

            for i in archers:
                i.health_bar(Game_Map.array, Game_Map.pseudo_array)

            for i in balloons:
                i.health_bar(Game_Map.array, Game_Map.pseudo_array)

            # check game_ending:
            game_lost = Game_Map.game_lost(
                king, barbarians, barbarian_count, archers, archer_count, balloons, balloon_count)
            game_won = Game_Map.game_won(Universal_array)
            game_points = Game_Map.game_points(Universal_array)

            if(game_won == True):
                if(level == 0):
                    print("Lol This was Easy one")
                    level_1_mark = loop_num
                    game_score += game_points
                elif(level == 1):
                    print("Nice Nice Nice")
                    level_2_mark = loop_num
                    game_score += game_points
                elif(level == 2):
                    print(Fore.RED + "GAME WON" + Style.RESET_ALL)
                    game_score += game_points
                break
            if(game_lost == True):
                print(Fore.RED + "YOU LOST, koi baat nahi , sab ke liye nhi bna ye game")
                gv.Lost = True
                break

            # Barbarian spawning
            if input_ == "1" and barbarian_count < 6:
                barbarians.append(mc.barbarians(
                    18, 55, Game_Map.array, Game_Map.pseudo_array, barbarian_count))
                barbarian_count += 1
            elif input_ == "2" and barbarian_count < 6:
                barbarians.append(mc.barbarians(
                    2, 17, Game_Map.array, Game_Map.pseudo_array, barbarian_count))
                barbarian_count += 1
            elif input_ == "3" and barbarian_count < 6:
                barbarians.append(mc.barbarians(
                    17, 45, Game_Map.array, Game_Map.pseudo_array, barbarian_count))
                barbarian_count += 1
            elif input_ == "4" and archer_count < 6:
                archers.append(mc.Archers(15, 8, Game_Map.array,
                                Game_Map.pseudo_array, archer_count))
                archer_count += 1
            elif input_ == "5" and archer_count < 6:
                archers.append(mc.Archers(15, 55, Game_Map.array,
                                Game_Map.pseudo_array, archer_count))
                archer_count += 1
            elif input_ == "6" and archer_count < 6:
                archers.append(mc.Archers(2, 45, Game_Map.array,
                                Game_Map.pseudo_array, archer_count))
                archer_count += 1
            elif input_ == "7" and balloon_count < 3:
                balloons.append(mc.Balloons(2, 3, Game_Map.array,
                                Game_Map.pseudo_array, balloon_count))
                balloon_count += 1
            elif input_ == "8" and balloon_count < 3:
                balloons.append(mc.Balloons(18, 3, Game_Map.array,
                                Game_Map.pseudo_array, balloon_count))
                balloon_count += 1
            elif input_ == "9" and balloon_count < 3:
                balloons.append(mc.Balloons(2, 50, Game_Map.array,
                                Game_Map.pseudo_array, balloon_count))
                balloon_count += 1

            # quit game
            elif input_ == "q":
                quit_game_bool = True
                break

            # spells and nuke
            elif input_ == "h":
                if king.health > 0:
                    king.health += 0.5*king.health
                if king.health > 100:
                    king.health = 100
                for i in barbarians:
                    i.health += 0.5*i.health
                    if i.health > gv.max_health_barbarians:
                        i.health = gv.max_health_barbarians
                for i in archers:
                    i.health += 0.5*i.health
                    if i.health > gv.max_health_archers:
                        i.health = gv.max_health_archers
                for i in balloons:
                    i.health += 0.5*i.health
                    if i.health > gv.max_health_balloons:
                        i.health = gv.max_health_balloons
            elif input_ == "r":
                gv.Rage_spell = True
                gv.Rage_step = 0
                if king.health > 0:
                    king.attack_power = int(1.5*king.attack_power)
                for i in barbarians:
                    if i.health > 0:
                        i.attack_power = int(1.5*i.attack_power)
                for i in archers:
                    if i.health > 0:
                        i.attack_power = int(1.5*i.attack_power)
                for i in balloons:
                    if i.health > 0:
                        i.attack_power = int(1.5*i.attack_power)
                timeout /= 2
            elif input_ == 'k':
                pass
            elif input_ == 'n' and level == 0:
                gv.Nuke = True

            # King Controls and attack
            if king.health > 0:
                if input_ == "w":
                    king.move("w", Game_Map.array, Game_Map.pseudo_array)
                elif input_ == "s":
                    king.move("s", Game_Map.array, Game_Map.pseudo_array)
                elif input_ == "a":
                    king.move("a", Game_Map.array, Game_Map.pseudo_array)
                elif input_ == "d":
                    king.move("d", Game_Map.array,  Game_Map.pseudo_array)
                elif input_ == "-":
                    king.damage()
                elif input_ == " ":
                    king.attack(Game_Map.array,
                                Game_Map.pseudo_array, Universal_array)
                elif input_ == "l":
                    if king.type == "king":
                        king.leviathan(
                            Game_Map.array, Game_Map.pseudo_array, Universal_array)
                    elif king.type == "Archer_Queen":
                        print("attack initiated")
                        start = time.time()
                        queen_leviathan = True
                        Game_Map.array[king.x_coor][king.y_coor] = Back.MAGENTA + \
                            king.char + Style.RESET_ALL

            # Barbarian Movement and attack
            for i in barbarians:
                if universal_iterator % 2 == 0:
                    i.bar_move(Game_Map.array,
                                Game_Map.pseudo_array, Universal_array)
                if(i.health <= 0):
                    i.destroy(Game_Map.array, Game_Map.pseudo_array)

            # Archer Movement and attack
            for i in archers:
                i.move(Game_Map.array, Game_Map.pseudo_array, Universal_array)
                if(i.health <= 0):
                    i.health_bar(Game_Map.array, Game_Map.pseudo_array)

            # Balloon Movement and attack
            for i in balloons:
                i.move(Game_Map.array, Game_Map.pseudo_array, Universal_array)
                if(i.health <= 0):
                    i.health_bar(Game_Map.array, Game_Map.pseudo_array)

            # Canon attack
            for i in canon_list:
                if(universal_iterator % 3 == 2):
                    i.attack(Game_Map.array, Game_Map.pseudo_array,
                                king, barbarians, archers)
                if(universal_iterator % 3 == 1 or universal_iterator % 3 == 0):
                    if(i.health > 0):
                        Game_Map.array[i.X_coor][i.Y_coor] = i.color + \
                            'C' + Style.RESET_ALL

            # Wizard attack
            for i in wizard_tower_list:
                if(universal_iterator % 3 == 2):
                    i.attack(Game_Map.array, Game_Map.pseudo_array,
                                king, barbarians, archers, balloons)
                if(universal_iterator % 3 == 1 or universal_iterator % 3 == 0):
                    if(i.health > 0):
                        Game_Map.array[i.X_coor][i.Y_coor] = i.color + \
                            'Y' + Style.RESET_ALL

            # special attack
            if(queen_leviathan == True and time.time() - start > 1):
                queen_leviathan = False
                king.leviathan(
                    Game_Map.array, Game_Map.pseudo_array, Universal_array)
                print("damage done")
                Game_Map.array[king.x_coor][king.y_coor] = king.char + \
                    Style.RESET_ALL

            game_lost = Game_Map.game_lost(
                king, barbarians, barbarian_count, archers, archer_count, balloons, balloon_count)
            if game_lost == True:
                print("YOU LOSE")
                break

        if gv.Lost == True:
            break

        if quit_game_bool == True:
            break

        if game_over == True:
            break
    
    print("FINAL SCORE :", game_score)