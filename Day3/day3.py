def main():
    input_data = open('test.txt', 'r')
    priority = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26
        }
    current_priority = 0
    total_priority = 0

    for line in input_data:
        halfway_point = int((len(line) - 1) / 2)
        first_half, second_half = line[:halfway_point], line[halfway_point:]
        common_letter = find_common_letter(first_half, second_half)
        if common_letter.isupper():
            current_priority += 26
        current_priority += priority[common_letter.lower()]
        total_priority += current_priority
        current_priority = 0
    print(total_priority)


def find_common_letter(first_half, second_half):
    for letter in [*first_half]:
        if letter in [*second_half]:
            return letter

def find_common_in_three(first, second, third):
    for letter in [*first]:
        if letter in [*second] and letter in [*third]:
            return letter

if __name__ == "__main__":
    main()
