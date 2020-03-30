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
    print('1st path: ', my_path)
    best = []
    best_cand = []
    finished = 0
    walked = []

    curr_pos = wheres_waldo(my_map)
    my_hood = [my_path]

    t_start = perf_counter()
    while time - (perf_counter() - t_start) > 0:
        for neighbor in my_hood:
            if finished == 1:
                curr_pos = wheres_waldo(my_map)
                print('successful: ', walked)

                walked.clear()

                finished = 0
            else:
                my_path = randomize(my_path)

            print(curr_pos)
            print(neighbor)
            for idx in range(len(neighbor)):
                if neighbor[idx] == 0:  # RIGHT
                    if my_map[curr_pos[0]][curr_pos[1] + 1] != 1:
                        curr_pos[1] += 1
                        walked.append(0)

                if neighbor[idx] == 1:  # LEFT
                    if my_map[curr_pos[0]][curr_pos[1] - 1] != 1:
                        curr_pos[1] -= 1
                        walked.append(1)

                if neighbor[idx] == 2:  # DOWN
                    if my_map[curr_pos[0] + 1][curr_pos[1]] != 1:
                        curr_pos[0] += 1
                        walked.append(2)

                if neighbor[idx] == 3:  # UP
                    if my_map[curr_pos[0] - 1][curr_pos[1]] != 1:
                        curr_pos[0] -= 1
                        walked.append(3)

                if my_map[curr_pos[0]][curr_pos[1]] == 8:
                    print('finished')
                    finished = 1
                    try:
                        if len(walked) < len(best[0]):
                            best[0] = walked[::]
                    except IndexError:
                        best.append(walked[::])

                    try:
                        if len(walked) < len(best_cand[0]):
                            best_cand[0] = walked[::]
                    except IndexError:
                        best_cand.append(walked[::])

                    my_path = best_cand[0]
                    my_hood = get_hood(my_path)

                    break

    print(walked)
    return best[0]


def get_hood(my_path):
    my_hood = []

    for i in range(round(len(my_path)/2)):
        idx = whole_rand(len(my_path)-1)
        my_path[idx] = whole_rand(3)
        my_hood.append(my_path[:])

    return my_hood


le_inputo = get_input()
print("best: ", search_lab(le_inputo))

# print(le_inputo)
# print(gen_seq())
# da_map = [[1, 1, 1, 1], [1, 0, 0, 1], [8, 0, 0, 1], [1, 5, 0, 1], [1, 1, 1, 1]]
# print(wheres_waldo(da_map))
# print(get_hood([0, 0, 0, 0, 0, 0, 0]))
