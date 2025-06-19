import sys

def str_up_case(str_):
    str_ = str_.upper()
    return str_

def main():
    str_ = str(sys.argv[1])
    str_ = str_up_case(str_)
    print(str_)

if __name__ == "__main__":
    main()
    