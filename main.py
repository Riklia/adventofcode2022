def find_marker(info, length):
    i = 0
    while i < len(info) - length:
        for char in info[i:i + length]:
            if info[i:i + length].count(char) > 1:
                i += info[i:i + length].index(char)+1
                break
        else:
            return i+length


with open('input.txt') as file:
    inp = file.read()[:-1]

print("1.", find_marker(inp, 4))
print("2.", find_marker(inp, 14))
