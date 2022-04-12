import time
import os
import src.global_variable as gv
import src.building as b
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


class Character:

    def __init__(self):
        self.movement_speed = 1

    def move(self, direction, array, pseudo_array):
        old_x = self.x_coor
        old_y = self.y_coor

        if self.type == "king" or self.type == "Archer_Queen":
            if direction == "w":
                if(self.x_coor > 0):
                    if(array[self.x_coor-1][self.y_coor] != " "):
                        array[self.x_coor][self.y_coor] = self.char
                    else:
                        self.x_coor -= 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = self.char
                        pseudo_array[self.x_coor][self.y_coor] = self.char

                self.last_move = "w"
            elif direction == "s":
                if(self.x_coor < gv.m-1):
                    if(array[self.x_coor+1][self.y_coor] != " "):
                        array[self.x_coor][self.y_coor] = self.char
                    else:
                        self.x_coor += 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = self.char
                        pseudo_array[self.x_coor][self.y_coor] = self.char

                self.last_move = "s"
            elif direction == "a":
                if(self.y_coor > 0):
                    if(array[self.x_coor][self.y_coor-1] != " "):
                        array[self.x_coor][self.y_coor] = self.char
                    else:
                        self.y_coor -= 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = self.char
                        pseudo_array[self.x_coor][self.y_coor] = self.char

                self.last_move = "a"
            elif direction == "d":
                if(self.y_coor < gv.n-1):
                    if(array[self.x_coor][self.y_coor+1] != " "):
                        array[self.x_coor][self.y_coor] = self.char
                    else:
                        self.y_coor += 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = self.char
                        pseudo_array[self.x_coor][self.y_coor] = self.char

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

    def attack(self, array, pseudo_array, Universal_array):
        # print(self.x_coor, self.y_coor)
        curr_X = self.x_coor
        curr_Y = self.y_coor
        if self.last_move == "w":
            # print("we can attack")
            if(pseudo_array[curr_X-1][curr_Y] != ' '):
                code = pseudo_array[curr_X-1][curr_Y]
                # parse code into letter and number
                if code[0] == 'T':
                    Universal_array[0][0].damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    Universal_array[1][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    Universal_array[2][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'Y':
                    code = code[1:len(code):1]
                    Universal_array[3][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    Universal_array[4][code].damage(self.attack_power, array, pseudo_array)

        elif self.last_move == "s":
            if(pseudo_array[curr_X+1][curr_Y] != ' '):
                code = pseudo_array[curr_X+1][curr_Y]
                # parse code into letter and number
                if code[0] == 'T':
                    Universal_array[0][0].damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    Universal_array[1][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    Universal_array[2][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'Y':
                    code = code[1:len(code):1]
                    Universal_array[3][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    Universal_array[4][code].damage(self.attack_power, array, pseudo_array)

        elif self.last_move == "a":
            if(pseudo_array[curr_X][curr_Y-1] != ' '):
                code = pseudo_array[curr_X][curr_Y-1]
                # parse code into letter and number
                if code[0] == 'T':
                    Universal_array[0][0].damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    Universal_array[1][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    Universal_array[2][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'Y':
                    code = code[1:len(code):1]
                    Universal_array[3][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    Universal_array[4][code].damage(self.attack_power, array, pseudo_array)

        elif self.last_move == "d":
            if(pseudo_array[curr_X][curr_Y+1] != ' '):
                code = pseudo_array[curr_X][curr_Y+1]
                # parse code into letter and number
                if code[0] == 'T':
                    Universal_array[0][0].damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    Universal_array[1][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    Universal_array[2][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'Y':
                    code = code[1:len(code):1]
                    Universal_array[3][int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    Universal_array[4][code].damage(self.attack_power, array, pseudo_array)

    def leviathan(self, array, pseudo_array, Universal_array):
        for i in range(5):
            for j in Universal_array[i]:
                if((self.x_coor - j.X_coor)**2 + (self.y_coor - j.Y_coor)**2 <= 25):
                    j.damage(self.attack_power, array, pseudo_array)


class king(Character):
    def __init__(self, x_coor, y_coor, array, pseudo_array):
        self.type = "king"
        self.char = "K"
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
        self.char = "A"
        self.x_coor = x_coor
        self.y_coor = y_coor
        array[self.x_coor][self.y_coor] = "A"
        pseudo_array[self.x_coor][self.y_coor] = "A"
        self.health = gv.max_health_archer_queen
        self.last_move = " "
        self.attack_power = gv.attack_power_archer_queen
        self.movement_speed = 1

    def attack(self, array, pseudo_array, Universal_array):
        curr_X = self.x_coor
        curr_Y = self.y_coor
        if self.last_move == "w":
            # queen facing north
            # centre of volley attack = (curr_x - 8, curr_y)
            for i in range(5):
                for j in Universal_array[i]:
                    man_abs_x = abs(self.x_coor - 8 - j.X_coor)
                    man_abs_y = abs(self.y_coor - j.Y_coor)

                    if(man_abs_x <= 5/2 and man_abs_y <= 5/2):
                        j.damage(self.attack_power, array, pseudo_array)

        if self.last_move == "s":
            # queen facing south
            # centre of volley attack = (curr_x + 8, curr_y)
            for i in range(5):
                for j in Universal_array[i]:
                    man_abs_x = abs(self.x_coor + 8 - j.X_coor)
                    man_abs_y = abs(self.y_coor - j.Y_coor)

                    if(man_abs_x <= 5/2 and man_abs_y <= 5/2):
                        j.damage(self.attack_power, array, pseudo_array)

        if self.last_move == "a":
            # queen facing West
            # centre of volley attack = (curr_x, curr_y - 8)
            for i in range(5):
                for j in Universal_array[i]:
                    man_abs_x = abs(self.x_coor - j.X_coor)
                    man_abs_y = abs(self.y_coor - 8 - j.Y_coor)

                    if(man_abs_x <= 5/2 and man_abs_y <= 5/2):
                        j.damage(self.attack_power, array, pseudo_array)

        if self.last_move == "d":
            # queen facing north
            # centre of volley attack = (curr_x, curr_y + 8)
            for i in range(5):
                for j in Universal_array[i]:
                    man_abs_x = abs(self.x_coor - j.X_coor)
                    man_abs_y = abs(self.y_coor - j.Y_coor + 8)

                    if(man_abs_x <= 5/2 and man_abs_y <= 5/2):
                        j.damage(self.attack_power, array, pseudo_array)

    def leviathan(self, array, pseudo_array, Universal_array):
        if self.last_move == "w":
            # queen facing north
            # centre of volley attack = (curr_x - 8, curr_y)
            for i in range(5):
                for j in Universal_array[i]:
                    man_abs_x = abs(self.x_coor - 16 - j.X_coor)
                    man_abs_y = abs(self.y_coor - j.Y_coor)

                    if(man_abs_x <= 9/2 and man_abs_y <= 9/2):
                        j.damage(self.attack_power, array, pseudo_array)

        if self.last_move == "s":
            # queen facing south
            # centre of volley attack = (curr_x + 8, curr_y)
            for i in range(5):
                for j in Universal_array[i]:
                    man_abs_x = abs(self.x_coor + 16 - j.X_coor)
                    man_abs_y = abs(self.y_coor - j.Y_coor)

                    if(man_abs_x <= 9/2 and man_abs_y <= 9/2):
                        j.damage(self.attack_power, array, pseudo_array)

        if self.last_move == "a":
            # queen facing West
            # centre of volley attack = (curr_x, curr_y - 8)
            for i in range(5):
                for j in Universal_array[i]:
                    man_abs_x = abs(self.x_coor - j.X_coor)
                    man_abs_y = abs(self.y_coor - 16 - j.Y_coor)

                    if(man_abs_x <= 9/2 and man_abs_y <= 9/2):
                        j.damage(self.attack_power, array, pseudo_array)

        if self.last_move == "d":
            # queen facing north
            # centre of volley attack = (curr_x, curr_y + 8)
            for i in range(5):
                for j in Universal_array[i]:
                    man_abs_x = abs(self.x_coor - j.X_coor)
                    man_abs_y = abs(self.y_coor - j.Y_coor + 16)

                    if(man_abs_x <= 9/2 and man_abs_y <= 9/2):
                        j.damage(self.attack_power, array, pseudo_array)


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
        self.id = barbarian_count
        self.movement_speed = 1

    def bar_move(self, array, pseudo_array, Universal_array):
        old_x = self.x_coor
        old_y = self.y_coor

        if(self.health > 0):
            attacked = False
            min_distance = 10000
            obj = Universal_array[0][0]
            for i in range(4):
                for j in Universal_array[i]:
                    dist = ((self.x_coor - j.X_coor)**2 +
                            (self.y_coor - j.Y_coor)**2)**0.5
                    if(dist < min_distance):
                        min_distance = dist
                        obj = j

            man_abs_x = abs(self.x_coor - obj.X_coor)
            man_abs_y = abs(self.y_coor - obj.Y_coor)

            if((man_abs_x == 1 and man_abs_y == 0) or (man_abs_y == 1 and man_abs_x == 0) or (man_abs_x == 1 and man_abs_y == 1)):
                obj.damage(self.attack_power, array, pseudo_array)
                attacked = True

            if(attacked == False):
                # move towards the nearest building other than wall
                if(self.x_coor == obj.X_coor):
                    if(self.y_coor > obj.Y_coor):
                        self.y_coor -= 1
                        self.last_move = 'a'
                    else:
                        self.y_coor += 1
                        self.last_move = 'd'
                elif(self.y_coor == obj.Y_coor):
                    if(self.x_coor > obj.X_coor):
                        self.x_coor -= 1
                        self.last_move = 'w'
                    else:
                        self.x_coor += 1
                        self.last_move = 's'
                elif(self.x_coor > obj.X_coor):
                    if(self.y_coor > obj.Y_coor):
                        self.x_coor -= 1
                        self.y_coor -= 1
                        self.last_move = 'q'
                    else:
                        self.x_coor -= 1
                        self.y_coor += 1
                        self.last_move = 'e'
                elif(self.x_coor < obj.X_coor):
                    if(self.y_coor > obj.Y_coor):
                        self.x_coor += 1
                        self.y_coor -= 1
                        self.last_move = 'z'
                    else:
                        self.x_coor += 1
                        self.y_coor += 1
                        self.last_move = 'c'

                if(pseudo_array[self.x_coor][self.y_coor] == ' '):
                    pseudo_array[self.x_coor][self.y_coor] = "B"
                    array[self.x_coor][self.y_coor] = self.color + \
                        "B" + Style.RESET_ALL
                    array[old_x][old_y] = " "
                    pseudo_array[old_x][old_y] = " "

                else:
                    code = pseudo_array[self.x_coor][self.y_coor]
                    if(code[0] == 'W'):
                        self.x_coor = old_x
                        self.y_coor = old_y
                        code = code[1:len(code):1]
                        code = int(code)
                        Universal_array[4][code].damage(self.attack_power, array, pseudo_array)
                    else:
                        pseudo_array[old_x][old_y] = " "
                        array[old_x][old_y] = " "

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
            pseudo_array[self.x_coor][self.y_coor] = "B"


class Archers(Character):
    def __init__(self, x_coor, y_coor, array, pseudo_array, archer_count):
        self.type = "Archers"
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.char = "V"
        self.color = Back.GREEN
        array[self.x_coor][self.y_coor] = self.color + \
            self.char + Style.RESET_ALL
        pseudo_array[self.x_coor][self.y_coor] = self.char
        self.health = gv.max_health_archers
        self.last_move = " "
        self.attack_power = gv.attack_power_archers
        self.id = archer_count
        self.movement_speed = 1

    def move(self, array, pseudo_array, Universal_array):
        # if any building except walls is in 3 tile range, dont move
        old_x = self.x_coor
        old_y = self.y_coor

        attacked = False

        if(self.health > 0):
            if(attacked == False):
                # check if there is any building in range
                for i in range(4):
                    for j in Universal_array[i]:
                        # check if its under range
                        dist = ((self.x_coor-j.X_coor)**2 +
                                (self.y_coor-j.Y_coor)**2)**0.5
                        if(dist <= 4):
                            j.damage(self.attack_power, array, pseudo_array)
                            attacked = True
                            break
                    if(attacked == True):
                        break

            if(attacked == False):

                temp_x = self.x_coor
                temp_y = self.y_coor

                if(self.last_move == "w"):
                    temp_x = self.x_coor - 1
                    temp_y = self.y_coor
                elif(self.last_move == "s"):
                    temp_x = self.x_coor + 1
                    temp_y = self.y_coor
                elif(self.last_move == "a"):
                    temp_y = self.y_coor - 1
                    temp_x = self.x_coor
                elif(self.last_move == "d"):
                    temp_y = self.y_coor + 1
                    temp_x = self.x_coor
                elif(self.last_move == "q"):
                    temp_x = self.x_coor - 1
                    temp_y = self.y_coor - 1
                elif(self.last_move == "e"):
                    temp_x = self.x_coor - 1
                    temp_y = self.y_coor + 1
                elif(self.last_move == "z"):
                    temp_x = self.x_coor + 1
                    temp_y = self.y_coor - 1
                elif(self.last_move == "c"):
                    temp_x = self.x_coor + 1
                    temp_y = self.y_coor + 1

                # find wall with temp_x and temp_y coordinates
                for i in range(len(Universal_array[4])):
                    if(Universal_array[4][i].X_coor == temp_x and Universal_array[4][i].Y_coor == temp_y):
                        Universal_array[4][i].damage(self.attack_power, array, pseudo_array)
                        attacked = True
                        break

            if(attacked == False):
                # move
                obj = Universal_array[0][0]
                min_distance = 10000
                for i in range(4):
                    for j in Universal_array[i]:
                        dist = ((self.x_coor-j.X_coor)**2 +
                                (self.y_coor-j.Y_coor)**2)**0.5
                        if(dist < min_distance):
                            obj = j
                            min_distance = dist

                if(self.x_coor == obj.X_coor):
                    if(self.y_coor < obj.Y_coor):
                        self.last_move = "d"
                        self.y_coor += 1
                    else:
                        self.last_move = "a"
                        self.y_coor -= 1

                elif(self.y_coor == obj.Y_coor):
                    if(self.x_coor < obj.X_coor):
                        self.last_move = "s"
                        self.x_coor += 1
                    else:
                        self.last_move = "w"
                        self.x_coor -= 1

                elif(self.x_coor > obj.X_coor):
                    if(self.y_coor < obj.Y_coor):
                        self.last_move = "e"
                        self.x_coor -= 1
                        self.y_coor += 1
                    else:
                        self.last_move = "q"
                        self.x_coor -= 1
                        self.y_coor -= 1

                elif(self.x_coor < obj.X_coor):
                    if(self.y_coor < obj.Y_coor):
                        self.last_move = "c"
                        self.x_coor += 1
                        self.y_coor += 1
                    else:
                        self.last_move = "z"
                        self.x_coor += 1
                        self.y_coor -= 1

                if(pseudo_array[self.x_coor][self.y_coor] == ' '):
                    array[old_x][old_y] = ' '
                    pseudo_array[old_x][old_y] = ' '
                    array[self.x_coor][self.y_coor] = self.color + \
                        self.char + Style.RESET_ALL
                    pseudo_array[self.x_coor][self.y_coor] = self.char

                else:
                    code = pseudo_array[self.x_coor][self.y_coor]
                    if(code == 'T' or code == 'H' or code == 'C' or code == 'Y' or code == 'W'):
                        self.x_coor = old_x
                        self.y_coor = old_y

                    else:
                        pseudo_array[old_x][old_y] = ' '
                        array[old_x][old_y] = ' '

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
                self.char + Style.RESET_ALL
            pseudo_array[self.x_coor][self.y_coor] = self.char


class Balloons(Character):

    def __init__(self, x_coor, y_coor, array, pseudo_array, balloon_count):
        self.type = "Balloons"
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.char = "O"
        self.color = Back.GREEN
        array[self.x_coor][self.y_coor] = self.color + "O" + Style.RESET_ALL
        pseudo_array[self.x_coor][self.y_coor] = "O"
        self.health = gv.max_health_balloons
        self.last_move = " "
        self.attack_power = gv.attack_power_balloons
        self.id = balloon_count
        self.movement_speed = 1

    def move(self, array, pseudo_array, Universal_array):
        old_X = self.x_coor
        old_Y = self.y_coor
        if self.health > 0:

            defbuil_present = False
            attacked = False

            # check if there are any defensive buildings left
            for i in range(2, 4):
                for j in Universal_array[i]:
                    if(j.health > 0):
                        defbuil_present = True
                        break
                if(defbuil_present):
                    break

            if(defbuil_present == True and attacked == False):
                # find nearest defensive building
                min_dist = 10000
                obj = Universal_array[2][0]
                for i in range(2, 4):
                    for j in Universal_array[i]:
                        dist = ((self.x_coor - j.X_coor)**2 +
                                (self.y_coor - j.Y_coor)**2)**0.5
                        if dist < min_dist:
                            min_dist = dist
                            obj = j

                dist = ((self.x_coor - obj.X_coor)**2 +
                        (self.y_coor - obj.Y_coor)**2)**0.5
                if(dist < 1.5):
                    obj.damage(self.attack_power, array, pseudo_array)
                    attacked = True
                    return

                if(attacked == False):
                    # j is at min euclidean distance
                    # move towards it
                    if(self.x_coor == obj.X_coor):
                        if(self.y_coor > obj.Y_coor):
                            self.y_coor -= 1
                            self.last_move = 'a'

                        else:
                            self.y_coor += 1
                            self.last_move = 'd'

                    elif(self.y_coor == obj.Y_coor):
                        if(self.x_coor > obj.X_coor):
                            self.x_coor -= 1
                            self.last_move = 'w'

                        else:
                            self.x_coor += 1
                            self.last_move = 's'

                    elif(self.x_coor > obj.X_coor):
                        if(self.y_coor > obj.Y_coor):
                            self.x_coor -= 1
                            self.y_coor -= 1
                            self.last_move = 'q'

                        else:
                            self.x_coor -= 1
                            self.y_coor += 1
                            self.last_move = 'e'

                    elif(self.x_coor < obj.X_coor):
                        if(self.y_coor > obj.Y_coor):
                            self.x_coor += 1
                            self.y_coor -= 1
                            self.last_move = 'z'

                        else:
                            self.x_coor += 1
                            self.y_coor += 1
                            self.last_move = 'c'

                    # make changes accordingly
                    if(pseudo_array[old_X][old_Y] == 'O'):
                        array[old_X][old_Y] = " "
                        pseudo_array[old_X][old_Y] = " "
                    if(pseudo_array[self.x_coor][self.y_coor] == ' '):
                        array[self.x_coor][self.y_coor] = self.color + \
                            "O" + Style.RESET_ALL
                        pseudo_array[self.x_coor][self.y_coor] = "O"

            else:

                # find nearest building
                min_dist = 10000
                obj = Universal_array[0][0]
                for i in range(2):
                    for j in Universal_array[i]:
                        dist = ((self.x_coor - j.X_coor)**2 +
                                (self.y_coor - j.Y_coor)**2)**0.5
                        if dist < min_dist:
                            min_dist = dist
                            obj = j

                dist = ((self.x_coor - obj.X_coor)**2 +
                        (self.y_coor - obj.Y_coor)**2)**0.5
                if(dist < 1.5):
                    obj.damage(self.attack_power, array, pseudo_array)
                    attacked = True
                    return
                if(attacked == False):
                    # j is at min euclidean distance
                    # move towards it
                    if(self.x_coor == obj.X_coor):
                        if(self.y_coor > obj.Y_coor):
                            self.y_coor -= 1
                            self.last_move = 'a'

                        else:
                            self.y_coor += 1
                            self.last_move = 'd'

                    elif(self.y_coor == obj.Y_coor):
                        if(self.x_coor > obj.X_coor):
                            self.x_coor -= 1
                            self.last_move = 'w'

                        else:
                            self.x_coor += 1
                            self.last_move = 's'

                    elif(self.x_coor > obj.X_coor):
                        if(self.y_coor > obj.Y_coor):
                            self.x_coor -= 1
                            self.y_coor -= 1
                            self.last_move = 'q'

                        else:
                            self.x_coor -= 1
                            self.y_coor += 1
                            self.last_move = 'e'

                    elif(self.x_coor < obj.X_coor):
                        if(self.y_coor > obj.Y_coor):
                            self.x_coor += 1
                            self.y_coor -= 1
                            self.last_move = 'z'

                        else:
                            self.x_coor += 1
                            self.y_coor += 1
                            self.last_move = 'c'

                    # make changes accordingly
                    if(pseudo_array[old_X][old_Y] == 'O'):
                        array[old_X][old_Y] = " "
                        pseudo_array[old_X][old_Y] = " "
                    if(pseudo_array[self.x_coor][self.y_coor] == ' '):
                        array[self.x_coor][self.y_coor] = self.color + \
                            "O" + Style.RESET_ALL
                        pseudo_array[self.x_coor][self.y_coor] = "O"

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
            if self.health >= 0.5*gv.max_health_balloons:
                self.color = Back.GREEN
            elif self.health >= 0.2*gv.max_health_balloons:
                self.color = Back.YELLOW
            elif self.health > 0:
                self.color = Back.RED

            if(pseudo_array[self.x_coor][self.y_coor] == ' '):
                array[self.x_coor][self.y_coor] = self.color + \
                    "O" + Style.RESET_ALL
                pseudo_array[self.x_coor][self.y_coor] = "O"
