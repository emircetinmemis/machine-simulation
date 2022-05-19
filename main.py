from util import decode_assembly, opcode, hextobin, menomic
from Components import ALU, RAM, Accumulator, ProgramCounter, InstructionMemory

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
        # Fetch
        instruction, value = im.read(pc.get())
        line_number = pc.get() + 1

        # Execute
        if instruction == '0x0':
            if int(acc.get(), 16) == 0:
                pc.modify(int(value, 16))
                pc.modify(-1)

        elif instruction == '0x1':
            if int(acc.get(), 16) < 0:
                pc.modify(int(value, 16))
                pc.modify(-1)

        elif instruction == '0x2':
            acc.set(value) # value is a hex string because it converted in alu ops

        elif instruction == '0x3':
            acc.set(ram.read(value))

        elif instruction == '0x4':
            ram.write(value, acc.get())

        elif instruction == '0x5':
            acc.set(ALU.add(acc.get(), ram.read(value)))

        elif instruction == '0x6':
            acc.set(ALU.sub(acc.get(), ram.read(value)))

        elif instruction == '0x7':
            acc.set(ALU.mul(acc.get(), ram.read(value)))

        elif instruction == '0x8':
            acc.set(ALU.div(acc.get(), ram.read(value)))

        elif instruction == '0x8':
            acc.set(ALU.neg(acc.get(), ram.read(value)))

        # Update
        pc.modify(1)

        print("\n===========================================")
        print("\n\tCurrent Instruction:", menomic[instruction], int(value, 16))
        print("\n\tRaw Instruction:", instruction, value)
        print("\n\tLine Number:", line_number, "\n\n\tAccumulator:", acc.get())
        ram.display()

        is_manual = True

        if is_manual:
            stop_simulation = input('\nPress \'q\' to exit or press \'Enter\' to cycle once.\n')
            if stop_simulation == 'q' or stop_simulation == 'Q':
                print('>Simulation stopped.')
                break
        
        if pc.get() >= number_of_instructions:
            print('>Simulation finished.')
            break

        
# check if __name__ is main and run the main function
if __name__ == "__main__":
    main()


    # instruction memorysi olur, verilen txt file'in kom