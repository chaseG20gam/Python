import sys

def search_replace(str_, srch, repl):
    result = []

    if str_ == '':
        return print("\n")
    else:
        for i in str_:
            if i == srch:
                result.append(repl)
            else:
                result.append(i)
        return ''.join(result)
    
def main():
    if len(sys.argv) < 4 or len(sys.argv) > 4:
        print("\n")
        return
    else:
        str_ = str(sys.argv[1])
        srch = str(sys.argv[2])
        repl = str(sys.argv[3])
        str_ = search_replace(str_, srch, repl)

        print(str_)

if __name__ == "__main__":
    main()