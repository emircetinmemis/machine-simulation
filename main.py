from util import decode_assembly, opcode, hextobin, menomic, display_content
from Components import ALU, RAM, Accumulator, ProgramCounter, InstructionMemory, Compiler
from application import Application

GUI = False
CONSOLE_WRITE = True
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
    instructions = decode_assembly('data.txt')
    number_of_instructions = len(instructions)

    # Initialize the components
    ram = RAM()
    acc = Accumulator()
    pc = ProgramCounter()
    im = InstructionMemory(instructions)

    while True:
        Compiler.compile_instruction(acc, ram, pc, im)
        is_manual = True and not(CONSOLE_WRITE) # Console output verecegi zaman manuel olmasın diye yaptım cunku console cok sacma oluyor :D (aynı anda hem txt hem console olmuyor sadece enter koyuyorsun fln)

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
    if GUI:
        main_gui()
    else:
        if CONSOLE_WRITE:
            console_output_file = "console_output.txt"
            with contextlib.redirect_stdout(open(console_output_file, "w")):
                main()
        else:
            main()