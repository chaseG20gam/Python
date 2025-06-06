def print_comb2():

    for i in range(100):
        for j in range(i + 1, 100):
            print(f"{i:02d} {j:02d}")

def main():
    print_comb2()

if __name__ == "__main__":
    main()