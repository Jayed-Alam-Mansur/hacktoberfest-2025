def print_n_to_1(n: int) -> None:
    if n <= 0:
        return
    print(n)
    print_n_to_1(n - 1)

if __name__ == "__main__":
    try:
        N = int(input("Enter a positive integer N: ").strip())
    except ValueError:
        print("Please enter a valid integer.")
    else:
        print_n_to_1(N)
