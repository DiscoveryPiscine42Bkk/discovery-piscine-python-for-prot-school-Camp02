def main():

    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = [num + 2 for num in original_array if num > 5]

    unique_values = set(new_array)

    print(original_array)
    print(unique_values)

if __name__ == "__main__":
    main()
input()