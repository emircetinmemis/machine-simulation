from util import decode_assembly, opcode, hextobin, menomic, display_content
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
        # BRZ: Branch on Zero
        if instruction == '0x0':
            pc.brz(acc.get(), value)
        # BRN: Branch on Negative
        elif instruction == '0x1':
            pc.brn(acc.get(), value)
        # LDI: Load Immediate
        elif instruction == '0x2':
            acc.set(value)
        # LDM: Load from Memory
        elif instruction == '0x3':
            acc.set(ram.read(value))
        # STR: Store
        elif instruction == '0x4':
            ram.write(value, acc.get())
        # ADD: Add
        elif instruction == '0x5':
            acc.set(ALU.add(acc.get(), ram.read(value)))
        # SUB: Subtract
        elif instruction == '0x6':
            acc.set(ALU.sub(acc.get(), ram.read(value)))
        # MUL: Multiply
        elif instruction == '0x7':
            acc.set(ALU.mul(acc.get(), ram.read(value)))
        # DIV: Divide
        elif instruction == '0x8':
            acc.set(ALU.div(acc.get(), ram.read(value)))
        # NEG: Negate
        elif instruction == '0x9':
            acc.set(ALU.neg(acc.get(), ram.read(value)))
        # LSL: Shift Left
        elif instruction == '0xa':
            acc.set(ALU.lsl(acc.get(), value))
        # LSR: Shift Right
        elif instruction == '0xb':
            acc.set(ALU.lsr(acc.get(), value))
        # XOR: Bitwise XOR
        elif instruction == '0xc':
            acc.set(ALU.xor(acc.get(), ram.read(value)))
        # NOT: Bitwise NOT
        elif instruction == '0xd':
            acc.set(ALU.not_(acc.get(), value))
        # AND: Bitwise AND
        elif instruction == '0xe':
            acc.set(ALU.and_(acc.get(), ram.read(value)))
        # ORR: Bitwise OR
        elif instruction == '0xf':
            acc.set(ALU.or_(acc.get(), ram.read(value)))

        # Update
        pc.increment()

        # Displaying the content of the simulation
        display_content(instruction, value, line_number, acc.get())
        ram.display(display_as_hex=True)

        is_manual = True

        if is_manual:
            stop_simulation = input('\nPress \'q\' to exit or press \'Enter\' to cycle once.\n')
            if stop_simulation == 'q' or stop_simulation == 'Q':
                print('<Simulation stopped>')
                break
        
        if pc.get() >= number_of_instructions:
            print('<Simulation finished>')
            break

        
# check if __name__ is main and run the main function
if __name__ == "__main__":
    main()