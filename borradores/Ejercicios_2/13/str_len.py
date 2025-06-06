import sys

def str_len(str_):
    return print(len(str_))

def main():
    str_ = sys.argv[1]
    str_len(str_)
    # the program counts spaces as characters. 'Hola mundo' will return 10 instead of 9

if __name__ == "__main__" :
    main()
