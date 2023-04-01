from constants import (
    UNSIGNED_MAX_LEN, 
    hextobin, 
    menomic, 
    opcode
)

def decode_assembly(code_path):
    """
    It reads the file line by line, and for each line, it extracts the command and appends it to a list
    
    :param code_path: The path to the assembly code file
    :return: A list of commands
    """
    commands = list()
    with open(code_path, 'r') as f:
        for line in f:
            command = extract_code(line)
            if command is not None:
                commands.append(command)
    return commands

def extract_code(raw_line):
    """
    It takes a line of code, removes comments, whitespace, and converts it to a list of binary numbers
    
    :param raw_line: The line of code that you want to extract the code from
    :return: the binary code of the instruction.
    """
    # Remove the '\n' at the end
    line = raw_line[:-1] if raw_line[-1] == '\n' else raw_line
    # Remove the comments
    comment_index = line.find('#')
    if comment_index != -1:
        line = line[:comment_index]
    # Remove leading and trailing whitespace
    line = line.replace('\t', ' ')
    line = line.strip()
    # Turn it into a list
    if line == '':
        return None
    line = line.split()
    if line == []:
        return None
    line[0] = opcode[line[0].upper()]
    
    line[1] = input_to_bin(line[1].lower())

    return line

def input_to_bin(val):
    """
    If the input is negative, it adds a 1 to the front of the binary number. If the input is positive,
    it adds a 0 to the front of the binary number
    
    :param val: The value that is being converted to binary
    :return: A string of binary digits.
    """
    if val[0] == '-':
        if len(val) == 2:
            val = '1000' + hextobin[val[1]]
        elif len(val) == 3:
            if hextobin[val[1]][0] == '1':
                val = '1111' + hextobin[val[2]]
            else:
                val = '1' + hextobin[val[1]][1:] + hextobin[val[2]]
        else:
            print('Something went wrong. (-)')
    elif len(val) == 1:
        val = '0000' + hextobin[val]
    elif len(val) == 2:
        if hextobin[val[1]][0] == '1':
            val = '0111' + hextobin[val[1]]
        else:
            val = hextobin[val[0]] + hextobin[val[1]]
    else:
        print('Something went wrong. (+)')
    return val

def display_content(inst, val, line_no, acc):
    """
    It prints the current instruction, the current line number, the current accumulator value, and the
    current instruction value
    
    :param inst: The instruction
    :param val: The instruction value
    :param line_no: The line number of the instruction
    :param acc: The accumulator
    """
    inst_value = reverse_sign_op(val)
    acc_value  = reverse_sign_op(acc)

    print("\n===========================================")
    print("\n\tLine Number:", line_no)
    print("\nCurrent Instruction:", menomic[inst], inst_value)
    print("\tBIN:", val[0], val[1:])
    print("\tHEX:", inst_value)
    print("\tDEC:", int(inst_value, 16))

    print("\nAccumulator")
    print("\tBIN:", acc[0], acc[1:])
    print("\tHEX:", acc_value)
    print("\tDEC:", int(acc_value, 16))
    print()

def boundary_check(data):
    """
    If the data is greater than 127, return 127. If the data is less than -127, return -127. Otherwise,
    return the data
    
    :param data: the data to be checked
    :return: The hexadecimal representation of the data.
    """
    if data > 127:
        return hex(127)
    elif data < -127:
        return hex(-127)
    else:
        return hex(data)

def sign_op(data):
    """
    It takes a hexadecimal number and returns a signed binary number
    
    :param data: The data to be converted to signed binary
    :return: The sign bit and the 7-bit data.
    """
    #print("This:", bin(int(data,16)))
    data = boundary_check(int(data,16))
    data = bin(int(data,16))
    sign_bit = '1' if data[0] == '-' else '0'
    data = data[data.find("b")+1:]
    data = '0' * (7-len(data)) + data
    data = sign_bit + data

    #print("Sign_Op:", data)
    return data

def reverse_sign_op(data):
    """
    If the sign bit is 1, then the number is negative, so we add a negative sign to the front of the
    number. 
    If the sign bit is 0, then the number is positive, so we don't add a negative sign to the front of
    the number
    
    :param data: The binary data to be converted to hexadecimal
    :return: The return value is the data that is passed in.
    """
    sign_bit = data[0]
    data = data[1:]
    data = hex(int(data,2))
    data = ('-' + data) if sign_bit == '1' else data
    data = boundary_check(int(data,16))
    return data

def summation(num1, num2):
    """
    It takes two binary numbers, adds them together, and returns the result
    
    :param num1: The first number to be added
    :param num2:
    1000101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101
    :return: The result of the summation of the two numbers.
    """
    result = ''
    carry = 0
    
    for i in range(UNSIGNED_MAX_LEN - 1, -1, -1):
        r = carry
        r += 1 if num1[i] == '1' else 0
        r += 1 if num2[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
    
        carry = 0 if r < 2 else 1
    
    if carry != 0:
        result = '1' + result

    result = result[len(result) - UNSIGNED_MAX_LEN:]
    return result

def extraction(num1, num2):
    """
    It takes two numbers, inverts the second one, adds them together, and adds one to the result
    
    :param num1: The first number to be subtracted
    :param num2: the number to be subtracted
    :return: The result of the subtraction of two numbers.
    """
    temp = ''
    for i in range(UNSIGNED_MAX_LEN):
        temp += '0' if num2[i] == '1' else '1'

    num2 = temp

    result = summation(num1, num2)
    result = summation(result, '0000001')
    return result