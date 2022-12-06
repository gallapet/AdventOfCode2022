# read in text file
def read_data(testing):
    if testing:
        return open('sample.txt')
    return open('inputDay6.txt')

def main():
    input_data = [line for line in read_data(testing=False)]
    part_one_solution = solve_part_one(input_data[0])
    part_two_solution = solve_part_two(input_data[0])
    print(f"The answer to Part 1 is: {part_one_solution}")
    print(f"The answer to Part 2 is: {part_two_solution}")

def solve_part_one(data):
    for idx, char in enumerate(data[3:], 3):
        group_of_four = data[idx-3:idx+1]
        if len(set(group_of_four)) == 4:
            return idx + 1
    return

def solve_part_two(data):
    for idx, char in enumerate(data[13:], 13):
        group_of_four = data[idx - 13:idx + 1]
        if len(set(group_of_four)) == 14:
            return idx + 1
    return

if __name__ == "__main__":
    main()