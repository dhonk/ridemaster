from ridemaster.main import *

if __name__ == '__main__':
    drive1 = driver((0, 0), 3)
    drive2 = driver((10, 10), 2)

    ride1 = rider((0, 1))
    ride2 = rider((1, 0))
    ride3 = rider((5, 9))

    drives = [drive1, drive2]
    rides = [ride1, ride2, ride3, rider((2, 8)), rider((5, 5)), rider((1, 3)), rider((11,11))]

    soln = solve(drives, rides)
    soln.init_dists()
    soln.show_distances()

    soln.find_routes()
    soln.show_routes()
