switch_count = int(input())

onandoff = list(input().split())

students = int(input())

recipe = []

for _ in range(students):
    gender, number = map(int, input().split())
    recipe.append((gender, number))

for gender, number in recipe:
    if gender == 1:
        for i in range(number - 1, switch_count, number):
            if onandoff[i] == '1':
                onandoff[i] = '0'
            else:
                onandoff[i] = '1'
    else:
        left = number - 1
        right = number - 1

        if onandoff[left] == '1':
            onandoff[left] = '0'
        else:
            onandoff[left] = '1'

        while left > 0 and right < switch_count - 1:
            left -= 1
            right += 1
            if onandoff[left] == onandoff[right]:
                if onandoff[left] == '1':
                    onandoff[left] = '0'
                else:
                    onandoff[left] = '1'

                if onandoff[right] == '1':
                    onandoff[right] = '0'
                else:
                    onandoff[right] = '1'
            else:
                break

line_size = 20

for i in range(0, len(onandoff), line_size):
    line = onandoff[i:i + line_size]
    print(' '.join(line))
