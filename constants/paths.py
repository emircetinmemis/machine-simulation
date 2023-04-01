import os

def _connect_paths(*paths):
    """
    It takes a variable number of arguments and joins them together with the appropriate path separator
    :return: the path of the file.
    """
    return os.path.join(*paths)

ASSETS_FOLDER_PATH = "assets"
CONSTANTS_FOLDER_PATH = "constants"
GRAPHICS_FOLDER_PATH = "graphics"
DATA_FOLDER_PATH = "data"
UTILITIES_FOLDER_PATH = "utilities"

SHEET_PATH = _connect_paths(ASSETS_FOLDER_PATH, "instruction_set.png")
INPUT_TXT_PATH = _connect_paths(DATA_FOLDER_PATH, "instructions.txt")
CONSOLE_TEXT_PATH = _connect_paths(DATA_FOLDER_PATH, "console_output.txt")

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

PRE_EXISTING_CHECKLIST = [
    DATA_FOLDER_PATH
]