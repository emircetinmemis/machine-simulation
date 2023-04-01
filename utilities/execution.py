from constants import (
    PROGRAM_STRUCTURE_CHECKLIST,
    PRE_EXISTING_CHECKLIST,
    PYCACHE_INCLUDERS_CHECKLIST
)
import os
import shutil

def starter():
    
    empty = list()

    for current_folder in PRE_EXISTING_CHECKLIST:
        if not os.path.exists(current_folder):
            os.mkdir(current_folder)

    missangelous = list()
    for current_folder in PROGRAM_STRUCTURE_CHECKLIST:
        if not os.path.exists(current_folder):
            missangelous.append(os.path.abspath(current_folder))
    if missangelous is not empty:
        raise Exception(f"Corrupted program structure. Please make sure the following folders exist: {missangelous}")

def closer():
    
    projectDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for folder in PYCACHE_INCLUDERS_CHECKLIST :
        folderPath = os.path.join(projectDir, folder)
        for root, dirs, files in os.walk(folderPath):
            for dir in dirs :
                if dir == "__pycache__" :
                    shutil.rmtree(os.path.join(root, dir))

    exit()