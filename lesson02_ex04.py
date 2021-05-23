my_word= input().split()
print(my_word)
for i, el in enumerate(my_word):
    print(i + 1, ': ', el[0:10])