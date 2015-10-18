names = [ 'D', 'u', 'r', 'i', 'n', 'g']

def sortNames():
    global names
    names.sort()

def binarySearch():
    global names, found, nameSearch, lower_bound, middle_pos, upper_bound

    nameSearch = input("What name are you looking for? ")
    lower_bound = 0
    upper_bound = len(names)-1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound+upper_bound) // 2
        if names[middle_pos] < nameSearch:
            lower_bound = middle_pos + 1
        elif names[middle_pos] > nameSearch:
            upper_bound = middle_pos - 1
        else:
            found = True
    if found:
        print("The name is at position", middle_pos)
    else:
        print("The name was not in the list.")                           

def main():
        sortNames()
        binarySearch()

if __name__ == "__main__":
    main()