from utilities import decode_assembly
from utilities import RAM, Accumulator, ProgramCounter, InstructionMemory, Compiler
from graphics import Application
from utilities import starter, closer
from constants import CONSOLE_TEXT_PATH, INPUT_TXT_PATH
import argparse

# Parts of the machine
#   Memory ->Data Memory, Instruction Memory
#   Register -> Accumulator, Program Counter(maybe list of registers)
#   ALU -> Add, Subtract, Multiply, Divide, Negate, Shift Left, Shift Right, XOR, Not, And, Or
#   Control Circuit
#   
#   INC(?) & Control Word(?=control signals)
#
#   Input Output Components!!!!!!!

def main():
    # Read the assembly code
    instructions = decode_assembly(INPUT_TXT_PATH)
    number_of_instructions = len(instructions)

    # Initialize the components
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

def main_gui():
    app = Application()
    app.mainloop()

def get_arguments():

    parser = argparse.ArgumentParser(description='This is a Python-based simulation of a computer processor that includes components such as Memory, Registers, ALU, and a Control Circuit, which reads assembly code and allows users to interact with it through input/output components. The project is designed to be flexible, efficient, and educational, and can be run in a console or GUI interface.')
    parser.add_argument('-g', '--gui', type=bool, default=True, help='Set this to False if you want to run the simulation in the console. Default is running on gui.')
    parser.add_argument('-c', '--console-save', type=bool, default=False, help='Set this to True if you want to save the console output to a text file. Default is False.')
    parser.add_argument('-i', '--instructions-path', type=str, help='Set this to the path of the assembly code file you want to run. Default is the file in the data folder.')
    parser.add_argument('-o', '--console-output-path', type=str, help='Set this to the path of the text file you want to save the console output to. Default is the file in the data folder.')
    args = parser.parse_args()
    
    return args.console_save, args.gui, args.instructions_path or INPUT_TXT_PATH, args.console_output_path or CONSOLE_TEXT_PATH

# check if __name__ is main and run the main function
import contextlib
if __name__ == "__main__":
    
    CONSOLE_WRITE, GUI, INPUT_TXT_PATH, CONSOLE_TEXT_PATH = get_arguments()
    
    starter()
    try :
        if GUI:
            main_gui()
        else:
            if CONSOLE_WRITE:
                with contextlib.redirect_stdout(open(CONSOLE_TEXT_PATH, "w")):
                    main()
            else:
                main()
    except Exception as e:
        print(f"Exception occured while executing the program: {e}")
        
    closer()