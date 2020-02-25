#!/usr/bin/env python3

import math

class Navigation:

    def __init__(self, pX, pY, tX, tY):
        self.pX = pX
        self.pY = pY
        self.tX = tX
        self.tY = tY

    def getpX():
        return pX

    def getpY():
        return pY

    def gettX():
        return tX
    
    def gettY():
        return tY

    def setpX():
        self.pX = pX

    def setpY():
        self.pY = pY

    def settX():
        self.tX = tX

    def settY():
        self.tY = tY

    def getAllPosition():
        return "Navigation{" +
                "pX=" + pX +
                ", pY=" + pY +
                ", tX=" + tX +
                ", tY=" + tY +
                "}"

    def calculateResultant():
        xDiff = int(math.pow((pX - tX), 2))
        yDiff = int(math.pow((pY - tY), 2))
        summed = int(xDiff + yDiff)
        
        return math.sqrt(summed)