# read in text file
def read_data(testing):
    if testing:
        return open('sample.txt')
    return open('inputDayX.txt')

def main():
    input_data = read_data(testing=True)
    part_one_solution = solve_part_one(input_data)
    part_two_solution = solve_part_two(input_data)
    print(f"The answer to Part 1 is: {part_one_solution}")
    print(f"The answer to Part 2 is: {part_two_solution}")

def solve_part_one(data):
    # solution goes here
    return

def solve_part_two(data):
    # solution goes here
    return

if __name__ == "__main__":
    main()