import sys

def div_mod(a, b, c):
    return (a / b) % c

def main():

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    result = div_mod(a, b , c)
    print(f"Result: ({a} / {b}) % {c} = {result}")

if __name__ == "__main__":
    main()

