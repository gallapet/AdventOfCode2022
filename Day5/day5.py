from collections import defaultdict

# read in text file
def read_data(testing):
    if testing:
        return open('sample.txt')
    return open('inputDay5.txt')

def main():
    input_data = [line.replace('\n', '') for line in read_data(testing=False)]
    part_one_solution = solve_part_one(input_data)
    part_two_solution = solve_part_two(input_data)
    print(f"The answer to Part 1 is: {part_one_solution}")
    print(f"The answer to Part 2 is: {part_two_solution}")

def solve_part_one(data):
    blank_line_separator = data.index('')
    layout, instructions = data[:blank_line_separator], data[blank_line_separator + 1:]
    layout_map = defaultdict(list)
    for line in layout[-2::-1]:
        for i, char in enumerate(line[1::4], 1):
            if char != ' ':
                layout_map[i].append(char)
    layout_map = do_instructions(layout_map, instructions)
    result = []
    for x in range(1, len(layout_map) + 1):
        result.append(layout_map[x][-1])
    return ''.join(result)

def do_instructions(stacks, instructions):
    for command in instructions:
        _, count, _, old_stack, _, new_stack = command.split()
        for i in range(int(count)):
            stacks[int(new_stack)].append(stacks[int(old_stack)].pop())
    return stacks

def solve_part_two(data):
    blank_line_separator = data.index('')
    layout, instructions = data[:blank_line_separator], data[blank_line_separator + 1:]
    layout_map = defaultdict(list)
    for line in layout[-2::-1]:
        for i, char in enumerate(line[1::4], 1):
            if char != ' ':
                layout_map[i].append(char)
    layout_map = do_instructions_new_crane(layout_map, instructions)
    result = []
    for x in range(1, len(layout_map) + 1):
        result.append(layout_map[x][-1])
    return ''.join(result)

def do_instructions_new_crane(stacks, instructions):
    for command in instructions:
        _, count, _, old_stack, _, new_stack = command.split()
        move_pile = stacks[int(old_stack)][-int(count):]
        for i in range(0, int(count)):
            stacks[int(new_stack)].append(move_pile[i])
        del stacks[int(old_stack)][-int(count):]
    return stacks

if __name__ == "__main__":
    main()