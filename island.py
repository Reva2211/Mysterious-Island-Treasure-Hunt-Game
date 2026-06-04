print("----welcome to the mysterious island----")
import random
import time
lives=3
rooms=['library','kitchen','living room','attic','master bedroom','storeroom']
treasure_room=random.choice(rooms)
ghost_room=random.choice(rooms)
print(treasure_room)
print(ghost_room)
while lives>0:
     time.sleep(1)
     for room in rooms:
         print("<-",room)
     room_user=input("enter your room you want to enter: ")
     if room_user not in rooms:
         print("invald name")
     elif room_user==treasure_room:
         print("lucky!you win")
         break
     elif room_user==ghost_room:
         print("alas!you entered into a ghost room")
         break
     else:
         lives-=1
         print("lives left:",lives)
         if lives==1:
            print("you still have 1 chance.the clue for for treasure room is ",treasure_room[0].upper())
if lives==0:
             print("you have lost")
             print("game over")
