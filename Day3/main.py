def get_priority(input_str):
    for letter in input_str:
        if letter.islower():
            return ord(letter) % 96
        else:
            return ord(letter) % 64 + 26


def intersection(content):
    if len(content) == 2:
        return ''.join((set(content[0]) & set(content[1])))
    else:
        return ''.join(content[0] & content[1] & content[2])


with open('input.txt') as file:
    info = file.read().split("\n")[:-1]

info2 = [[set(x), set(y), set(z)] for x, y, z in zip(info[0::3], info[1::3], info[2::3])]
info = [[i[:len(i) // 2], i[len(i) // 2:]] for i in info]

print("1.", sum(map(get_priority, list(map(intersection, info)))))
print("2.", sum(map(get_priority, list(map(intersection, info2)))))
