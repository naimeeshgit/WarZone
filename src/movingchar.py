import time
import os
import src.global_variable as gv
import src.building as b
from src.initialise import Game_Map, townhall, list_hut, canon_list, wall, Universal_array, townH
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


class Character:

    def __init__(self):
        self.movement_speed = 1

    def move(self, direction, array, pseudo_array):
        old_x = self.x_coor
        old_y = self.y_coor

        if self.type == "king":
            if direction == "w":
                if(self.x_coor > 0):
                    if(array[self.x_coor-1][self.y_coor] != " "):
                        array[self.x_coor][self.y_coor] = "K"
                    else:
                        self.x_coor -= 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = "K"
                        pseudo_array[self.x_coor][self.y_coor] = "K"

                self.last_move = "w"
            elif direction == "s":
                if(self.x_coor < gv.m-1):
                    if(array[self.x_coor+1][self.y_coor] != " "):
                        array[self.x_coor][self.y_coor] = "K"
                    else:
                        self.x_coor += 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = "K"
                        pseudo_array[self.x_coor][self.y_coor] = "K"

                self.last_move = "s"
            elif direction == "a":
                if(self.y_coor > 0):
                    if(array[self.x_coor][self.y_coor-1] != " "):
                        array[self.x_coor][self.y_coor] = "K"
                    else:
                        self.y_coor -= 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = "K"
                        pseudo_array[self.x_coor][self.y_coor] = "K"

                self.last_move = "a"
            elif direction == "d":
                if(self.y_coor < gv.n-1):
                    if(array[self.x_coor][self.y_coor+1] != " "):
                        array[self.x_coor][self.y_coor] = "K"
                    else:
                        self.y_coor += 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = "K"
                        pseudo_array[self.x_coor][self.y_coor] = "K"

                self.last_move = "d"

    def health_bar(self, array, pseudo_array):
        health = self.health
        health_value = int(health/10)

        if(health <= 0):
            self.destroy(array, pseudo_array)

        healthBar = ""
        for i in range(health_value):
            if i <= 2:
                healthBar += Back.RED + "  "
            elif i <= 5:
                healthBar += Back.YELLOW + "  "
            elif i <= 10:
                healthBar += Back.GREEN + "  "
        print(healthBar)

    def destroy(self, array, pseudo_array):
        self.health = 0
        array[self.x_coor][self.y_coor] = " "
        pseudo_array[self.x_coor][self.y_coor] = " "
        self.x_coor = -1
        self.y_coor = -1
        self.attack_power = 0

    def damage(self):
        self.health -= gv.canon_damage

    def attack(self, array, pseudo_array):
        # print(self.x_coor, self.y_coor)
        curr_X = self.x_coor
        curr_Y = self.y_coor
        if self.last_move == "w":
            # print("we can attack")
            if(pseudo_array[curr_X-1][curr_Y] != ' '):
                code = pseudo_array[curr_X-1][curr_Y]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power, array, pseudo_array)

        elif self.last_move == "s":
            if(pseudo_array[curr_X+1][curr_Y] != ' '):
                code = pseudo_array[curr_X+1][curr_Y]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power, array, pseudo_array)

        elif self.last_move == "a":
            if(pseudo_array[curr_X][curr_Y-1] != ' '):
                code = pseudo_array[curr_X][curr_Y-1]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power, array, pseudo_array)

        elif self.last_move == "d":
            if(pseudo_array[curr_X][curr_Y+1] != ' '):
                code = pseudo_array[curr_X][curr_Y+1]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power, array, pseudo_array)

    def leviathan(self, array, pseudo_array, Universal_array):
        for i in range(4):
            for j in Universal_array[i]:
                if((self.x_coor - j.X_coor)**2 + (self.y_coor - j.Y_coor)**2 <= 25):
                    j.damage(self.attack_power, array, pseudo_array)


class king(Character):
    def __init__(self, x_coor, y_coor, array, pseudo_array):
        self.type = "king"
        self.x_coor = x_coor
        self.y_coor = y_coor
        array[self.x_coor][self.y_coor] = "K"
        pseudo_array[self.x_coor][self.y_coor] = "K"
        self.health = gv.max_health_king
        self.last_move = " "
        self.attack_power = gv.attack_power_king
        self.movement_speed = 1
        # self.color = Back.BLUE

