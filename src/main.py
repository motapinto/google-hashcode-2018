from solvers.car_genetic import car_genetic
from solvers.hill_climbing import hill_climbing
from solvers.rides_genetic import rides_genetic
from solvers.simulated_annealing import simulated_annealing
from solvers.greedy import greedy
from solvers.files import group
from solvers.car_genetic import print_car_genetic_info
from solvers.rides_genetic import print_rides_genetic_info

import sys
import time


def run(algorithm):
    global_score = 0
    # print("\n{}".format(algorithm.__name__.upper()))

    if len(sys.argv) == 3:
        start_time = time.time()
        score = algorithm(sys.argv[2])

        print(sys.argv[2].ljust(20) + "time {:.4f}s \tscore {}".
              format(time.time() - start_time, group(score)))

    else:
        # save start time in start to count total time
        start_time = time.time()
        start = start_time
        score = algorithm("a_example")
        global_score += score

        print("{} time {:08.4f}s \tscore {}".
              format("a_example".ljust(20, ' '), time.time() - start_time, group(score)))

        start_time = time.time()
        score = algorithm("b_should_be_easy")
        global_score += score
        print("{} time {:08.4f}s \tscore {}".
              format("b_should_be_easy".ljust(20, ' '), time.time() - start_time, group(score)))

        start_time = time.time()
        score = algorithm("c_no_hurry")
        global_score += score
        print("{} time {:08.4f}s \tscore {}".
              format("c_no_hurry".ljust(20, ' '), time.time() - start_time, group(score)))

        start_time = time.time()
        score = algorithm("d_metropolis")
        global_score += score
        print("{} time {:08.4f}s \tscore {}".
              format("d_metropolis".ljust(20, ' '), time.time() - start_time, group(score)))

        start_time = time.time()
        score = algorithm("e_high_bonus")
        global_score += score
        print("{} time {:08.4f}s \tscore {}".
              format("e_high_bonus".ljust(20, ' '), time.time() - start_time, group(score)))

        print("\nGlobal score is {}".format(group(global_score)))
        print("Total runtime is {:.4f}s".format(time.time() - start))


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("python main.py <algorithm> <specific file>  ---> For a specific file")
        print("python main.py <algorithm>                  ---> For all test files\n")
        print("algorithm options: car_genetic | greedy | hill_climbing | rides_genetic | simulated_annealing")
        print("file options:      a_example | b_should_be_easy | c_no_hurry | d_metropolis | e_high_bonus\n")
        print("Try again...")
        exit(1)

    if sys.argv[1] == "car_genetic":
        print_car_genetic_info()
        run(car_genetic)
    elif sys.argv[1] == "hill_climbing":
        print("\nHILL CLIMBING")
        run(hill_climbing)
    elif sys.argv[1] == "rides_genetic":
        print_rides_genetic_info()
        run(rides_genetic)
    elif sys.argv[1] == "simulated_annealing":
        print("\nSIMULATED ANNEALING")
        run(simulated_annealing)
    elif sys.argv[1] == "greedy":
        print("\nGREEDY")
        run(greedy)
