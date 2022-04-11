# from config import *
from colorama import Fore, Back, Style
# from scenery import scenery
from src.input import Get, input_to
import src.scenery
import src.movingchar as mc
import src.building as b
import src.global_variable as gv

Game_Map = src.scenery.GameBoard()


Universal_array = []



# Game_Map.print_board()
townhall = b.Townhall(Game_Map.array,Game_Map.pseudo_array)
townH = []
townH.append(townhall)
Universal_array.append(townH)

list_hut = []
list_hut.append(b.Huts(6, 13, Game_Map.array, Game_Map.pseudo_array, 0))
list_hut.append(b.Huts(14, 23, Game_Map.array, Game_Map.pseudo_array, 1))
list_hut.append(b.Huts(8, 25, Game_Map.array, Game_Map.pseudo_array, 2))
list_hut.append(b.Huts(14, 43, Game_Map.array, Game_Map.pseudo_array, 3))
list_hut.append(b.Huts(6, 38, Game_Map.array, Game_Map.pseudo_array, 4))
Universal_array.append(list_hut)

canon_list = []
canon_list.append(b.Canon(6, 25, Game_Map.array, Game_Map.pseudo_array, 0))
Universal_array.append(canon_list)
canon_list.append(b.Canon(12, 45, Game_Map.array, Game_Map.pseudo_array, 1))

wizard_tower_list = []
wizard_tower_list.append(b.Wizard_tower(6, 27, Game_Map.array, Game_Map.pseudo_array, 0))
wizard_tower_list.append(b.Wizard_tower(14, 25, Game_Map.array, Game_Map.pseudo_array, 1))

wall = []
count = 0
i = int(gv.m/5)
for j in range(int(gv.n/5), int(4*gv.n/5)):
    wall.append(b.Wall(i, j, Game_Map.array, Game_Map.pseudo_array, count))
    count += 1

i = int(4*gv.m/5)
for j in range(int(gv.n/5), int(4*gv.n/5)):
    wall.append(b.Wall(i, j, Game_Map.array, Game_Map.pseudo_array, count))
    count += 1

j = int(gv.n/5)
for i in range(int(gv.m/5), int(4*gv.m/5)):
    wall.append(b.Wall(i, j, Game_Map.array, Game_Map.pseudo_array, count))
    count += 1

j = int(4*gv.n/5)
for i in range(int(gv.m/5), int(4*gv.m/5)):
    wall.append(b.Wall(i, j, Game_Map.array, Game_Map.pseudo_array, count))
    count += 1

Universal_array.append(wall)


Game_Map.print_board()
# print("x")
# print(townhall)
# print(list_hut[0].X_coor, list_hut[0].Y_coor)
# print(Game_Map.array[6][15])
# print(Game_Map.pseudo_array[6][15])