class Archer_Queen(Character):
    def __init__(self, x_coor, y_coor, array, pseudo_array):
        self.type = "Archer_Queen"
        self.x_coor = x_coor
        self.y_coor = y_coor
        array[self.x_coor][self.y_coor] = "A"
        pseudo_array[self.x_coor][self.y_coor] = "A"
        self.health = gv.max_health_archer_queen
        self.last_move = " "
        self.attack_power = gv.attack_power_archer_queen
        self.movement_speed = 1
        # self.color = Back.BLUE


class Nuke(Character):
    def __init__(self, x_coor, y_coor, array, pseudo_array):
        self.type = "Rocket"
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.color = Fore.BLUE
        array[self.x_coor][self.y_coor] = self.color + "N" + Style.RESET_ALL
        pseudo_array[self.x_coor][self.y_coor] = "N"
        self.last_move = " "
        self.attack_power = gv.attack_power_nuke
        # self.color = Back.BLUE

    def move(self, array, pseudo_array, Universal_array):
        if(self.x_coor == Universal_array[0][0].X_coor and self.y_coor == Universal_array[0][0].Y_coor):
            self.x_coor = -1
            self.y_coor = -1
            Universal_array[0][0].damage(
                self.attack_power, array, pseudo_array)
            gv.Nuke_isdestroyed = True

            file = "bomb_explosion_sms.mp3"
            os.system("mpg123 " + file)
            time.sleep(0.24)
            print("Destroyed the townhall")

            return

        else:
            self.y_coor += 1
            if(pseudo_array[self.x_coor][self.y_coor] == ' '):
                pseudo_array[self.x_coor][self.y_coor] = "N"
                array[self.x_coor][self.y_coor] = self.color + \
                    "N" + Style.RESET_ALL


