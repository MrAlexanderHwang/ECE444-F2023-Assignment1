#Below code was generated with ChatGPT but modified for debugging

class Utils:
    @staticmethod
    def reversed(number):
        if isinstance(number, int):
            if number < 0:
                return int("-" + str(abs(number))[::-1])
            else: 
                return int(str(number)[::-1])
        else:
            raise ValueError("Input must be an integer")

    @staticmethod
    def formatter(number):
        if isinstance(number, int):
            binary = bin(number)
            octal = oct(number)
            return binary, octal
        else:
            raise ValueError("Input must be an integer")
