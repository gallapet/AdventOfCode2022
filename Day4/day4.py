# read in text file
def read_data(testing):
    if testing:
        return open('sample.txt')
    return open('inputDay4.txt')

def main():
    input_data = read_data(testing=False)
    part_one_solution = solve_part_one(input_data)
    part_two_solution = solve_part_two(input_data)
    print(f"The answer to Part 1 is: {part_one_solution}")
    print(f"The answer to Part 2 is: {part_two_solution}")

def solve_part_one(data):
    total = 0
    for line in data:
        elf_assignment = line.split(',')
        first_elf, second_elf = elf_assignment[0], elf_assignment[1].replace('\n', '')
        total += compare_elves(first_elf, second_elf)
    return total

def compare_elves(first, second):
    first = first.split('-')
    second = second.split('-')
    first_as_int = [eval(i) for i in first]
    second_as_int = [eval(j) for j in second]
    if max(first_as_int) <= max(second_as_int) and min(first_as_int) >= min(second_as_int):
        return 1
    elif max(second_as_int) <= max(first_as_int) and min(second_as_int) >= min(first_as_int):
        return 1
    return 0

def solve_part_two(data):
    total = 0
    print(data.read())
    for line in data:
        elf_assignment = line.split(',')
        first_elf, second_elf = elf_assignment[0], elf_assignment[1].replace('\n', '')
        total += find_overlaps(first_elf, second_elf)
    return total

def find_overlaps(first, second):
    first = first.split('-')
    second = second.split('-')
    first_as_int = [eval(i) for i in first]
    second_as_int = [eval(j) for j in second]
    first_as_list = [x for x in range(first_as_int[0], first_as_int[1] + 1)]
    second_as_list = [y for y in range(second_as_int[0], second_as_int[1] + 1)]
    for item in first_as_list:
        if item in second_as_list:
            return 1
    return 0

if __name__ == "__main__":
    main()