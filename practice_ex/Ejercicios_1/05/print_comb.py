def print_comb():

    for n1 in range(10):
        for n2 in range(n1 + 1, 10):
            for n3 in range(n2 + 1, 10):
                print(f"{n1}{n2}{n3}" + " ")

def main():
    print_comb()

if __name__ == "__main__":
    main()
    