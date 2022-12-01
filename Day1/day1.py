def main():
    input_data = open('inputDay1.txt').readlines()
    formatted_data = format_data(input_data)
    most_calories = 0
    calories_sum = 0
    for calories in formatted_data:
        if calories != "\n":
            calories_sum += int(calories)
        else:
            if calories_sum > most_calories:
                most_calories = calories_sum
            calories_sum = 0
    print(most_calories)

def format_data(data):
    data_with_separators = []
    for line in data:
        if line != "\n":
            data_with_separators.append(line.replace("\n", ""))
        else:
            data_with_separators.append(line)
    return data_with_separators

if __name__ == "__main__":
    main()
