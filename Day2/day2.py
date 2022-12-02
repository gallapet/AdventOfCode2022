def main():
    input_data = open('inputDay2.txt', 'r')
    score = 0
    for line in input_data:
        if line[0] == "A":
            score += opponent_chose_rock(line[2])
        elif line[0] == "B":
            score += opponent_chose_paper(line[2])
        elif line[0] == "C":
            score += opponent_chose_scissors(line[2])
    print(score)

def opponent_chose_rock(prediction):
    if prediction == "X":
        return 4
    elif prediction == "Y":
        return 8
    elif prediction == "Z":
        return 3

def opponent_chose_paper(prediction):
    if prediction == "X":
        return 1
    elif prediction == "Y":
        return 5
    elif prediction == "Z":
        return 9


def opponent_chose_scissors(prediction):
    if prediction == "X":
        return 7
    elif prediction == "Y":
        return 2
    elif prediction == "Z":
        return 6


if __name__ == "__main__":
    main()