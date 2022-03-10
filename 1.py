# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def give_raise(self, percent):
#         self.salary = self.salary + (self.salary * percent)
#         return self.salary


# emp = []
# emp.append(Employee("John", 50000))
# emp.append(Employee("Mary", 60000))
# emp.append(Employee("Bob", 70000))

# emp[1].give_raise(0.1)
# print(emp[1].salary)


# grid = [[' ' for i in range(2)] for j in range(2)]
# grid[0][0] = "apple"
# grid[0][1] = "banana"
# grid[1][0] = "cherry"
# grid[1][1] = "durian"

# print(grid)


# for i in range(1,5):
#     print(i)

code = "a11"


code = code[1:len(code):1]
print(code)

import colorama
from colorama import Fore, Back, Style
from matplotlib import offsetbox
colorama.init(autoreset=True)
str = Fore.RED + "Hello World" + Style.RESET_ALL

print(str)

str = ' ' + Style.RESET_ALL
print(str)






