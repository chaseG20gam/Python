def str_inv_case(str_):
    result = []

    if str_ == '':
        return print("\n")
    else:
        for i in str_:
            if i.isalpha():
                if i.islower():
                    result.append(i.upper())
                else:
                    result.append(i.lower())
            else:
                result.append(i)
        return ''.join(result)
    
def main():
    str_ = input("Enter a string: ")
    print(str_inv_case(str_))

if __name__ == "__main__":
    main()