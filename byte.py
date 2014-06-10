import string
from array import Array


class Byte:
    @staticmethod
    def hex_to_byte(_hex):
        if not all(c in string.hexdigits for c in _hex):
            raise TypeError("Input type is not hexadecimal.")
        bytes = []
        for i in range(len(_hex) / 2):
            bytes.append(int(_hex[2 * i: 2 * i + 2], 16))

        return bytes

    @staticmethod
    def byte_to_hex(array):
        symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        result = ""
        for i in range(len(array)):
            current = array[i] & 0xff
            temp = ""
            temp = symbols[current & 0x0f] + temp
            temp = symbols[current >> 4] + temp
            result += temp

        return result

    @staticmethod
    def xor(str1, str2):
        if len(str1) > len(str2):
            max_len = len(str1)
        else:
            max_len = len(str2)

        str1 = Byte.extend_byte_array(str1, max_len)
        str2 = Byte.extend_byte_array(str2, max_len)
        result = []
        result = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(str1,str2))
        
        return result

    @staticmethod
    def Or(str1, str2):
        if len(str1) > len(str2):
            max_len = len(str1)
        else:
            max_len = len(str2)

        str1 = Byte.extend_byte_array(str1, max_len)
        str2 = Byte.extend_byte_array(str2, max_len)
        result = []
        result = ''.join(chr(ord(a) | ord(b)) for a,b in zip(str1,str2))
        
        return result

    @staticmethod
    def extend_byte_array(a, new_length):
        if len(a) < new_length:
            temp = Array.fill([], 0, new_length)
            Array.copy(a, 0, temp, 0, len(a))

            a = temp

        return a
