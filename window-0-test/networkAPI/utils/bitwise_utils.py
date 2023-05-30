
class BitwiseUtils:

    @staticmethod
    def str_bits_to_bool_list(*args: str) -> tuple[list[bool], ...]:
        """
            Name: str_bits_to_bool_list

            Description: 
                
                (For each of the *args):

                Evaluates each "binary" element of the bitstring. 
                It creates a list of booleans where each element 
                is True or False depending if there was a 0 or a 
                1 when iterating the previous string.

            Args:
                -> args: list[str]: A list of array representations made of 
                                    a string of 0s and 1s.

            Returns:
                ->  tuple[list[bool], ...]:
                        (for each of the *args) A list of booleans. 
        """
        boolean_lists = []

        # Lambda function that evaluates the string value
        char_to_bool = lambda x: bool(eval(x))

        # Creating the list of booleans based on the arguments
        for bin_str in args:
            bool_list  = list(map(char_to_bool, bin_str))

            boolean_lists.append(bool_list)
        
        return boolean_lists

    @staticmethod
    def split_to_str_bits(input_bytes: bytes, n_left_bits: int) -> tuple[str, str]:
        """
            Name: split_to_str_bits

            Description: 
                Divides a "bytes" object into two different sub-strings 
                that represent the byte slice in binary format

            Args:
                -> input_bytes [bytes]: The byte number to be splitted.
                -> n_left_bits [int]:   Number of bits to be kept in the 
                                        left part.

            Returns:
                ->  tuple[str, str]:
                        (for both args) A string that represents the
                        byte slice in binary format.
        """
        EIGHT_BITS = 8

        # Total bits lenght of input_bytes
        total_bits = len(input_bytes) * EIGHT_BITS

        # Checking bounds
        if n_left_bits < 0 or n_left_bits > total_bits:
            raise ValueError("Invalid \"n_left_bits\" for the left side")

        # Getting a bit string from input_bytes
        bits = ''.join(format(byte, '08b') for byte in input_bytes)
        
        # Splitting the bit string
        left_frag  = bits[:n_left_bits]
        right_frag = bits[n_left_bits:]

        return left_frag, right_frag
    
    @staticmethod
    def int_to_bytes(int_num: int, n_bytes: int = None) -> bytes:
        """
            Name: int_to_bytes

            Description: 
                Converts an int number to bytes with a desired number
                of "n_bytes". If it is smaller than the minimun, the
                number will ocupy the minimun number of bytes. 

            Args:
                -> int_num [int]: The integer to be converted to bytes.
                -> n_bytes [int]: Desired number of bytes for the 
                                  "int_num" bytes conversion.

            Returns:
                ->  [bytes]:
                        (for both args) A string that represents the
                        byte slice in binary format.
        """
        
        SEVEN_BITS      = 7
        EIGHT_BITS_BYTE = 8
        BIG_ENDIAN      = "big"

        minimun_bytes = (int_num.bit_length() + SEVEN_BITS) // EIGHT_BITS_BYTE

        if not n_bytes or n_bytes < minimun_bytes:
            n_bytes = minimun_bytes

        return int_num.to_bytes(n_bytes, BIG_ENDIAN)