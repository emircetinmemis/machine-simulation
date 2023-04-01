from constants import (
    PROGRAM_STRUCTURE_CHECKLIST,
    PYCACHE_INCLUDERS_CHECKLIST,
    PRE_EXISTING_CHECKLIST
)
import shutil
import os

def starter():
    """
    It checks if the folders in the checklist exist, and if they don't, it creates them
    """

    for current_folder in PRE_EXISTING_CHECKLIST:
        if not os.path.exists(current_folder):
            os.mkdir(current_folder)

    missangelous = list()
    for current_folder in PROGRAM_STRUCTURE_CHECKLIST:
        if not os.path.exists(current_folder):
            missangelous.append(os.path.abspath(current_folder))
    if missangelous != []:
        raise Exception(f"Corrupted program structure. Please make sure the following folders exist: {missangelous}")

def closer():
    """
    It deletes all the __pycache__ folders in the project directory
    """
    
    projectDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for folder in PYCACHE_INCLUDERS_CHECKLIST :
        folderPath = os.path.join(projectDir, folder)
        for root, dirs, files in os.walk(folderPath):
            for dir in dirs :
                if dir == "__pycache__" :
                    shutil.rmtree(os.path.join(root, dir))

    exit()