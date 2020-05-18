__version__ = "0.6"
__name_ = "coden"
'''
This module is based on my code methods
Explanation for a function/class you can call like: sec_code.function_name/class_name.__doc__
'''

import random    
class randoms:

    """based on random codes"""
    class rande:
        '''returns a rande object(all random characters exept space(always a string)),with which you can:
            - decode: self.decoded
            - encode: self.encoded
characters from qwerty keyboard
parameters(type_):"all"(all characters), "numbers"(only numbers), "alphabets"(only alphabets), "special"(only special characters), "numpha"(numbers and alphabets), "spepha"(special characters and alphabets), "numspe"(numbers and special charaters)                                       
'''
        
        def __init__(self, code, type_ =  "all"):
            type_ = type_.lower()
            if type_ == "all":
                help_ = "abcdefghijklmnopqrstuvwxyzQWERTUIOPLKJHGFDSAMNBVCXZ1234567890!@#$%^&*\()~`,./?><\"':;{}[]+_=-|"
                c = list()
                for i in code:
                    if i != " " and i !="\t":
                        halpc = random.choice(help_)
                        c.append(halpc)
                    else:
                        if i == "\t":
                            c.append("\t")
                        else:
                            c.append(" ")
                global codef
                codef = "".join(c)
                self.encoded = codef
                self.decoded = code
            elif type_ == "numbers":
                help_ = "1234567890"
                c = list()
                for i in code:
                    if i != " " and i !="\t":
                        halpc = random.choice(help_)
                        c.append(halpc)
                    else:
                        if i == "\t":
                            c.append("\t")
                        else:
                            c.append(" ")
                codef = "".join(c)
                self.encoded = codef
                self.decoded = code
            elif type_ == "special":
                help_ = "!@#$%^&*\()~`,./?><\"':;{}[]+_=-|"
                c = list()
                for i in code:
                    if i != " " and i != "\t":
                        halpc = random.choice(help_)
                        c.append(halpc)
                    else:
                        if i == "\t":
                            c.append("\t")
                        else:
                            c.append(" ")
                codef = "".join(c)
                self.encoded = codef
                self.decoded = code
            elif type_ == "numpha":
                help_ = "abcdefghijklmnopqrstuvwxyzQWERTUIOPLKJHGFDSAMNBVCXZ1234567890"
                c = list()
                for i in code:
                    if i != " " and i != "\t":
                        halpc = random.choice(help_)
                        c.append(halpc)
                    else:
                        if i == "\t":
                            c.append("\t")
                        else:
                            c.append(" ")
                codef = "".join(c)
                self.encoded = codef
                self.decoded = code
            elif type_ == "alphabets":
                help_ = "abcdefghijklmnopqrstuvwxyzQWERTUIOPLKJHGFDSAMNBVCXZ"
                c = list()
                for i in code:
                    if i != " " and i != "\t":
                        halpc = random.choice(help_)
                        c.append(halpc)
                    else:
                        if i == "\t":
                            c.append("\t")
                        else:
                            c.append(" ")
                codef = "".join(c)
                self.encoded = codef
                self.decoded = code
            elif type_ == "spepha":
                help_ = "abcdefghijklmnopqrstuvwxyzQWERTUIOPLKJHGFDSAMNBVCXZ!@#$%^&*\()~`,./?><\"':;{}[]+_=-|"
                c = list()
                for i in code:
                    if i != " " and i != "\t":
                        halpc = random.choice(help_)
                        c.append(halpc)
                    else:
                        if i == "\t":
                            c.append("\t")
                        else:
                            c.append(" ")
                codef = "".join(c)
                self.encoded = codef
                self.decoded = code
            elif type_ == "numspe":
                help_ = "1234567890!@#$%^&*\()~`,./?><\"':;{}[]+_=-|"
                c = list()
                for i in code:
                   if i != " " and i != "\t":
                        halpc = random.choice(help_)
                        c.append(halpc)
                   else:
                        if i == "\t":
                            c.append("\t")
                        else:
                            c.append(" ")
                codef = "".join(c)
                self.encoded = codef
                self.decoded = code
            else:
                raise ValueError("type_ value is not correct")
            

    def hexadecimal(a, b):
        """returns random hexadecimal number in range of a, b"""
        ai = hex_to_int(a)
        bi = hex_to_int(b)
        return int_to_hex(random.randint(ai, bi))
    
    def hexcolor():
        """ returns a random hexadecimal number(color)"""
        a = hex(random.randint(0,255))
        b = hex(random.randint(0,255))
        c = hex(random.randint(0,255))
        a = a[2:]
        b = b[2:]
        c = c[2:]
        if len(a)<2:
            a = "0" + a
        if len(b)<2:
            b = "0" + b
        if len(c)<2:
            c = "0" + c
        z = a + b + c
        return "#" + z.upper()
    
    def rgb(mode="normal"):
        """
        returns a random rgb color code. mode can be normal(0-255) or turtle(0.0-1.0)
        """
        if mode == "normal":
            return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        elif mode == "turtle":
            return (random.random(),random.random(), random.random())
        else:
            raise Exception("Mode can only be 'normal' or 'turtle'")
    def hsl():
        """
        returns a random hsl hue saturation light color code
        """
        return  (random.randint(0, 100), random. randint(0, 100), random.randint(0, 100))
    def binary(a, b):
        """genarates random binary number with range a, b"""
        a = str(a)
        b = str(b)
        inta = binary(a, mode = "to_int")
        intb = binary(b, mode = "to_int")
        ran = random.randint(inta, intb)
        resultb = binary(ran, mode = "to_binary")
        return resultb
        
    def password(main_word = ""):
        """generates secure password"""
        lnpassw = "0123456789"
        help_p = "1234567890@*.-"
        c = list()
        for i in lnpassw:
            if i != " "and i != "\t":
                halpc = random.choice(help_p)
                c.append(halpc)
            else:
                if i == "\t":
                    c.append("\t")
                else:
                    c.append(" ")
        codefpassw = "".join(c)
        rpassw = list(codefpassw)
        del rpassw[0:len(main_word)]
        rpassw.insert(random.randint(0, len(rpassw)), main_word)
        rpassw = "".join(rpassw)
        return rpassw
    
    def pin():
        """generates secure pin"""
        lnpin = "012345"
        rpin = randoms.rande(lnpin, type_ = "numbers")
        return rpin.encoded

    



        
