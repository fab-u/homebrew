import sys
import os

def _pathBuilder(relative):
    localDir = os.path.dirname(__file__)
    path = os.path.join(localDir, relative)
    return path


def getBrewPlans():
    f = open(_pathBuilder('../homebrewPlan/plan.txt'),'r')
    content = f.read()
