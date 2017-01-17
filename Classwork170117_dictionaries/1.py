words = ["a","as","al"]

words_c = {}

for word in words:
    if word not in words_c:
        words_c[word] = 1
    else:
        words_c[word] += 1

print(words_c)
## создание массива из ключей: "перевод из словаря в массив"
keys_list = list(words_c.keys())

print(keys_list)
