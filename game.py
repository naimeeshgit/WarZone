# from config import *
from colorama import Fore, Back, Style
import os
# from scenery import scenery
from input import Get, input_to
from character import *
import scenery
import movingchar as mc
import building as b
import global_variable as gv
from initialise import Game_Map, townhall, list_hut, canon_list, wall

if __name__ == "__main__":

    # print(canon_list)
    # print(wall)

    while True:
        # Getting input from user

        input_ = input_to(Get())

        # spawning: key = "X"
        # if king_deploy == False: -> deploy king
        # else if barbarian_1_deploy == False: -> deploy barbarian_1 (deploy from left)
        # else if barbarian_2_deploy == False: -> deploy barbarian_2 (deploy from bottom)
        # else if barbarian_3_deploy == False: -> deploy barbarian_3 (deploy from right)

        # king.move(input_) -> move king , keys = wsad

        if input_ == "x":
            if gv.king_deploy == False:
                king = mc.king(1,1, Game_Map.array, Game_Map.pseudo_array)
                gv.king_deploy = True
            elif gv.barbarian_1_deploy == False:
                barbarian_1 = mc.barbarians(19,1, Game_Map.array, Game_Map.pseudo_array)
                gv.barbarian_1_deploy = True
            elif gv.barbarian_2_deploy == False:
                barbarian_2 = mc.barbarians(19, 59, Game_Map.array, Game_Map.pseudo_array)
                gv.barbarian_2_deploy = True
            elif gv.barbarian_3_deploy == False:
                barbarian_3 = mc.barbarians(1, 59,Game_Map.array, Game_Map.pseudo_array)
                gv.barbarian_3_deploy = True

        elif input_ == "w":
            king.move("w", Game_Map.array, Game_Map.pseudo_array)
        elif input_ == "s":
            king.move("s", Game_Map.array, Game_Map.pseudo_array)
        elif input_ == "a":
            king.move("a", Game_Map.array, Game_Map.pseudo_array)
        elif input_ == "d":
            king.move("d", Game_Map.array,  Game_Map.pseudo_array)
        elif input_ == "q":
            break
        elif input_ == "-":
            king.damage()
        elif input_ == "1":
            townhall.damage(5,Game_Map.array, Game_Map.pseudo_array)
        elif input_ == "2":
            wall[1].damage(1,Game_Map.array, Game_Map.pseudo_array)
        elif input_ == "3":
            list_hut[2].damage(1,Game_Map.array, Game_Map.pseudo_array)
        elif input_ == "4":
            canon_list[0].damage(1,Game_Map.array, Game_Map.pseudo_array)
        elif input_ == "5":
            print("attack")
            king.attack(Game_Map.array, Game_Map.pseudo_array)
            
            
        
        Game_Map.print_board()
        

        
        

        
        

        

        

        


