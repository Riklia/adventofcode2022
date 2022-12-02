def one_round(combination):
    combinations = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9,
                    "C X": 7, "C Y": 2, "C Z": 6}
    return combinations[combination]


def calc_round(combination):
    combinations = {"A X": "A Z", "A Y": "A X", "A Z": "A Y", "B X": "B X",
                    "B Y": "B Y", "B Z": "B Z", "C X": "C Y", "C Y": "C Z",
                    "C Z": "C X"}
    return combinations[combination]


with open('input.txt') as file:
    info = file.read().split("\n")[:-1]

print("1.", sum(map(one_round, info)))
print("2.", sum(map(one_round, list(map(calc_round, info)))))
