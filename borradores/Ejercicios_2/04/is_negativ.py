import sys

def is_negative(n):
    if n < 0:
        print("N")
    else:
        print("P")

def main():
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            is_negative(n)
        except ValueError:
            print("Error")
    else:
        print("Error")

if __name__ == "__main__":
    main()