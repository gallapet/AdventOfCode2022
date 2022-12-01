def main():
    input_data = open('inputDay1.txt', 'r')
    calories_by_elf = []
    calories_sum = 0
    for calories in input_data:
        if calories == "\n":
            calories_by_elf.append(calories_sum)
            calories_sum = 0
        else:
            calories_sum += int(calories)
    if calories_sum != 0:
        calories_by_elf.append(calories_sum)
    calories_by_elf.sort(reverse=True)
    print(calories_by_elf[0])
    print(sum(calories_by_elf[:3]))

if __name__ == "__main__":
    main()
