opcode = {
    'BRZ': '0x0',
    'BRN': '0x1',
    'LDI': '0x2',
    'LDM': '0x3',
    'STR': '0x4',
    'ADD': '0x5',
    'SUB': '0x6',
    'MUL': '0x7',
    'DIV': '0x8',
    'NEG': '0x9',
    'LSL': '0xa',
    'LSR': '0xb',
    'XOR': '0xc',
    'NOT': '0xd',
    'AND': '0xe',
    'ORR': '0xf'
}

menomic = {
    '0x0': 'BRZ',
    '0x1': 'BRN',
    '0x2': 'LDI',
    '0x3': 'LDM',
    '0x4': 'STR',
    '0x5': 'ADD',
    '0x6': 'SUB',
    '0x7': 'MUL',
    '0x8': 'DIV',
    '0x9': 'NEG',
    '0xa': 'LSL',
    '0xb': 'LSR',
    '0xc': 'XOR',
    '0xd': 'NOT',
    '0xe': 'AND',
    '0xf': 'ORR'
}

hextobin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

def decode_assembly(code_path):
    commands = list()
    with open(code_path, 'r') as f:
        for line in f:
            command = extract_code(line)
            if command is not None:
                commands.append(command)
    return commands

def extract_code(raw_line):
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
    if data > 127:
        return hex(127)
    elif data < -127:
        return hex(-127)
    else:
        return hex(data)

def sign_op(data):
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
    sign_bit = data[0]
    data = data[1:]
    data = hex(int(data,2))
    data = ('-' + data) if sign_bit == '1' else data
    data = boundary_check(int(data,16))
    return data

UNSIGNED_MAX_LEN = 7
SIGNED_MAX_LEN = 1 + UNSIGNED_MAX_LEN

def summation(num1, num2):
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
    temp = ''
    for i in range(UNSIGNED_MAX_LEN):
        temp += '0' if num2[i] == '1' else '1'

    num2 = temp

    result = summation(num1, num2)
    result = summation(result, '0000001')
    return result