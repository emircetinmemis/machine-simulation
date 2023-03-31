import os

def _connect_paths(*paths):
    return os.path.join(*paths)

ASSETS_FOLDER_PATH = "assets"
CONSTANTS_FOLDER_PATH = "constants"
GRAPHICS_FOLDER_PATH = "graphics"
UTILITIES_FOLDER_PATH = "utilities"

SHEET_PATH = _connect_paths(ASSETS_FOLDER_PATH, "instruction_set.png")

PROGRAM_STRUCTURE_CHECKLIST = [
    ASSETS_FOLDER_PATH,
    CONSTANTS_FOLDER_PATH,
    GRAPHICS_FOLDER_PATH,
    UTILITIES_FOLDER_PATH
]

PYCACHE_INCLUDERS_CHECKLIST = [
    CONSTANTS_FOLDER_PATH,
    GRAPHICS_FOLDER_PATH,
    UTILITIES_FOLDER_PATH
]