with open("9c211d5a025011ea.txt.clean.txt") as file:
    data = file.readlines()
n = int(data[0])
velocity = [int(x) for x in data[1]]
position = [int(x) for x in data[2]]


# def find_overtakes(velocity, position, n):
#     number_of_overtakes = 0
#     for i in range(n-1):
#         if (velocity[i] > velocity[i+1]) and (position[i+1] <= (position[i] + 1)) :
#             number_of_overtakes += 1

#     return number_of_overtakes


# n = int(input_val[0])
# velocity = [int(x) for x in input_val[1].split()]
# position = [int(x) for x in input_val[2].split()]

# print(find_overtakes(velocity, position, n))
