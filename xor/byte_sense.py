def bytesense(input_text, range):
    """
    Turn a string into bytes, encrypt the result and and return it as hexadecimal
    Input: STR
    Output: HEX
    """
    text_tobytes = bytearray(input_text.encode('utf-8')) # input text to bytes
    # print(text_tobytes)

    even_bytes = text_tobytes[::2]  # extract only the bytes at even indices
    # print(even_bytes)

    concat_bytes = text_tobytes + even_bytes # concat the result of the text and the even result
    # print(concat_bytes)

    
    i = 0
    len_bytes = len(concat_bytes)
    while i < len_bytes: # xor
        concat_bytes[i] ^= (i + range % 256)
        i = i + 1

    # print(concat_bytes)
    return concat_bytes.hex()

def reverse_bytesense(hex_text, range):
    """
    Revert the bytesense encryption and print the original string
    Input: HEX
    Output: STR
    """
    # ask for the same range used in encryption
    new_encrypt_range = int(input('encrypt range used in the encryption: '))
    concat_bytes = bytearray.fromhex(hex_text) # return from hex to bytes
    # print(type(len(concat_bytes))) 

    # reverse the XOR operation
    """for i in len(concat_bytes):
        concat_bytes[i] ^= (i + range % 256)"""
    
    i = 0
    while i < len(concat_bytes):
        concat_bytes[i] ^= (i + range % 256)
        i = i + 1
    """
    -the original bytes are the first half (before concatenation with even_bytes)
    -the length of the original text in bytes is two thirds the result: len(concat_bytes) * 2 // 3?
    -the code always concatenates the original bytes with the even-indexed bytes (which 
    is always half the length of the original, rounded up), the total length of 
    concat_bytes will always be 1.5 times the length of the original byte sequence
    -so its always gonna be two thirds
    """
    orig_bytes = concat_bytes[:len(concat_bytes) * 2 // 3] # has to be // because i need an integer for slicing. 2/3 gives me decimals

    if new_encrypt_range == range:
        original_text = orig_bytes.decode('utf-8')
        print(f'original: {original_text}')
    else:
        print('failed to decode, probably due to a bad encrypting range request')



def main():
    text = input('input a text: ')
    encrypt_range = int(input('encrypt range: ')) # times added at the index to add complexity to the encrypting, could be changed
    bytes_transformed = bytesense(text, encrypt_range)
    print(f'result: ', bytes_transformed)

    print('do you wanna reverse the encryption?')
    reverse = input("y, n: ")
    if reverse == 'y':
        reverse_bytesense(bytes_transformed, encrypt_range)
    else:
        print('program terminated')


if __name__ == '__main__':
    main()


