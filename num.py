def dec2bin(num):
    return int(bin(num).replace("0b", ""))

def bin2dec(num):
    return int(num, 2)

def dec2oct(num):
    return oct(num);

def oct2dec(num):
    return int(num, 8)

def dec2hex(num):
    return hex(num);

def hex2dec(num):
    return int(num, 16);

def bin2hex(num):
    return dec2hex(bin2dec(num))

def oct2bin(num):
    return dec2bin(oct2dec(num))
