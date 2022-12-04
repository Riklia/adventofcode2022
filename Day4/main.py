def cont(ids):
    ids = [list(map(int, i.split('-'))) for i in ids]
    if ids[0][0] <= ids[1][0] and ids[0][1] >= ids[1][1]:
        return 1
    elif ids[0][0] >= ids[1][0] and ids[0][1] <= ids[1][1]:
        return 1
    else:
        return 0


def overlap(ids):
    ids = [list(map(int, i.split('-'))) for i in ids]
    if ids[1][0] > ids[0][1] or ids[0][0] > ids[1][1]:
        return 0
    else:
        return 1


with open('input.txt') as file:
    info = [i.split(",") for i in file.read().split("\n")[:-1]]

print("1.", sum(map(cont, info)))
print("2.", sum(map(overlap, info)))
