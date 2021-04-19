def sort_group(values, grp):
    found = False
    def sort_helper(el):
        nonlocal found
        if el in grp:
            found = True
            return (0, el)
        return (1, el)
    values.sort(key = sort_helper)
    return found

if __name__ == "__main__":
    numbers = [5, 6, 3, 4, 1, 2, 7, 8, 9]
    group = {4, 7, 9}

    is_found = sort_group(numbers, group)
    print(f"found = {is_found} nums = {numbers}")

    print("--- --- --- ---")