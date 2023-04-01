from    utilities   import  RAM, Accumulator, ProgramCounter, InstructionMemory, Compiler
from    constants   import  CONSOLE_TEXT_PATH, INPUT_TXT_PATH
from    utilities   import  decode_assembly
from    utilities   import  starter, closer
from    graphics    import  Application
import  contextlib
import  argparse

def console_application() -> None:
    """
    It takes the instructions from the input file, puts them into the instruction memory, and then
    cycles through the instructions until the program counter reaches the end of the instructions.
    """
    instructions = decode_assembly(INPUT_TXT_PATH)
    number_of_instructions = len(instructions)

    ram = RAM()
    acc = Accumulator()
    pc = ProgramCounter()
    im = InstructionMemory(instructions)

    while True:
        Compiler.compile_instruction(acc, ram, pc, im)
        is_manual = True

        if is_manual:
            stop_simulation = input('\nPress \'q\' to exit or press \'Enter\' to cycle once.\n')
            if stop_simulation == 'q' or stop_simulation == 'Q':
                print('<Simulation stopped>')
                break
        
        if pc.get() >= number_of_instructions:
            print('<Simulation finished>')
            break

def graphical_application():
    """
    It creates an instance of the `Application` class, and then calls the `mainloop` method on that
    instance
    """
    app = Application()
    app.mainloop()

def execute_application():
    """
    If the user wants to run the GUI version of the application, then run the GUI version of the
    application. If the user wants to run the console version of the application, then run the console
    version of the application. If the user wants to save the console output, then save the console
    output
    """
    isGUI, isSaved = get_arguments()
    
    if isGUI:
        if isSaved:
            with contextlib.redirect_stdout(open(CONSOLE_TEXT_PATH, "w")):
                graphical_application()
        else:
            graphical_application()
    else:
        if isSaved:
            with contextlib.redirect_stdout(open(CONSOLE_TEXT_PATH, "w")):
                console_application()
        else:
            console_application()


def get_arguments():
    """
    It takes in two arguments, gui and console_save, and returns them as booleans
    :return: a tuple of two boolean values.
    """
    parser = argparse.ArgumentParser(description='This is a Python-based simulation of a computer processor that includes components such as Memory, Registers, ALU, and a Control Circuit, which reads assembly code and allows users to interact with it through input/output components. The project is designed to be flexible, efficient, and educational, and can be run in a console or GUI interface.')
    parser.add_argument('-g', '--gui', type=int, default=True, help='Set this to False if you want to run the simulation in the console. Default is running on gui.')
    parser.add_argument('-c', '--console-save', type=int, default=False, help='Set this to True if you want to save the console output to a text file. Default is False.')
    args = parser.parse_args()
    
    return bool(args.gui), bool(args.console_save)

# A way to make sure that the code in the `starter` and `closer` functions is only executed when the
# file is run as a script.
if __name__ == "__main__":
    
    starter()
    
    execute_application()

    closer()