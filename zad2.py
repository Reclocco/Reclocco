from __future__ import print_function
import sys
import random
from time import perf_counter


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_hood(x):
    hood = []

    for i in range(x - 1):
        for j in range(x - 1 - i):
            hood.append([i, i + j + 1])

    return hood


def get_dist():
    dist_arr = []

    line = input().split()
    dist_arr.append(int(line[0]))

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
        idx = round(random.randint(0, n - i - 1))
        rand_path.append(nums[idx])
        nums.pop(idx)

    return rand_path


def swap_nodes(path=[], idxs=[]):
    tmp1 = path[:]
    tmp = tmp1[idxs[0]]
    tmp1[idxs[0]] = tmp1[idxs[1]]
    tmp1[idxs[1]] = tmp

    return tmp1


def calc_dist(path=[], dist_table=[]):
    dist = 0

    for i in range(len(path) - 1):
        dist += dist_table[path[i]][path[i + 1]]

    dist += dist_table[path[-1]][path[0]]

    return dist


def search_tsp(curr_path, dist_table, time):
    best_candidate = curr_path
    best_path = curr_path
    tabu = []
    max_tabu = 50
    t_start = perf_counter()

    while time - (perf_counter() - t_start) > 0:
        for swap in get_hood(len(curr_path)):
            if swap_nodes(curr_path, swap) not in tabu:

                if calc_dist(swap_nodes(curr_path, swap), dist_table) < calc_dist(curr_path, dist_table):
                    best_candidate = swap_nodes(curr_path, swap)[::]

        if best_candidate == curr_path:
            curr_path = rand_start(len(curr_path))
        else:
            curr_path = best_candidate

        tabu += best_candidate
        if len(tabu) > max_tabu:
            tabu.pop(0)

        if calc_dist(best_candidate, dist_table) < calc_dist(best_path, dist_table):
            best_path = best_candidate[::]

    return best_path


my_dist = get_dist()
my_time = int(my_dist.pop(0))
my_path = rand_start(len(my_dist))
my_hood = get_hood(len(my_path))

my_best = search_tsp(my_path, my_dist, my_time)

print(calc_dist(my_best, my_dist))
eprint(my_best)
