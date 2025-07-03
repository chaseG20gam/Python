import sys

def print_str(str_):

    for i in range(len(str_)):
        print(f"{str_[i]}")
    print()

    # print(len(str_)) "debugging"

def main():
    
    """this program does not count spaces as part of the string rather than a separator for another argument.
    if you want to count spaces, use quotes around the string."""

    str = sys.argv[1]
    print_str(str)

if __name__ == "__main__":
    main()