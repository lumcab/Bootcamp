from os import O_APPEND
from typing import Set


list = input("Introduce una muestra de números separados por comas: ")
list = list.split(',')
mySet = set(list)
print(sorted(mySet))