# This class represents a position made up of an x and y coordinate
class Position:

    def __init__(self, x = 0, y = 0):

            self.__x = x
            self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def __str__(self):
        result = "(" + str(self.getX()) + ", " + str(self.getY()) + ")"
        return result

# A class to represent a robot with a position on a coordinate plane
class Robot:

    def __init__(self, position):
        position = self.__position

    def getPosition(self):
        return self.__position

# A class to represent a treasure with a position on a coordinate plane
class Treasure:

    def __init__(self, position):
        position = self.__position

    def getPosition(self):
        return self.__position

