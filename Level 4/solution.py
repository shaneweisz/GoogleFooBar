#####################
##### Solution ######
#####################

def solution(times, times_limit):
    shortest_paths = floyd(times)
    pass


def time_to_collect(bunnies_list, shortest_paths):
    first_bunny = bunnies_list[0]
    s = shortest_paths[0][first_bunny]
    for a, b in zip(bunnies_list, bunnies_list[1:]):
        s += shortest_paths[a][b]
    last_bunny = bunnies_list[-1]
    s += shortest_paths[last_bunny][-1]
    return s


def floyd(times):
    shortest_paths = times.copy()
    n = len(times)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                shortest_paths[i][j] = min(shortest_paths[i][j],
                                           shortest_paths[i][k] + shortest_paths[k][j])
    return shortest_paths

#####################
#### Test Cases #####
#####################


def check_test_case(i, inp, exp_out):
    print("-"*20)
    print("Test Case", i)

    out = solution(*inp)
    print("Output:", out)
    print("Expected:", exp_out)

    print("PASSED" if out == exp_out else "FAILED")


def run_all_tests(inputs, expected_outputs):
    for i, (inp, exp_out) in enumerate(zip(inputs, expected_outputs), start=1):
        check_test_case(i, inp, exp_out)


def main():
    inputs = [([[0, 2, 2, 2, -1],
                [9, 0, 2, 2, -1],
                [9, 3, 0, 2, -1],
                [9, 3, 2, 0, -1],
                [9, 3, 2, 2, 0]], 1),
              ([[0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1],
                  [1, 1, 0, 1, 1],
                  [1, 1, 1, 0, 1],
                  [1, 1, 1, 1, 0]], 3)]

    expected_outputs = [[1, 2], [0, 1]]

    # run_all_tests(inputs, expected_outputs)

    shortest_paths = floyd(inputs[0][0])

    print(shortest_paths)

    bunnies_list = [2, 3]
    print(time_to_collect(bunnies_list, shortest_paths))


if __name__ == '__main__':
    main()
