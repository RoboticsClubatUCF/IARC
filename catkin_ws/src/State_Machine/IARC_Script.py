"""
IARC Lakitu State Machine
Robotics Club at UCF
Developer: Andrew Schroeder
Last updated: 2/1/2018
"""


#declare states
SYSTEM_BOOT = 0
HOVER = 1
MOVE_TO_START = 2
SEARCH_PATTERN = 3
TRACK_ROOMBA = 4
LAND_ON_ROOMBA = 5
LAND_IN_FRONT_ROOMBA = 6
AVOID = 7
RETURN_TO_GRID = 8
EXIT = 9

#declare global input variables
sonic1, sonic2, sonic3, sonic4, sonic5, sonic6, sonic7, sonic8, sonic9
#etc

#set state = startup state to begin
state = STARTUP

#start main loop
while state != EXIT:
    #get input

    #check for collision
    #check for outside grid
    
    if state == SYSTEM_BOOT:

    else if state == HOVER:

    else if state == MOVE_TO_START:

    else if state == SEARCH_PATTERN:

    else if state == TRACK_ROOMBA:

    else if state == LAND_ON_ROOMBA:

    else if state == LAND_IN_FRONT_ROOMBA:

    else if state == AVOID:

    else if state == RETURN_TO_GRID:

    else if state == EXIT:





