from base_classes.coordinates import Coordinates
from base_classes.door import Door
from base_classes.room import Room
from base_classes.item import Item
from base_classes.object_types import ObjectTypes

#print grid for map
def print_grid(area, unit):
    for _ in range(area):
        print(("+" + "- " * unit) * area + "+")
        for _ in range(unit):
            print(("|" + "  " * unit) * area + "|")
    print(("+" + "- " * unit) * area + "+")
    
# def print_grid(area, unit):
#     for _ in range(area):
#         print(("+" + "- " * unit) * area + "+")
#         for _ in range(unit):
#             print(("|" + "  " * unit) * area + "|")
#     print(("+" + "- " * unit) * area + "+")

# create rooms
testroom = Room("Kitchen",4,4)
testroom2 = Room("lounge",6,4)

# add objects to kitchen
testroom.add_object(Item("sword",ObjectTypes.ITEM,Coordinates(2,3)))
testroom.add_object(Item("feather",ObjectTypes.ITEM,Coordinates(1,1)))
testroom.add_object(Door(Coordinates(0,2), testroom2))

#add objects to lounge
testroom2.add_object(Door(Coordinates(0,2),testroom))


# print_grid(testroom.columns,2)

#show kitchen
for i in testroom.room:
    print(i)
    
print("")
print("")
print("")
    
#show lounge
for i in testroom2.room:
    print(i)