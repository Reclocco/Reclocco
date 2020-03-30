import random
from time import perf_counter


def nums(n):
    num = []
    for i in range(n):
        num.append(i)

    return num


def my_split(line):
    return list(map(int, [digit for digit in line]))


def whole_rand(n):
    return round(random.randint(0, n))


def get_input():
    my_input = []
    line = input().split()
    my_input.append(int(line[0]))
    my_input.append(int(line[1]))
    my_input.append(int(line[2]))

    for i in range(my_input[1]):
        my_input.append(my_split(input()))

    return my_input


def gen_seq():
    my_seq = []
    for i in range(20):
        my_seq.append(whole_rand(3))

    return my_seq


def randomize(my_path):
    for i in range(2):
        idx = whole_rand(len(my_path)-1)
        my_path[idx] = whole_rand(3)

    return my_path


def wheres_waldo(my_map):
    waldo = [0, 0]

    for i in range(len(my_map)):
        for j in range(len(my_map[1])):
            if my_map[i][j] == 5:
                waldo = [i, j]

    return waldo


def search_lab(my_map):
    time = my_map.pop(0)
    my_map.pop(1)
    my_map.pop(0)

    my_path = gen_seq()
    print(my_path)
    my_hood = []
    best = my_path
    finished = 1

    t_start = perf_counter()
    while time - (perf_counter() - t_start) > 0:
        walked = []
        my_hood = get_hood(my_path)
        if finished == 1:
            curr_pos = wheres_waldo(my_map)
            finished = 0
        else:
            my_path = randomize(my_path)

        idx = 0
        print(curr_pos)

        for _ in range(len(my_path)):
            if my_path[idx % len(my_path)] == 0:  # RIGHT
                if my_map[curr_pos[0]][curr_pos[1] + 1] != 1:
                    curr_pos[1] += 1
                    walked.append(0)

            if my_path[idx % len(my_path)] == 1:  # LEFT
                if my_map[curr_pos[0]][curr_pos[1] - 1] != 1:
                    curr_pos[1] -= 1
                    walked.append(1)

            if my_path[idx % len(my_path)] == 2:  # DOWN
                if my_map[curr_pos[0] + 1][curr_pos[1]] != 1:
                    curr_pos[0] += 1
                    walked.append(2)

            if my_path[idx % len(my_path)] == 3:  #UP
                if my_map[curr_pos[0] - 1][curr_pos[1]] != 1:
                    curr_pos[0] -= 1
                    walked.append(3)

            idx += 1
            # print(curr_pos)
            if my_map[curr_pos[0]][curr_pos[1]] == 8:
                finished = 1
                print('finished')
                break


def get_hood(my_path):
    my_hood = []

    for i in range(round(len(my_path)/2)):
        idx = whole_rand(len(my_path)-1)
        my_path[idx] = whole_rand(3)
        my_hood.append(my_path[:])

    return my_hood


le_inputo = get_input()
search_lab(le_inputo)

# print(le_inputo)
# print(gen_seq())
# da_map = [[1, 1, 1, 1], [1, 0, 0, 1], [8, 0, 0, 1], [1, 5, 0, 1], [1, 1, 1, 1]]
# print(wheres_waldo(da_map))
# print(get_hood([0, 0, 0, 0, 0, 0, 0]))
