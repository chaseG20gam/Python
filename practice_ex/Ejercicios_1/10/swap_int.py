def swap_int(a, b):
    return b, a

def main():
    a = int(input("int 1: "))
    b = int(input("int 2: "))
    print(f"before swap: int 1 = {a}, int 2 = {b}")
    a, b = swap_int(a, b)
    print(f"after swap: int 1 = {a}, int 2 = {b}")

if __name__ == "__main__":
    main()