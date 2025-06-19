def inv_tab(arr_):
    return arr_[::-1]

def main():
    arr = [1, 2, 3, 4, 5]
    print("Original:", arr)
    inverted_arr = inv_tab(arr)
    print("Inverted:", inverted_arr)

if __name__ == "__main__":
    main()