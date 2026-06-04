# Mysterious Island Treasure Hunt 

## Overview

Mysterious Island Treasure Hunt is a simple Python command-line adventure game where players search different rooms to find a hidden treasure. However, one room contains a ghost that instantly ends the game. Players must use logic and a limited number of lives to locate the treasure before it's too late.

## Features

* Random treasure room generation
* Random ghost room generation
* Limited lives system
* Interactive room selection
* Clue provided when only one life remains
* Win and lose conditions

## How to Play

1. Start the game.
2. A list of available rooms is displayed.
3. Enter the name of a room to explore.
4. Outcomes:

   * Find the treasure → You win.
   * Enter the ghost room → Game over.
   * Choose an empty room → Lose one life.
5. When only one life remains, a clue is revealed showing the first letter of the treasure room.
6. The game ends when the treasure is found, the ghost is encountered, or all lives are lost.

## Rooms Available

* Library
* Kitchen
* Living Room
* Attic
* Master Bedroom
* Storeroom

## Technologies Used

* Python 3
* Random Module
* Time Module

## Learning Concepts

This project demonstrates:

* Lists
* Loops
* Conditional Statements
* User Input Handling
* Randomization
* Basic Game Design
* Importing Python Modules

## Running the Program

```bash
python mysterious_island.py
```

## Example Gameplay

```text
----welcome to the mysterious island----

<- library
<- kitchen
<- living room
<- attic
<- master bedroom
<- storeroom

enter your room you want to enter: kitchen

lives left: 2
```

## Future Improvements

* Multiple levels
* More clues
* Score tracking
* Difficulty settings
* Colorful terminal interface
* Save and load game progress


