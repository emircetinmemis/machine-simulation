from utilities import decode_assembly
from utilities import RAM, Accumulator, ProgramCounter, InstructionMemory, Compiler
from graphics import Application
from utilities import starter, closer
from constants import CONSOLE_TEXT_PATH, INPUT_TXT_PATH
import argparse
import contextlib

def console_application():
    instructions = decode_assembly(INPUT_TXT_PATH)
    number_of_instructions = len(instructions)

    ram = RAM()
    acc = Accumulator()
    pc = ProgramCounter()
    im = InstructionMemory(instructions)

    while True:
        Compiler.compile_instruction(acc, ram, pc, im)
        is_manual = True and not(CONSOLE_WRITE)

        if is_manual:
            stop_simulation = input('\nPress \'q\' to exit or press \'Enter\' to cycle once.\n')
            if stop_simulation == 'q' or stop_simulation == 'Q':
                print('<Simulation stopped>')
                break
        
        if pc.get() >= number_of_instructions:
            print('<Simulation finished>')
            break

def graphical_application():
    app = Application()
    app.mainloop()

def get_application(application_type):
    if application_type == "gui":
        return graphical_application
    elif application_type == "console":
        return console_application


def get_arguments():

    parser = argparse.ArgumentParser(description='This is a Python-based simulation of a computer processor that includes components such as Memory, Registers, ALU, and a Control Circuit, which reads assembly code and allows users to interact with it through input/output components. The project is designed to be flexible, efficient, and educational, and can be run in a console or GUI interface.')
    parser.add_argument('-g', '--gui', type=int, default=True, help='Set this to False if you want to run the simulation in the console. Default is running on gui.')
    parser.add_argument('-c', '--console-save', type=int, default=False, help='Set this to True if you want to save the console output to a text file. Default is False.')
    parser.add_argument('-i', '--instructions-path', type=str, help='Set this to the path of the assembly code file you want to run. Default is the file in the data folder.')
    parser.add_argument('-o', '--console-output-path', type=str, help='Set this to the path of the text file you want to save the console output to. Default is the file in the data folder.')
    args = parser.parse_args()
    
    return bool(args.console_save), bool(args.gui), args.instructions_path or INPUT_TXT_PATH, args.console_output_path or CONSOLE_TEXT_PATH

if __name__ == "__main__":
    
    CONSOLE_WRITE, GUI, INPUT_TXT_PATH, CONSOLE_TEXT_PATH = get_arguments()
    print(f"Console write: {CONSOLE_WRITE}, GUI: {GUI}, Input path: {INPUT_TXT_PATH}, Output path: {CONSOLE_TEXT_PATH}")
    starter()
    try :
        if CONSOLE_WRITE:
            with contextlib.redirect_stdout(open(CONSOLE_TEXT_PATH, "w")):
                get_application("gui" if GUI else "console")()
        else:
            get_application("gui" if GUI else "console")() 
    except Exception as e:
        print(f"Exception occured while executing the program: {e}")

    closer()