def secret(message, mode = "encode"):
    """encodes or decodes the message in a secret language"""
    if mode == "encode":
        encoded = ""
        for char in message:
            if char == "a" or char == "A":
                encoded += "#"
            elif char == "b" or char == "B":
                encoded += "*"
            elif char == "c" or char == "C":
                encoded += "3"
            elif char == "d" or char == "D":
                encoded += "f"
            elif char == "e" or char == "E":
                encoded += "@"
            elif char == "f" or char == "F":
                encoded += "4"
            elif char == "g" or char == "G":
                encoded += "!"
            elif char == "h" or char == "H":
                encoded += "j"
            elif char == "i" or char == "I":
                encoded += ")"
            elif char == "j" or char == "J":
                encoded += "l"
            elif char == "k" or char == "K":
                encoded += "w"
            elif char == "l" or char == "L":
                encoded += "n"
            elif char == "m" or char == "M":
                encoded += "0"
            elif char == "n" or char == "N":
                encoded += "p"
            elif char == "o" or char == "O":
                encoded += "q"
            elif char == "p" or char == "P":
                encoded += "r"
            elif char == "q" or char == "Q":
                encoded += "$"
            elif char == "r" or char == "R":
                encoded += "t"
            elif char == "s" or char == "S":
                encoded += "u"
            elif char == "t" or char == "T":
                encoded += "v"
            elif char == "u" or char == "U":
                encoded += "m"
            elif char == "v" or char == "V":
                encoded += "x"
            elif char == "w" or char == "W":
                encoded += "y"
            elif char == "x" or char == "X":
                encoded += "z"
            elif char == "y" or char == "Y":
                encoded += "a"
            elif char == "z" or char == "Z":
                encoded += "b"
            else:
                encoded += char
        return encoded
    elif mode == "decode":
        encoded = ""
        for char in message:
            if char == "#":
                encoded += "a"
            elif char == "*":
                encoded += "b"
            elif char == "3":
                encoded += "c"
            elif char == "f":
                encoded += "d"
            elif char == "@":
                encoded += "e"
            elif char == "4":
                encoded += "f"
            elif char == "!":
                encoded += "g"
            elif char == "j":
                encoded += "h"
            elif char == ")":
                encoded += "i"
            elif char == "l":
                encoded += "j"
            elif char == "w":
                encoded += "k"
            elif char == "n":
                encoded += "l"
            elif char == "0":
                encoded += "m"
            elif char == "p":
                encoded += "n"
            elif char == "q":
                encoded += "o"
            elif char == "r":
                encoded += "p"
            elif char == "$":
                encoded += "q"
            elif char == "t":
                encoded += "r"
            elif char == "u":
                encoded += "s"
            elif char == "v":
                encoded += "t"
            elif char == "m":
                encoded += "u"
            elif char == "x":
                encoded += "v"
            elif char == "y":
                encoded += "w"
            elif char == "z":
                encoded += "x"
            elif char == "a":
                encoded += "y"
            elif char == "b":
                encoded += "z"
            else:
                encoded += char
        return encoded
    else:
        raise Exception("You can only choose mode is encode or decode")

def bin_to_int(number):
    """converts binary to integer"""
    number = str(number)
    return int(number, 2)

def int_to_bin(number):
    number = int(number)
    return int(bin(number)[2:])

def hex_to_bin(number):
    nomint = hex_to_int(number)
    return int_to_bin(nomint)

def bin_to_hex(number):
    nomintb = bin_to_int(number)
    return int_to_hex(nomintb)

def hex_to_int(number):
    number = str(number)
    return int(number, 16)

def int_to_hex(number):
    number = int(number)
    return str(hex(number)[2:])