class barbarians(Character):
    def __init__(self, x_coor, y_coor, array, pseudo_array, barbarian_count):
        self.type = "barbarians"
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.color = Back.GREEN
        array[self.x_coor][self.y_coor] = self.color + "B" + Style.RESET_ALL
        pseudo_array[self.x_coor][self.y_coor] = "B"
        self.health = gv.max_health_barbarians
        self.last_move = " "
        self.attack_power = gv.attack_power_barbarians
        self.barbarian_id = barbarian_count
        self.movement_speed = 1

    def bar_move(self, array, pseudo_array):
        old_x = self.x_coor
        old_y = self.y_coor

        if(self.health > 0):

            # iterate over all the objects and find nearest object
            # Euclidean distance
            # iterate over Universal_array
            min_distance = 10000
            i_temp, j_temp = 0, 0
            for i in range(3):
                for j in range(len(Universal_array[i])):
                    x_diff = abs(self.x_coor - Universal_array[i][j].X_coor)**2
                    y_diff = abs(self.y_coor - Universal_array[i][j].Y_coor)**2
                    euclidean = x_diff + y_diff
                    if(min_distance >= euclidean):
                        min_distance = euclidean
                        i_temp = i
                        j_temp = j

            x_diff = abs(
                self.x_coor - Universal_array[i_temp][j_temp].X_coor)**2
            y_diff = abs(
                self.y_coor - Universal_array[i_temp][j_temp].Y_coor)**2

            if((x_diff == 1 or y_diff == 1) or (x_diff == 1 or y_diff == 0) or (x_diff == 0 or y_diff == 0) or (x_diff == 0 or y_diff == 1)):
                self.attack(array, pseudo_array)

            if(self.x_coor > Universal_array[i_temp][j_temp].X_coor and self.y_coor == Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor-1][self.y_coor] == ' ' or pseudo_array[self.x_coor-1][self.y_coor] == 'B' or pseudo_array[self.x_coor-1][self.y_coor] == 'K')):
                self.x_coor -= 1
                self.last_move = 'w'
                array[old_x][old_y] = " "
                pseudo_array[old_x][old_y] = " "
                array[self.x_coor][self.y_coor] = self.color + \
                    "B" + Style.RESET_ALL
                pseudo_array[self.x_coor][self.y_coor] = "B"
            elif(self.x_coor < Universal_array[i_temp][j_temp].X_coor and self.y_coor == Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor+1][self.y_coor] == ' ' or pseudo_array[self.x_coor+1][self.y_coor] == 'B' or pseudo_array[self.x_coor+1][self.y_coor] == 'K')):
                self.x_coor += 1
                self.last_move = 's'
                array[old_x][old_y] = " "
                pseudo_array[old_x][old_y] = " "
                array[self.x_coor][self.y_coor] = self.color + \
                    "B" + Style.RESET_ALL
                pseudo_array[self.x_coor][self.y_coor] = "B"
            elif(self.x_coor == Universal_array[i_temp][j_temp].X_coor and self.y_coor > Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor][self.y_coor-1] == ' ' or pseudo_array[self.x_coor][self.y_coor-1] == 'B' or pseudo_array[self.x_coor][self.y_coor-1] == 'K')):
                self.y_coor -= 1
                self.last_move = 'a'
                array[old_x][old_y] = " "
                pseudo_array[old_x][old_y] = " "
                array[self.x_coor][self.y_coor] = self.color + \
                    "B" + Style.RESET_ALL
                pseudo_array[self.x_coor][self.y_coor] = "B"
            elif(self.x_coor == Universal_array[i_temp][j_temp].X_coor and self.y_coor < Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor][self.y_coor+1] == ' ' or pseudo_array[self.x_coor][self.y_coor+1] == 'B' or pseudo_array[self.x_coor][self.y_coor+1] == 'K')):
                self.y_coor += 1
                self.last_move = 'd'
                array[old_x][old_y] = " "
                pseudo_array[old_x][old_y] = " "
                array[self.x_coor][self.y_coor] = self.color + \
                    "B" + Style.RESET_ALL
                pseudo_array[self.x_coor][self.y_coor] = "B"
            elif(self.x_coor > Universal_array[i_temp][j_temp].X_coor and self.y_coor > Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor-1][self.y_coor-1] == ' ' or pseudo_array[self.x_coor-1][self.y_coor-1] == 'B' or pseudo_array[self.x_coor-1][self.y_coor-1] == 'K')):
                self.x_coor -= 1
                self.y_coor -= 1
                self.last_move = '#'
                array[old_x][old_y] = " "
                pseudo_array[old_x][old_y] = " "
                array[self.x_coor][self.y_coor] = self.color + \
                    "B" + Style.RESET_ALL
                pseudo_array[self.x_coor][self.y_coor] = "B"
            elif(self.x_coor > Universal_array[i_temp][j_temp].X_coor and self.y_coor < Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor-1][self.y_coor+1] == ' ' or pseudo_array[self.x_coor-1][self.y_coor+1] == 'B' or pseudo_array[self.x_coor-1][self.y_coor+1] == 'K')):
                self.x_coor -= 1
                self.y_coor += 1
                self.last_move = '#'
                array[old_x][old_y] = " "
                pseudo_array[old_x][old_y] = " "
                array[self.x_coor][self.y_coor] = self.color + \
                    "B" + Style.RESET_ALL
                pseudo_array[self.x_coor][self.y_coor] = "B"
            elif(self.x_coor < Universal_array[i_temp][j_temp].X_coor and self.y_coor > Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor+1][self.y_coor-1] == ' ' or pseudo_array[self.x_coor+1][self.y_coor-1] == 'B' or pseudo_array[self.x_coor+1][self.y_coor-1] == 'K')):
                self.x_coor += 1
                self.y_coor -= 1
                self.last_move = '#'
                array[old_x][old_y] = " "
                pseudo_array[old_x][old_y] = " "
                array[self.x_coor][self.y_coor] = self.color + \
                    "B" + Style.RESET_ALL
                pseudo_array[self.x_coor][self.y_coor] = "B"
            elif(self.x_coor < Universal_array[i_temp][j_temp].X_coor and self.y_coor < Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor+1][self.y_coor+1] == ' ' or pseudo_array[self.x_coor+1][self.y_coor+1] == 'B' or pseudo_array[self.x_coor+1][self.y_coor+1] == 'K')):
                self.x_coor += 1
                self.y_coor += 1
                self.last_move = '#'
                array[old_x][old_y] = " "
                pseudo_array[old_x][old_y] = " "
                array[self.x_coor][self.y_coor] = self.color + \
                    "B" + Style.RESET_ALL
                pseudo_array[self.x_coor][self.y_coor] = "B"

    def attack(self, array, pseudo_array):
        curr_X = self.x_coor
        curr_Y = self.y_coor

        if(self.health > 0):
            if(pseudo_array[curr_X-1][curr_Y] != ' ' and pseudo_array[curr_X-1][curr_Y] != 'K' and pseudo_array[curr_X-1][curr_Y] != 'B'):
                code = pseudo_array[curr_X-1][curr_Y]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power,
                                      array, pseudo_array)
            elif(pseudo_array[curr_X][curr_Y-1] != ' ' and pseudo_array[curr_X][curr_Y-1] != 'K' and pseudo_array[curr_X][curr_Y-1] != 'B'):
                code = pseudo_array[curr_X][curr_Y-1]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power,
                                      array, pseudo_array)
            elif(pseudo_array[curr_X+1][curr_Y] != ' ' and pseudo_array[curr_X+1][curr_Y] != 'K' and pseudo_array[curr_X+1][curr_Y] != 'B'):
                code = pseudo_array[curr_X+1][curr_Y]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power,
                                      array, pseudo_array)
            elif(pseudo_array[curr_X][curr_Y+1] != ' ' and pseudo_array[curr_X][curr_Y+1] != 'K' and pseudo_array[curr_X][curr_Y+1] != 'B'):
                code = pseudo_array[curr_X][curr_Y+1]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power,
                                      array, pseudo_array)
            elif(pseudo_array[curr_X-1][curr_Y-1] != ' ' and pseudo_array[curr_X-1][curr_Y-1] != 'K' and pseudo_array[curr_X-1][curr_Y-1] != 'B'):
                code = pseudo_array[curr_X-1][curr_Y-1]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power,
                                      array, pseudo_array)
            elif(pseudo_array[curr_X+1][curr_Y-1] != ' ' and pseudo_array[curr_X+1][curr_Y-1] != 'K' and pseudo_array[curr_X+1][curr_Y-1] != 'B'):
                code = pseudo_array[curr_X+1][curr_Y-1]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power,
                                      array, pseudo_array)
            elif(pseudo_array[curr_X-1][curr_Y+1] != ' ' and pseudo_array[curr_X-1][curr_Y+1] != 'K' and pseudo_array[curr_X-1][curr_Y+1] != 'B'):
                code = pseudo_array[curr_X-1][curr_Y+1]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power,
                                      array, pseudo_array)
            elif(pseudo_array[curr_X+1][curr_Y+1] != ' ' and pseudo_array[curr_X+1][curr_Y+1] != 'K' and pseudo_array[curr_X+1][curr_Y+1] != 'B'):
                code = pseudo_array[curr_X+1][curr_Y+1]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power,
                                      array, pseudo_array)

            else:
                return

    def health_bar(self, array, pseudo_array):
        health = self.health
        if self.health <= 0:
            old_X = self.x_coor
            old_Y = self.y_coor
            array[old_X][old_Y] = ' '
            pseudo_array[old_X][old_Y] = ' '
            self.x_coor = -1
            self.y_coor = -1
            self.attack_power = 0

        else:
            if self.health >= 0.5*gv.max_health_barbarians:
                self.color = Back.GREEN
            elif self.health >= 0.2*gv.max_health_barbarians:
                self.color = Back.YELLOW
            elif self.health > 0:
                self.color = Back.RED

            array[self.x_coor][self.y_coor] = self.color + \
                "B" + Style.RESET_ALL
            pseudo_array[self.x_coor][self.y_coor] = self.color + \
                "B" + Style.RESET_ALL


