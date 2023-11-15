# -*- coding: utf-8 -*-
"""Tic Tac Toe.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I8pcWYDb3crlcU3Gxpie9onj1pkNEabE

# Notes:
for computer look for empty spot randomly grab a index
## Smart computer
look for optimal choices
same logic to block and win
"""
# %%
import numpy as np
import random

board = ["#","#","#","#","#","#","#","#","#"]

def check(board):
  if(board[0] == board[1] == board[2] != "#"):
    return False

  if(board[3] == board[4] == board[5] != "#"):
    return False

  if(board[6] == board[7] == board[8] != "#"):
    return False

  if(board[0] == board[3] == board[6] != "#"):
    return False

  if(board[1] == board[4] == board[7] != "#"):
    return False

  if(board[2] == board[5] == board[8] != "#"):
    return False

  if(board[0] == board[4] == board[8] != "#"):
    return False

  if(board[2] == board[4] == board[6] != "#"):
    return False

  return True

#player1 = input("please input your cordinates (x,y)")

def insert(board,marker):
  bad = True
  while(bad):
    player = input("please input your cordinates (x,y)")
    player = player.split(",")
    spot = 0

    if player[0] == "1":
      spot = spot + 3
    if player[0] == "2":
      spot = spot + 6
    spot = spot + int(player[1])
    if(board[spot] == "#"):
      bad = False

  board[spot] = marker

  return board

#insert(board,"O")

def play2():
  gaming = True
  board = ["#","#","#","#","#","#","#","#","#"]
  starting = random.randint(0,1)

  marker = "O"
  if(starting == 1):
    marker = "X"

  for x in range(0,9):
    print(marker, "move")
    board = insert(board,marker)
    gaming = check(board)

    if(gaming == False):
      break
    if(marker == "O"):
      marker = "X"
    elif(marker == "X"):
      marker = "O"

    print(board)

  if(gaming ==  False):
    print("winner",marker )
  else:
    print("tie")

#play2()

def getCPUinput(board):
  spots = []
  for x in range(len(board)):
    if(board[x] == "#"):
      spots.append(x)
  random_choice = random.choice(spots)
  return random_choice

def getPlayerinput(board):
  bad = True
  while(bad):
    player = input("please input your cordinates (x,y)")
    player = player.split(",")
    spot = 0

    if player[0] == "1":
      spot = spot + 3
    if player[0] == "2":
      spot = spot + 6
    spot = spot + int(player[1])
    if(board[spot] == "#"):
      bad = False
  return spot

def play1():
  gaming = True
  board = ["#","#","#","#","#","#","#","#","#"]
  starting = random.randint(0,1)

  marker = "O"
  if(starting == 1):
    marker = "X"

  for x in range(0,9):
    print(marker, "move")
    if(x % 2 == 0):
      choice = getPlayerinput(board)
    else:
      choice = getCPUinput(board)
    board[choice] = marker
    gaming = check(board)

    if(gaming == False):
      break

    if(marker == "O"):
      marker = "X"
    elif(marker == "X"):
      marker = "O"
    print(board)

  if(gaming ==  False):
    print("winner",marker )
  else:
    print("tie")

#play1()

def lookforspot(board,marker):
  print("this is my marker", marker)
  if(marker == "O"):
    oppositemarker = "X"
  elif(marker == "X"):
    oppositemarker = "O"

  for x in range(0,9,3):
    if(board[x] == board[x+2] == marker):
      if(board[x+1] == '#'):
        return x+1
    if(board[x] == board[x+1] == marker):
      if(board[x+2] == '#'):
        return x+2
    if(board[x+1] == board[x+2] == marker):
      if(board[x] == '#'):
        return x

  for x in range(0,3):
    if(board[x] == board[x+6] == marker):
      if(board[x+3] == '#'):
        return x+3
    if(board[x] == board[x+3] == marker):
      if(board[x+6] == '#'):
        return x+6
    if(board[x+3] == board[x+6] == marker):
      if(board[x] == '#'):
        return x

  if(board[0] == board[4] == marker):
    if(board[8] == '#'):
      return 8
  if(board[0] == board[8] == marker):
    if(board[4] == '#'):
      return 4
  if(board[8] == board[4] == marker):
    if(board[0] == '#'):
      return 0

  if(board[2] == board[4] == marker):
    if(board[6] == '#'):
      return 6
  if(board[2] == board[6] == marker):
    if(board[4] == '#'):
      return 4
  if(board[6] == board[4] == marker):
    if(board[2] == '#'):
      return 2

  print("blocking",oppositemarker)
  if(board[0] == board[4] == oppositemarker):
    if(board[8] == '#'):
      return 8
  if(board[0] == board[8] == oppositemarker):
    if(board[4] == '#'):
      return 4
  if(board[8] == board[4] == oppositemarker):
    if(board[0] == '#'):
      return 0

  if(board[2] == board[4] == oppositemarker):
    if(board[6] == '#'):
      return 6
  if(board[2] == board[6] == oppositemarker):
    if(board[4] == '#'):
      return 4
  if(board[6] == board[4] == oppositemarker):
    if(board[2] == '#'):
      return 2

  for x in range(0,9,3):
    if(board[x] == board[x+2] == oppositemarker):
      if(board[x+1] == '#'):
        return x+1
    if(board[x] == board[x+1] == oppositemarker):
      if(board[x+2] == '#'):
        return x+2
    if(board[x+1] == board[x+2] == oppositemarker):
      if(board[x] == '#'):
        return x

  for x in range(0,3):
    if(board[x] == board[x+6] == oppositemarker):
      if(board[x+3] == '#'):
        return x+3
    if(board[x] == board[x+3] == oppositemarker):
      if(board[x+6] == '#'):
        return x+6
    if(board[x+3] == board[x+6] == oppositemarker):
      if(board[x] == '#'):
        return x

  return 9

#boardsetup = ['X', '#', '#', 'X', 'X', 'O', 'X', 'O', 'X']
#print(lookforspot(boardsetup,'O'))

def showboard(board):
 print("|",board[0],"|",board[1],"|",board[2],"|\n|",board[3],"|",board[4],"|",board[5],"| \n|",board[6],"|",board[7],"|",board[8],"| \n")

def hardplay1():
  gaming = True
  board = ["#","#","#","#","#","#","#","#","#"]
  starting = random.randint(0,1)
  showboard(board)

  marker = "O"
  if(starting == 1):
    marker = "X"

  for x in range(0,9):
    print(marker, "move")
    if(x % 2 == 0):
      choice = getPlayerinput(board)
    else:
      print("ai cook")
      choice = lookforspot(board,marker)
      if(choice == 9):
        print("guess")
        choice = getCPUinput(board)
    board[choice] = marker
    gaming = check(board)

    if(gaming == False):
      break

    if(marker == "O"):
      marker = "X"
    elif(marker == "X"):
      marker = "O"
    showboard(board)

  if(gaming ==  False):
    showboard(board)
    print("winner",marker )
  else:
    print("tie")
    
# %%

#hardplay1()
play2()

