import sys

while(1):
    n = int(sys.stdin.readline())

    if n == 0:
        break

    name = []

    height = []

    max = 0

    for _ in range(n):
        input_name, input_height = map(str, sys.stdin.readline().rstrip().split())

        input_height = float(input_height)
        name.append(input_name)
        height.append(input_height)

        if max < input_height:
            max = input_height


    for i in range(n):
        if height[i] == max:
            print(name[i], end = ' ')

