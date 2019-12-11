import sys
import os

def _pathBuilder(relative):
    localDir = os.path.dirname(__file__)
    path = os.path.join(loaclDir, relative)
    return path


def getBrewPlans():
    f = open(_pathBuilder('../homebrewPlan/plan.txt'),'r')
    content = f.read()



#script_dir = os.path.dirname(__file__)
#file_path = os.path.join(script_dir, './output03.txt')
#print(file_path)
#fptr = open(file_path, 'w')