class Archers(Character):
    def __init__(self, x_coor, y_coor, array, pseudo_array, archer_count):
        self.type = "Archers"
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.color = Back.GREEN
        array[self.x_coor][self.y_coor] = self.color + "A" + Style.RESET_ALL
        pseudo_array[self.x_coor][self.y_coor] = "A"
        self.health = gv.max_health_archers
        self.last_move = " "
        self.attack_power = gv.attack_power_archers
        self.barbarian_id = archer_count
        self.movement_speed = 1

    def move(self, array, pseudo_array, Universal_array):
        # if any building except walls is in 3 tile range, dont move
        old_x = self.x_coor
        old_y = self.y_coor

        attacked = False

        if(self.health>0):

            temp_x = self.x_coor
            temp_y = self.y_coor
            
            if(self.last_move == "w" or self.last_move == "#"):
                temp_x = self.x_coor - 1
                temp_y = self.y_coor 
            elif(self.last_move == "s" or self.last_move == "#"):
                temp_x = self.x_coor + 1
                temp_y = self.y_coor
            elif(self.last_move == "a" or self.last_move == "#"):
                temp_y = self.y_coor - 1
                temp_x = self.x_coor
            elif(self.last_move == "d" or self.last_move == "#"):
                temp_y = self.y_coor + 1
                temp_x = self.x_coor
            
            # find wall with temp_x and temp_y coordinates
            for i in range(len(wall)):
                if(wall[i].X_coor == temp_x and wall[i].Y_coor == temp_y):
                    wall[i].damage(self.attack_power, array, pseudo_array)
                    attacked = True
                    break 

            else: 
            # now check if there is no building in range
                for i in range(3):
                    for j in Universal_array[i]:
                        # check if its under range
                        dist = ((self.x_coor-j.X_coor)**2 + (self.y_coor-j.Y_coor)**2)**0.5
                        if(dist<=8):
                            j.damage(self.attack_power, array, pseudo_array)
                            attacked = True
                

            if(attacked == False):
                # move
                min_distance = 10000
                i_temp, j_temp = 0, 0
                for i in range(3):
                    for j in range(len(Universal_array[i])):
                        x_diff = abs(self.x_coor - Universal_array[i][j].X_coor)**2
                        y_diff = abs(self.y_coor - Universal_array[i][j].Y_coor)**2
                        euclidean = x_diff + y_diff
                        if(min_distance >= euclidean):
                            min_distance = euclidean
                            i_temp = i
                            j_temp = j

                x_diff = abs(
                    self.x_coor - Universal_array[i_temp][j_temp].X_coor)**2
                y_diff = abs(
                    self.y_coor - Universal_array[i_temp][j_temp].Y_coor)**2

                if((x_diff == 1 or y_diff == 1) or (x_diff == 1 or y_diff == 0) or (x_diff == 0 or y_diff == 0) or (x_diff == 0 or y_diff == 1)):
                    self.attack(array, pseudo_array)

                if(self.x_coor > Universal_array[i_temp][j_temp].X_coor and self.y_coor == Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor-1][self.y_coor] == ' ' or pseudo_array[self.x_coor-1][self.y_coor] == 'B' or pseudo_array[self.x_coor-1][self.y_coor] == 'K')):
                    self.x_coor -= 1
                    self.last_move = 'w'
                    array[old_x][old_y] = " "
                    pseudo_array[old_x][old_y] = " "
                    array[self.x_coor][self.y_coor] = self.color + \
                        "A" + Style.RESET_ALL
                    pseudo_array[self.x_coor][self.y_coor] = "A"
                elif(self.x_coor < Universal_array[i_temp][j_temp].X_coor and self.y_coor == Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor+1][self.y_coor] == ' ' or pseudo_array[self.x_coor+1][self.y_coor] == 'B' or pseudo_array[self.x_coor+1][self.y_coor] == 'K')):
                    self.x_coor += 1
                    self.last_move = 's'
                    array[old_x][old_y] = " "
                    pseudo_array[old_x][old_y] = " "
                    array[self.x_coor][self.y_coor] = self.color + \
                        "A" + Style.RESET_ALL
                    pseudo_array[self.x_coor][self.y_coor] = "A"
                elif(self.x_coor == Universal_array[i_temp][j_temp].X_coor and self.y_coor > Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor][self.y_coor-1] == ' ' or pseudo_array[self.x_coor][self.y_coor-1] == 'B' or pseudo_array[self.x_coor][self.y_coor-1] == 'K')):
                    self.y_coor -= 1
                    self.last_move = 'a'
                    array[old_x][old_y] = " "
                    pseudo_array[old_x][old_y] = " "
                    array[self.x_coor][self.y_coor] = self.color + \
                        "A" + Style.RESET_ALL
                    pseudo_array[self.x_coor][self.y_coor] = "A"
                elif(self.x_coor == Universal_array[i_temp][j_temp].X_coor and self.y_coor < Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor][self.y_coor+1] == ' ' or pseudo_array[self.x_coor][self.y_coor+1] == 'B' or pseudo_array[self.x_coor][self.y_coor+1] == 'K')):
                    self.y_coor += 1
                    self.last_move = 'd'
                    array[old_x][old_y] = " "
                    pseudo_array[old_x][old_y] = " "
                    array[self.x_coor][self.y_coor] = self.color + \
                        "A" + Style.RESET_ALL
                    pseudo_array[self.x_coor][self.y_coor] = "A"
                elif(self.x_coor > Universal_array[i_temp][j_temp].X_coor and self.y_coor > Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor-1][self.y_coor-1] == ' ' or pseudo_array[self.x_coor-1][self.y_coor-1] == 'B' or pseudo_array[self.x_coor-1][self.y_coor-1] == 'K')):
                    self.x_coor -= 1
                    self.y_coor -= 1
                    self.last_move = '#'
                    array[old_x][old_y] = " "
                    pseudo_array[old_x][old_y] = " "
                    array[self.x_coor][self.y_coor] = self.color + \
                        "A" + Style.RESET_ALL
                    pseudo_array[self.x_coor][self.y_coor] = "A"
                elif(self.x_coor > Universal_array[i_temp][j_temp].X_coor and self.y_coor < Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor-1][self.y_coor+1] == ' ' or pseudo_array[self.x_coor-1][self.y_coor+1] == 'B' or pseudo_array[self.x_coor-1][self.y_coor+1] == 'K')):
                    self.x_coor -= 1
                    self.y_coor += 1
                    self.last_move = '#'
                    array[old_x][old_y] = " "
                    pseudo_array[old_x][old_y] = " "
                    array[self.x_coor][self.y_coor] = self.color + \
                        "A" + Style.RESET_ALL
                    pseudo_array[self.x_coor][self.y_coor] = "A"
                elif(self.x_coor < Universal_array[i_temp][j_temp].X_coor and self.y_coor > Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor+1][self.y_coor-1] == ' ' or pseudo_array[self.x_coor+1][self.y_coor-1] == 'B' or pseudo_array[self.x_coor+1][self.y_coor-1] == 'K')):
                    self.x_coor += 1
                    self.y_coor -= 1
                    self.last_move = '#'
                    array[old_x][old_y] = " "
                    pseudo_array[old_x][old_y] = " "
                    array[self.x_coor][self.y_coor] = self.color + \
                        "A" + Style.RESET_ALL
                    pseudo_array[self.x_coor][self.y_coor] = "A"
                elif(self.x_coor < Universal_array[i_temp][j_temp].X_coor and self.y_coor < Universal_array[i_temp][j_temp].Y_coor and (pseudo_array[self.x_coor+1][self.y_coor+1] == ' ' or pseudo_array[self.x_coor+1][self.y_coor+1] == 'B' or pseudo_array[self.x_coor+1][self.y_coor+1] == 'K')):
                    self.x_coor += 1
                    self.y_coor += 1
                    self.last_move = '#'
                    array[old_x][old_y] = " "
                    pseudo_array[old_x][old_y] = " "
                    array[self.x_coor][self.y_coor] = self.color + \
                        "A" + Style.RESET_ALL
                    pseudo_array[self.x_coor][self.y_coor] = "A"


                        

    def health_bar(self, array, pseudo_array):
        health = self.health
        if self.health <= 0:
            old_X = self.x_coor
            old_Y = self.y_coor
            array[old_X][old_Y] = ' '
            pseudo_array[old_X][old_Y] = ' '
            self.x_coor = -1
            self.y_coor = -1
            self.attack_power = 0

        else:
            if self.health >= 0.5*gv.max_health_barbarians:
                self.color = Back.GREEN
            elif self.health >= 0.2*gv.max_health_barbarians:
                self.color = Back.YELLOW
            elif self.health > 0:
                self.color = Back.RED

            array[self.x_coor][self.y_coor] = self.color + \
                "A" + Style.RESET_ALL
            pseudo_array[self.x_coor][self.y_coor] = self.color + \
                "A" + Style.RESET_ALL





class Balloon(Character):
    pass

