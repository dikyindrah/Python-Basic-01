# Nested Loop

print('\n==========Nested Loop==========\n')


perkalian = 2
hasil_perkalian = 0

for i in range(perkalian, perkalian+1):
    for j in range(1, 10+1):
        hasil_perkalian = i * j
        print(i, '*', j,'=', hasil_perkalian)

# start = 2
# stop  = 5

# for i in range(start, stop+1):
#     print('')
#     for j in range(1, 10+1):
#         print(i, '*', j, '=', (i*j))

# i = 2
# while (i < 3):
#     j = 1
#     while (j <= 10):
#         print(i, '*', j, '=', (i * j))
#         j = j + 1
#     i = i + 1

# i = 1
# while (i <= 3):
#     print('')
#     j = 1
#     while (j <= 10):
#         print(i, '*', j, '=', (i * j))
#         j = j + 1
#     i = i + 1