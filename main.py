from utilities import decode_assembly
from utilities import RAM, Accumulator, ProgramCounter, InstructionMemory, Compiler
from graphics import Application
from utilities import starter, closer
from constants import CONSOLE_TEXT_PATH, INPUT_TXT_PATH

GUI = True
CONSOLE_WRITE = False
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

# check if __name__ is main and run the main function
import contextlib
if __name__ == "__main__":
    starter()
    if GUI:
        main_gui()
    else:
        if CONSOLE_WRITE:
            with contextlib.redirect_stdout(open(CONSOLE_TEXT_PATH, "w")):
                main()
        else:
            main()
    closer()