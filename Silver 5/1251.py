import sys

str = sys.stdin.readline().rstrip()

list = []

for i in range(1, len(str) - 1):

    for j in range(i + 1, len(str)):

        str1 = str[0:i][::-1]
        str2 = str[i:j][::-1]
        str3 = str[j:len(str)][::-1]


        list.append(str1 + str2 + str3)

print(sorted(list)[0])