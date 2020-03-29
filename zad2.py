import random


def get_hood(x=None):
    if x is None:
        x = []

    hood = []

    for i in range(len(x) - 1):
        for j in range(len(x) - 1 - i):
            hood.append([i, i + j + 1])

    return hood


def get_dist():
    dist_arr = []

    line = input().split()
    dist_arr.append([int(line[0])])

    for i in range(int(line[1])):
        line = input().split()
        dist_arr.append(list(map(int, line)))

    return dist_arr


def rand_start(n):
    nums = []
    rand_path = []

    for i in range(n):
        nums.append(i)

    for i in range(n):
        idx = round(random.randint(0, n-i-1))
        rand_path.append(nums[idx])
        nums.pop(idx)

    return rand_path


dist = get_dist()
time = dist.pop(0)
print("distances: ", dist)

my_path = rand_start(len(dist))
print("my random path: ", my_path)

my_hood = get_hood(my_path)
print("indx fo swap: ", my_hood)


