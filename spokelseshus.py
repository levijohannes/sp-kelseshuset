# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:55:18 2023

@author: Levi
"""

# Haunted home 
from random import randint
print ('Haunted home')
feeling_brave = True
score = 0
while feeling_brave: 
    ghost_door = randint(1, 3)
    print ('You face 3 doors...')
    print('Behind one of the doors is a ghost.')
    print('Which door will you open?... :) ')
    door = input('1, 2, or 3?')
    door_num = int(door)
    if door_num == ghost_door:
        print('BOO!')
        feeling_brave = False
    else: 
        print('Phew not a ghost')
        print('You continue to the next room')
        score = score + 1
print('RUN!')
print('Game Over! You collected', score)