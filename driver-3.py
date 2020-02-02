# Driver for greedy robot finding the treasure by asking user for input

import sys
import greedyRobot


def getUniquePaths(robotX, robotY, treasureX, treasureY, direction):

    if treasureX == robotX and treasureY == robotY:
        pathList.append(direction)

    else:
        if treasureY > robotY:
            getUniquePaths(robotX, robotY + 1, treasureX, treasureY, direction + "N")
        if treasureX > robotX:
            getUniquePaths(robotX + 1, robotY, treasureX, treasureY, direction + "E")
        if treasureX < robotX:
            getUniquePaths(robotX - 1, robotY, treasureX, treasureY, direction + "W")
        if treasureY < robotY:
            getUniquePaths(robotX, robotY - 1, treasureX, treasureY, direction + "S")


robotPosX = int(sys.argv[1])
robotPosY = int(sys.argv[2])

treasurePosX = int(sys.argv[3])
treasurePosY = int(sys.argv[4])


robotPos = greedyRobot.Position(robotPosX, robotPosY)
treasurePos = greedyRobot.Position(treasurePosX, treasurePosY)
pathList = []

getUniquePaths(robotPosX, robotPosY, treasurePosX, treasurePosY, "")
for i in range(len(pathList)):
    print(pathList[i])
if len(pathList) == 1:
    print("total paths: 0")
else:
    print("total paths: " + str(len(pathList)))