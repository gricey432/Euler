def char_to_num(char):
    return ord(char) - ord('A') + 1

def word_value(word):
    return sum([char_to_num(c) for c in word])

with open("p042_words.txt", "r") as f:
    word_values = [word_value(w[1:-1]) for w in f.readline().split(",")]

largest_value = max(word_values)

triangle_nums = []
n = 1
while True:
    new = n * (n + 1) / 2
    triangle_nums.append(new)
    if new > largest_value:
        break
    n += 1

print sum([1 for value in word_values if value in triangle_nums])
