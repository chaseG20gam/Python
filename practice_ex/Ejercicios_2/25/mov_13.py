def mov_alpha(str_):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = []

    if str_ == '':
        return print("\n")
    else:
        for i in str_:
            if i.isalpha():
                index = alphabet.index(i.lower())
                new_index = (index + 13) % len(alphabet)
                result.append(alphabet[new_index] if i.islower() else alphabet[new_index].upper())
            else:
                result.append(i)
        return ''.join(result)
    
def main():
    str_ = input("Enter a string: ")
    print(mov_alpha(str_))

if __name__ == "__main__":
    main()

    