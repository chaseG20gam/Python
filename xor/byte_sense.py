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



def main():
    text = input('introduce un texto: ')
    encrypt_range = int(input('introduce el rango de encriptado: ')) # times added at the index to add complexity to the encrypting, could be changed
    bytes_transformed = bytesense(text, encrypt_range)
    print(f'result: ', bytes_transformed)

if __name__ == '__main__':
    main()


