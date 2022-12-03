priority = {x: y for (x, y) in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))}

def main():
    input_data = open('inputDay3.txt', 'r')
    total_priority = 0
    input_lines = []

    for line in input_data:
        halfway_point = int((len(line) - 1) / 2)
        first_half, second_half = line[:halfway_point], line[halfway_point:]
        common_letter = find_common_letter(first_half, second_half)
        total_priority += get_total_priority(common_letter)
        input_lines.append(line)

    print(total_priority)

    groups = [input_lines[i:i + 3] for i in range(0, len(input_lines), 3)]
    badge_total = 0
    for group in groups:
        badge = find_common_in_group(group)
        badge_total += get_total_priority(badge)
    print(badge_total)


def find_common_letter(first_half, second_half):
    for letter in [*first_half]:
        if letter in [*second_half]:
            return letter


def find_common_in_group(array):
    for letter in [*array[0]]:
        if letter in [*array[1]] and letter in [*array[2]]:
            return letter


def get_total_priority(letter):
    total = 0
    if letter.isupper():
        total += 26
    total += priority[letter.lower()]
    return total


if __name__ == "__main__":
    main()
