# from config import *
from telnetlib import GA
from colorama import Fore, Back, Style
import os
import json

from numpy import save
# from scenery import scenery
from src.input import Get, input_to
import src.movingchar as mc
import src.building as b
import src.global_variable as gv
from src.initialise import Game_Map, Universal_array, townhall, list_hut, canon_list, wall
import src.scenery as scenery
import time


if __name__ == "__main__":
    # Game_Map = []
    # for i in range(3):
    #     Game_Map.append(scenery.GameBoard())

    # print(canon_list)
    # print(wall)
    # user_char = input("Choose character 1 for Archer Queen , 2 for King:")
    # if user_char == "1":
    #     # Archer Queen
    #     PlayingChar = mc.Archer_Queen(2, 2, Game_Map.array, Game_Map.pseudo_array)
    # elif user_char == "2":
    #     # King
    #     PlayingChar = mc.king(2, 2, Game_Map.array, Game_Map.pseudo_array)
    # else: 
    #     PlayingChar = mc.king(2, 2, Game_Map.array, Game_Map.pseudo_array)
        
    PlayingChar = mc.king(2, 2, Game_Map.array, Game_Map.pseudo_array)
    king = PlayingChar
    barbarians = []
    barbarian_count = 0
    archers = []
    archer_count = 0
    universal_iterator = 0
    replay = []
    timeout = 0.24

    for level in range(2,3):

        # if(level == 1):
        #     # clear board
        #     # re run initialise.py
        #     Level_board(1)

        # elif(level == 2):
        #     # clear board
        #     # re run initialise.py
        #     Level_board(2)

       
        
        # timeout = 0.24

        while True:
            # Getting input from user
            input_time = time.time()

            # os.system("cls" if os.name == "nt" else "clear")
            os.system("clear")
            universal_iterator = universal_iterator + 1
            universal_iterator = universal_iterator % 100
            Game_Map.print_board()
            # Game_Map.print_pseudo_array()
            if king.health>0:
                king.health_bar(Game_Map.array, Game_Map.pseudo_array)
                print(king.health)

            
            # Nuke
            if(gv.Nuke == True and gv.Nuke_count == 0):
                print(Fore.LIGHTMAGENTA_EX+ "Nuke is launched" + Style.RESET_ALL)
                Nuke = mc.Nuke(int(gv.m/2), 3, Game_Map.array, Game_Map.pseudo_array)
                gv.Nuke_count += 1
            
            elif gv.Nuke == True and gv.Nuke_count == 1 and gv.Nuke_isdestroyed == False:
                Nuke.move(Game_Map.array, Game_Map.pseudo_array, Universal_array)
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
                timeout = 0.24
                


            # Health Bar
            

            for i in barbarians:
                i.health_bar(Game_Map.array, Game_Map.pseudo_array)
            
            for i in archers:
                i.health_bar(Game_Map.array, Game_Map.pseudo_array)

        


            # check game_ending:
            game_lost = Game_Map.game_lost(king, barbarians,barbarian_count, archers, archer_count)
            game_won = Game_Map.game_won(Universal_array)
            game_points = Game_Map.game_points(Universal_array)

            if(game_won == True):
                if(level == 0):
                    print("Lol This was Easy one")
                elif(level == 1):
                    print("Nice Nice Nice")
                elif(level == 2):
                    print(Fore.RED + "GAME WON" + Style.RESET_ALL)
                    input_file = input("Save Game as: ")
                    with open ("replays/" + input_file + ".json" ,'w')as outfile:
                        json.dump(replay,outfile)
                break
            if(game_lost==True):
                print(Fore.RED + "YOU LOST, koi baat nahi , sab ke liye nhi bna ye game")
                input_file = input("Save Game as: ")
                with open ("replays/" + input_file + ".json" ,'w')as outfile:
                    json.dump(replay,outfile)
                gv.Lost = True
                break


                
            
            
            input_ = input_to(Get(), timeout)
            if(input_ == None):
                input_ = 'k'
            replay.append(input_)
            
            
        
            

            # Barbarian spawning
            if input_ == "1" and barbarian_count < 6:
                barbarians.append(mc.barbarians(18,55, Game_Map.array, Game_Map.pseudo_array, barbarian_count))
                barbarian_count += 1
            elif input_ == "2" and barbarian_count < 6:
                barbarians.append(mc.barbarians(2,17, Game_Map.array, Game_Map.pseudo_array, barbarian_count))
                barbarian_count += 1
            elif input_ == "3" and barbarian_count < 6:
                barbarians.append(mc.barbarians(17,45, Game_Map.array, Game_Map.pseudo_array, barbarian_count))
                barbarian_count += 1
            elif input_ == "4" and archer_count < 6:
                archers.append(mc.Archers(15,8, Game_Map.array, Game_Map.pseudo_array, archer_count))
                archer_count += 1
            elif input_ == "5" and archer_count < 6:
                archers.append(mc.Archers(15,55, Game_Map.array, Game_Map.pseudo_array, archer_count))
                archer_count += 1
            elif input_ == "6" and archer_count < 6:
                archers.append(mc.Archers(2,45, Game_Map.array, Game_Map.pseudo_array, archer_count))
                archer_count += 1

            

            # quit game
            elif input_ == "q":
                input_file = input("Save Game as: ")
                with open ("replays/" + input_file + ".json" ,'w')as outfile:
                    json.dump(replay,outfile)
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
                timeout /= 2
            elif input_ == 'k':
                pass
            elif input_ == 'n':
                gv.Nuke = True
                


            # King Controls and attack
            if king.health>0:
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
                    king.attack(Game_Map.array, Game_Map.pseudo_array)
                elif input_ == "l":
                    king.leviathan(Game_Map.array, Game_Map.pseudo_array, Universal_array)
                    



            # Barbarian Movement and attack
            for i in barbarians:
                i.bar_move(Game_Map.array, Game_Map.pseudo_array)
                i.attack(Game_Map.array, Game_Map.pseudo_array)
                if(i.health<=0):
                    i.destroy(Game_Map.array, Game_Map.pseudo_array)

            # Archer Movement and attack
            for i in archers:
                i.move(Game_Map.array, Game_Map.pseudo_array, Universal_array)
                if(i.health<=0):
                    i.health_bar(Game_Map.array, Game_Map.pseudo_array)

            # Canon attack
            for i in canon_list:
                if(universal_iterator%3 == 2):
                    i.attack(Game_Map.array, Game_Map.pseudo_array, king, barbarians, archers)
                if(universal_iterator%3 == 1):
                    if(i.X_coor >0 and i.X_coor < gv.n and i.Y_coor > 0 and i.Y_coor < gv.m):
                        Game_Map.array[i.X_coor][i.Y_coor] = Fore.GREEN + 'C' + Style.RESET_ALL
            
        

        if gv.Lost == True:
           break
        
    
    
        
      
        
        

        
        

        
        

        

        

        


