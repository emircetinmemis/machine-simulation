from utilities import (
    reverse_sign_op, 
    display_content,
    extraction, 
    summation, 
    sign_op 
)
from constants import SIGNED_MAX_LEN
from colorama  import Fore, Style

class ALU:

    def add(acc_value, ram_value):
        """
        If the signs of the two numbers are the same, add them, otherwise subtract the smaller from the
        larger
        
        :param acc_value: The value of the accumulator
        :param ram_value: The value of the RAM cell that is being added to the accumulator
        :return: The result of the addition of the two values.
        """
        result = ''
        if acc_value[0] == '1' and ram_value[0] == '1':
            result = summation(acc_value[1:], ram_value[1:])
            result = '1' + result

        if acc_value[0] == '0' and ram_value[0] == '0':
            result = summation(acc_value[1:], ram_value[1:])
            result = '0' + result

        if acc_value[0] == '1' and ram_value[0] == '0':
            if int(acc_value[1:], 2) > int(ram_value[1:], 2):
                result = extraction(acc_value[1:], ram_value[1:])
                result = '1' + result

            else:
                result = extraction(ram_value[1:], acc_value[1:])
                result = '0' + result
                
        if acc_value[0] == '0' and ram_value[0] == '1':
            if int(acc_value[1:], 2) >= int(ram_value[1:], 2):
                result = extraction(acc_value[1:], ram_value[1:])
                result = '0' + result

            else:
                result = extraction(ram_value[1:], acc_value[1:])
                result = '1' + result

        return result

    def sub(acc_value, ram_value):
        """
        If the sign bits are the same, then the result is the same sign as the sign bits, and the result
        is the difference of the absolute values. 
        
        If the sign bits are different, then the result is the same sign as the sign bit of the larger
        absolute value, and the result is the sum of the absolute values
        
        :param acc_value: The value of the accumulator
        :param ram_value: The value of the RAM
        :return: The result of the subtraction of the two values.
        """
        result =  ''
        if acc_value[0] == '1' and ram_value[0] == '1':
            if int(acc_value[1:], 2) > int(ram_value[1:], 2):
                result = extraction(acc_value[1:], ram_value[1:])
                result = '1' + result

            else:
                result = extraction(ram_value[1:], acc_value[1:])
                result = '0' + result

        if acc_value[0] == '0' and ram_value[0] == '0':
            if int(acc_value[1:], 2) >= int(ram_value[1:], 2):
                result = extraction(acc_value[1:], ram_value[1:])
                result = '0' + result

            else:
                result = extraction(ram_value[1:], acc_value[1:])
                result = '1' + result

        if acc_value[0] == '1' and ram_value[0] == '0':
            result = summation(acc_value[1:], ram_value[1:])
            result = '1' + result

        if acc_value[0] == '0' and ram_value[0] == '1':
            result = summation(acc_value[1:], ram_value[1:])
            result = '0' + result

        return result

    def mul(acc_value, ram_value):
        """
        It takes the value in the accumulator and multiplies it by the value in the RAM, and stores the
        result in the accumulator
        
        :param acc_value: The value of the accumulator
        :param ram_value: the value of the RAM
        :return: The result of the multiplication operation.
        """
        sign = str((int(acc_value[0], 2) + int(ram_value[0], 2)) % 2)
        acc_value = acc_value[1:]
        ram_value = ram_value[1:]

        ram_value = int(reverse_sign_op(ram_value), 16)
        if ram_value == 0:
            return '00000000'
        
        if ram_value == 1:
            return acc_value

        temp = ALU.summation(acc_value, acc_value)
        for i in range(ram_value - 2): 
            temp = summation(temp, acc_value)

        result = sign + temp
        
        return result

    def div(acc_value, ram_value):
        """
        It takes the two values, reverses the sign, divides them, and then reverses the sign again
        
        :param acc_value: The value of the accumulator
        :param ram_value: The value of the RAM
        :return: The result of the division operation.
        """
        sign = str((int(acc_value[0], 2) + int(ram_value[0], 2)) % 2)
        acc_value = acc_value[1:]
        ram_value = ram_value[1:]

        acc_value = int(reverse_sign_op(acc_value), 16)
        ram_value = int(reverse_sign_op(ram_value), 16)

        if ram_value == 0:
            return '00000000'

        if acc_value < ram_value:
            return '00000000'
            
        result = sign + str(sign_op(hex(acc_value // ram_value)))[1:]
        return result

    def neg(acc_value):
        """
        If the first bit is 0, then the result is 1 followed by the rest of the bits. Otherwise, the
        result is 0 followed by the rest of the bits
        
        :param acc_value: The accumulator value
        :return: The result of the negation of the accumulator value.
        """
        result = '1' if acc_value[0] == '0' else '0'
        result += acc_value[1:]
        return result

    def lsl(acc_value, value):
        """
        It takes the sign bit of the accumulator value and shifts it to the left by the value of the
        second argument
        
        :param acc_value: The accumulator value
        :param value: The value to be shifted
        :return: The result of the operation.
        """
        if value[0] == '1' or int(value[1:], 2) < 1:
            return acc_value

        sign_bit = acc_value[0]
        acc_value = acc_value[1:]

        result = ""
        for i in range(int(value, 2)):
            acc_value = acc_value[1:] + '0'
        
        result = sign_bit + acc_value
        return result

    def lsr(acc_value, value):   
        """
        It takes the accumulator value and the value to be shifted, and returns the accumulator value
        after the shift
        
        :param acc_value: The value of the accumulator
        :param value: The value to be shifted
        :return: The result of the operation.
        """
        if value[0] == '1' or int(value[1:], 2) < 1:
            return acc_value

        sign_bit = acc_value[0]
        acc_value = acc_value[1:]

        result = ""
        for i in range(int(value, 2)):
            acc_value = '0' + acc_value[:6]
        
        result = sign_bit + acc_value
        return result

    def xor(acc_value, ram_value):
        """
        It takes two strings of length 8, and returns a string of length 8, where each character is the
        result of an XOR operation on the corresponding characters of the two input strings
        
        :param acc_value: The value of the accumulator
        :param ram_value: The value of the RAM at the current address
        :return: The result of the XOR operation.
        """
        result = ""
        for i in range(8):
            if acc_value[i] == ram_value[i]:
                result += '0'
            else:
                result += '1'
        return result

    def not_(acc_value, value):
        """
        It takes the accumulator value and returns the bitwise NOT of it
        
        :param acc_value: The value of the accumulator
        :param value: the value to be added to the accumulator
        :return: The result of the operation
        """
        result = ""
        for i in range(SIGNED_MAX_LEN):
            result = (result + '1') if acc_value[i] == '0' else (result + '0')
        return result

    def and_(acc_value, ram_value):
        """
        It takes two binary strings and returns a binary string that is the result of the bitwise AND
        operation on the two input strings.
        
        :param acc_value: The value of the accumulator
        :param ram_value: The value of the RAM at the current address
        :return: The result of the AND operation between the ACC and RAM values.
        """
        result = ""
        for i in range(8):
            if acc_value[i] == '1' and ram_value[i] == '1':
                result += '1'
            else:
                result += '0'
        return result

    def or_(acc_value, ram_value):    
        """
        It takes two binary strings of length 8 and returns a binary string of length 8 that is the
        result of the bitwise OR operation on the two input strings
        
        :param acc_value: The value of the accumulator
        :param ram_value: The value of the RAM address that is being accessed
        :return: The result of the operation.
        """
        result = ""
        for i in range(8):
            if acc_value[i] == '1' or ram_value[i] == '1':
                result += '1'
            else:
                result += '0'
        return result   

class RAM:
    
    class MemoryCell:
        def __init__(self, address, value='00000000'):
            """
            The function takes in two arguments, address and value, and assigns them to the object's
            address and value attributes
            
            :param address: The address of the register
            :param value: The value of the register, defaults to 00000000 (optional)
            """
            self.address = address
            self.value = value

        def __str__(self):
            """
            It takes a string of the form "address:value" and returns a tuple of the form (address,
            value)
            :return: The address and the value of the address.
            """
            return '{}:{}'.format(self.address, reverse_sign_op(self.value))

    def __init__(self, amount=256):
        """
        It creates a list of 256 MemoryCell objects, each with a hexadecimal value of 0-255
        
        :param amount: The amount of memory cells to be created, defaults to 256 (optional)
        """
        self.amount = amount
        self.registers = [self.MemoryCell(hex(i)) for i in range(amount)]

    def write(self, address, value):
        """
        It takes a binary string, converts it to an integer, and then uses that integer as an index to
        access a register in a list of registers
        
        :param address: The address of the register to write to
        :param value: The value to be written to the register
        """
        address = int(('0b' + address), 2)
        self.registers[address].value = value

    def read(self, address):
        """
        It converts the address to binary and then returns the value of the register at that address.
        
        :param address: The address of the register to read from
        :return: The value of the register at the address specified.
        """
        address = int(('0b' + address), 2)
        return self.registers[address].value

    def display(self, display_as_hex=False):
        """
        It prints out the contents of the RAM in a table format
        
        :param display_as_hex: True if you want to display the RAM in hexadecimal, False if you want to
        display it in binary, defaults to False (optional)
        """

        HORIZONTAL_CHAR = '=' # old
        VERTICAL_CHAR = ' ' + '|' + ' ' # old
        #HORIZONTAL_CHAR = '█'
        #VERTICAL_CHAR = ' ' + '█' + ' '

        HORIZONTAL_CHAR_START = HORIZONTAL_CHAR * 2
        VERTICAL_CHAR_START = VERTICAL_CHAR[1:]

        col_amount = 16 if display_as_hex else 8
        dash_amount = (col_amount * 13 - 1) if display_as_hex else (col_amount * 17 - 1)
        print('\n' + HORIZONTAL_CHAR_START, HORIZONTAL_CHAR * dash_amount, sep='')
        for i in range(0, self.amount, col_amount):
            print(VERTICAL_CHAR_START, sep='', end='')
            for j in range(0, col_amount):
                ram_address = 'x' + self.registers[i+j].address[2:].upper()
                if display_as_hex:
                    ram_value = reverse_sign_op(self.registers[i+j].value)
                    if ram_value[0] == '-':
                        ram_value = '-' + ram_value[2:]
                    else:
                        ram_value = ram_value[1:]
                else:
                    ram_value = self.registers[i+j].value
                if self.registers[i+j].value != '00000000':
                    print(Fore.GREEN, end='')
                    #print(Back.LIGHTBLACK_EX, end='')
                print('{:4s}: {:4s}'.format(ram_address, ram_value), sep='', end='')
                print(Style.RESET_ALL, end='')
                print(VERTICAL_CHAR, sep='', end='')
            print('\n' + HORIZONTAL_CHAR_START, HORIZONTAL_CHAR * dash_amount, sep='')
            
class InstructionMemory:

    class MemoryCell:
        def __init__(self, address, instruction, value):
            """
            The function takes in an address, instruction, and value and assigns them to the object.
            
            :param address: The address of the memory location
            :param instruction: The instruction to be executed
            :param value: the value of the instruction
            """
            self.address = address
            self.instruction = instruction 
            self.value = value

    def __init__(self, instructions):
        """
        It creates a list of MemoryCell objects, where each object is initialized with the index of the
        object, the first element of the tuple at that index in the instructions list, and the second
        element of the tuple at that index in the instructions list
        
        :param instructions: a list of tuples, each tuple containing a string and an integer
        """
        self.amount = len(instructions)
        self.registers = [self.MemoryCell(i, instructions[i][0], instructions[i][1]) for i in range(self.amount)]

    def read(self, address):
        """
        It returns the instruction and value of the register at the given address
        
        :param address: The address of the register to read from
        :return: The instruction and value of the register at the address.
        """
        return self.registers[address].instruction, self.registers[address].value

    def display(self):
        """
        It prints the value of each register in the register file
        """
        for i in range(self.amount):
            print(self.registers[i])

class Accumulator:

    def __init__(self, value='00000000'):
        """
        The function __init__() is a constructor that initializes the value of the object to the value
        passed as an argument
        
        :param value: The value of the register, defaults to 00000000 (optional)
        """
        self.value = value

    def get_hex(self):
        """
        It takes a number, converts it to hex, reverses the order of the bytes, and then returns the
        result
        :return: The value of the hexadecimal number.
        """
        return reverse_sign_op(self.value)

    def get(self):
        """
        It returns the value of the variable.
        :return: The value of the variable.
        """
        return self.value

    def set(self, value):
        """
        It sets the value of the variable.
        
        :param value: The value to be set
        """
        self.value = value

class ProgramCounter:

    def __init__(self, value=0):
        """
        The function __init__() is a special function in Python classes. It is run as soon as an object
        of a class is instantiated. The method is useful to do any initialization you want to do with
        your object
        
        :param value: The value of the counter. This must be a non-negative integer, defaults to 0
        (optional)
        """
        self.value = value

    def brz(self, acc_value, value):
        """
        If the accumulator is 0 or -0, add the value of the operand to the value of the accumulator, and
        subtract 1
        
        :param acc_value: The value of the accumulator
        :param value: The current value of the program counter
        """
        if acc_value == '00000000' or acc_value == '10000000':
            self.value += int(reverse_sign_op(value), 16) - 1

    def brn(self, acc_value, value):
        """
        If the accumulator is negative, add the value to the accumulator and subtract 1
        
        :param acc_value: The value of the accumulator
        :param value: The value of the current instruction
        """
        if acc_value[0] == '1':
            self.value += int(reverse_sign_op(value), 16) - 1
    
    def increment(self):
        """
        The function increment() takes an object of type Counter and adds 1 to its value
        """
        self.value += 1
        
    def get(self):
        """
        It returns the value of the variable.
        :return: The value of the variable.
        """
        return self.value

class Compiler:

    def compile_instruction(acc, ram, pc, im):
        """
        It takes in the current state of the simulation, executes the instruction at the current program
        counter, and returns the new state of the simulation
        
        :param acc: accumulator
        :param ram: The RAM object
        :param pc: Program Counter
        :param im: Instruction Memory
        :return: The instruction, value, line number, and accumulator value.
        """
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

        return instruction, value, line_number, acc.get()
