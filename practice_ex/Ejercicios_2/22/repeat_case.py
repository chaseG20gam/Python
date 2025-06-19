def repeat_case(str_):
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    result = []

    if str_ == '':
        return print("\n")
    else:
        for i in str_:
            if i.isalpha():
                index = alphabet.index(i.lower())
                result.append(i * (index + 1))
            else:
                result.append(i)
        return ''.join(result)

def main():
    str_ = input("Enter a string: ")
    print(repeat_case(str_))

if __name__ == "__main__":
    main()