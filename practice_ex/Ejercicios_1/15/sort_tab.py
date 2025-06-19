def sort_tab(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1]:
                # swap if the element found is greater than the next element
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

def main():
    arr = [5, 2, 9, 1, 5, 6]
    print("Original:", arr)
    sorted_arr = sort_tab(arr)
    print("Sorted:", sorted_arr)

if __name__ == "__main__":
    main()
