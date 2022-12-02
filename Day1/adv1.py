with open('adv1.txt') as file:
    test = file.read().split('\n\n')[:-1]

for i in range(len(test)):
    test[i] = sum(map(int, test[i].split('\n')))

print(max(test))
print(sum(sorted(test, reverse=True)[:3]))
