class Array:
    @staticmethod
    def copy(src, src_pos, des, des_pos, length):
        """
        Copies some item from source array to destination array.

        src: source array that copies item from that.
        src_pos: start position in the source array
        des: destination array that puts items on that
        des_pos: start position in the destination array
        length: specific number of items for copy from source array to destination
        """
        des[des_pos:des_pos + length] = src[src_pos:src_pos + length]

    @staticmethod
    def fill(arr, item, number=None):
        length = len(arr)
        if number is None:
            number = length
        temp = [item] * number
        if length > number:
            Array.copy(arr, number, temp, number, length - number)

        return temp
