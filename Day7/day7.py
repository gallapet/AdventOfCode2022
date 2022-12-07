# read in text file
from collections import defaultdict


def read_data(testing):
    if testing:
        return open('sample.txt')
    return open('inputDay7.txt')


def main():
    input_data = [line.replace('\n', '') for line in read_data(testing=False)]
    part_one_solution = solve_part_one(input_data)
    part_two_solution = solve_part_two(input_data)
    print(f"The answer to Part 1 is: {part_one_solution}")
    print(f"The answer to Part 2 is: {part_two_solution}")


def solve_part_one(data):
    path = []
    result = {}
    for index, command in enumerate(data):
        split = command.split()
        if split[0] == "$":
            if split[1] == "cd":
                if split[2] == "..":
                    path.pop()
                else:
                    path.append(split[2])
                    result.setdefault(''.join(path), [])
        else:
            if split[0] != "dir":
                result[''.join(path)].append(int(split[0]))
            else:
                result[''.join(path)].append(split[1])

    sorted_result_list = sorted(list(result.items()), key=lambda key: len(key[0]), reverse=True)
    sorted_result = {element[0]: element[1] for element in sorted_result_list}

    for key in sorted_result:
        total = 0
        for idx, value in enumerate(sorted_result[key]):
            if str(value).isalpha():
                sorted_result[key][idx] = sorted_result[key+value]
                total += sorted_result[key][idx]
            else:
                total += sorted_result[key][idx]
        sorted_result[key] = total

    result = 0
    for path in sorted_result:
        if sorted_result[path] <= 100000:
            result += sorted_result[path]

    return result

def solve_part_two(data):
    # solution goes here
    return

if __name__ == "__main__":
    main()
