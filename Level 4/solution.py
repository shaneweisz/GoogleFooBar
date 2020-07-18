#####################
##### Solution ######
#####################

def solution(times, times_limit):
    # Your code here
    pass


class Configuration:
    pass


class State:
    def __init__(self, grid, current_time_taken, times_limit):
        pass

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

    run_all_tests(inputs, expected_outputs)


if __name__ == '__main__':
    main()
