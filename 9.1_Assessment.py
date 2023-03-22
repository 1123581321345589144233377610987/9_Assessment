words = {}
FILE = open('tale_of_two_cities.txt', 'r')
file = FILE.readlines()
FILE.close()
for i in file:
    i = i.strip('\n')
    if i in words:
        words[i] += 1
    if i not in words:
        words[i] = 1
for i in words:
    if words[i] == 1:
        print(i)
