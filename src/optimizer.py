from src.config import *
from src.variable import best_for_turbo_driver
import copy
from ortools.linear_solver import pywraplp

teams = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team10]
drivers = [team1_driver1, team1_driver2, team2_driver1, team2_driver2, team3_driver1, team3_driver2, team4_driver1, team4_driver2, team5_driver1, team5_driver2, team6_driver1, team6_driver2, team7_driver1, team7_driver2, team8_driver1, team8_driver2, team9_driver1, team9_driver2, team10_driver1, team10_driver2]
n_teams = 1
n_drivers = 5


def print_all_drivers():
    # Print out all the drivers
    for i in range(len(teams)):
        print("___________________________")
        print("TEAM: " + teams[i].name)
        print("\tprice  : " + str(teams[i].price))
        print("\tpoints : " + str(teams[i].points))
        print("\tppm    : " + str(round(teams[i].points / teams[i].price, 2)) + "\n")
        print("\tDRIVER 1 : " + drivers[2 * i].name)
        print("\t\tprice  : " + str(drivers[2 * i].price))
        print("\t\tpoints : " + str(drivers[2 * i].points))
        print("\t\tppm    : " + str(round(drivers[2 * i].points / drivers[2 * i].price, 2)) + "\n")
        print("\tDRIVER 2 : " + drivers[2 * i + 1].name)
        print("\t\tprice  : " + str(drivers[2 * i + 1].price))
        print("\t\tpoints : " + str(drivers[2 * i + 1].points))
        print("\t\tppm    : " + str(round(drivers[2 * i + 1].points / drivers[2 * i + 1].price, 2)))
    print("___________________________\n\n\n\n")


def contains(name, drivers):
    for driver in drivers:
        if driver.name == name:
            return True
    return False


def print_team_expectation(team_t, drivers_d):
    cost = team_t.price
    expected_points = team_t.get_expected_points()
    print("___________________________")
    print("TEAM : " + team_t.name)
    print("\tprice : " + str(team_t.price))
    print("\texpected points : " + str(round(team_t.get_expected_points(), 2)))
    if team_t.substitute:
        print("\tSubstitute penalty of 10 points")
    elif team_t.name != my_team.name:
        print("\tFree substitution")
    if team_t.qualy_bonus:
        print("\tQualifying top 10 bonus with " + str(round(team_t.qualy_top10_ratio, 2)) + " probability")
    if team_t.finish_bonus:
        print("\tFinish top 10 bonus with " + str(round(team_t.finish_top10_ratio, 2)) + " probability")
    for i in range(len(drivers_d)):
        cost += drivers_d[i].price
        expected_points += drivers_d[i].get_expected_points()
        print("___________________________")
        print("DRIVER " + str(i + 1) + " : " + drivers_d[i].name)
        print("\tprice : " + str(drivers_d[i].price))
        print("\texpected points : " + str(round(drivers_d[i].get_expected_points(), 2)))
        if drivers_d[i].turbo_driver:
            print("\tUse turbo driver card")
        if drivers_d[i].substitute:
            print("\tSubstitute penalty of 10 points")
        elif not contains(drivers_d[i].name, my_drivers):
            print("\tFree substitution")
        if drivers_d[i].qualy_bonus:
            print("\tQualifying top 10 bonus with " + str(round(drivers_d[i].qualy_top10_ratio, 2)) + " probability")
        if drivers_d[i].finish_bonus:
            print("\tFinish top 10 bonus with " + str(round(drivers_d[i].finish_top10_ratio, 2)) + " probability")
    print("___________________________")
    print("SUMMARY")
    print("Budget: " + str(budget))
    print("Total price: " + str(round(cost, 1)))
    print("Expected points: " + str(round(expected_points, 2)))
    print("___________________________\n")


if __name__ == '__main__':
    # Print out all teams and drivers
    print_all_drivers()

    if len(my_drivers) != n_drivers:
        raise Exception("Your must have " + str(n_drivers) + " drivers")

    if not wildcard:
        for team in teams:
            if team != my_team:
                team.substitute = True
        for driver in drivers:
            if not driver in my_drivers:
                driver.substitute = True

    # Print out the expected performance for my team next week
    print("CURRENT TEAM EXPECTATION")
    my_team = copy.deepcopy(my_team)
    my_drivers = copy.deepcopy(my_drivers)
    best_for_turbo_driver(my_drivers).turbo_driver = True
    print_team_expectation(my_team, my_drivers)

    optimal_team = None
    optimal_drivers = None
    optimal_expectation = 0
    for d1 in range(len(drivers)):
        for d2 in range(len(drivers) if not wildcard else 1):
            if drivers[d1].price >= 20:
                continue

            # Set this driver as the turbo driver
            drivers[d1].turbo_driver = True

            # give the other driver a free substitution
            sub = drivers[d2].substitute
            drivers[d2].substitute = False

            solver = pywraplp.Solver.CreateSolver("F1 Fantasy solver", "CBC")

            # Declare all model variables
            driver_vars = []
            team_vars = []

            team1_var = solver.IntVar(0, 1, team1.name)
            team1_driver1_var = solver.IntVar(0, 1, team1_driver1.name)
            team1_driver2_var = solver.IntVar(0, 1, team1_driver2.name)
            team_vars.append(team1_var)
            driver_vars.append(team1_driver1_var)
            driver_vars.append(team1_driver2_var)

            team2_var = solver.IntVar(0, 1, team2.name)
            team2_driver1_var = solver.IntVar(0, 1, team2_driver1.name)
            team2_driver2_var = solver.IntVar(0, 1, team2_driver2.name)
            team_vars.append(team2_var)
            driver_vars.append(team2_driver1_var)
            driver_vars.append(team2_driver2_var)

            team3_var = solver.IntVar(0, 1, team3.name)
            team3_driver1_var = solver.IntVar(0, 1, team3_driver1.name)
            team3_driver2_var = solver.IntVar(0, 1, team3_driver2.name)
            team_vars.append(team3_var)
            driver_vars.append(team3_driver1_var)
            driver_vars.append(team3_driver2_var)

            team4_var = solver.IntVar(0, 1, team4.name)
            team4_driver1_var = solver.IntVar(0, 1, team4_driver1.name)
            team4_driver2_var = solver.IntVar(0, 1, team4_driver2.name)
            team_vars.append(team4_var)
            driver_vars.append(team4_driver1_var)
            driver_vars.append(team4_driver2_var)

            team5_var = solver.IntVar(0, 1, team5.name)
            team5_driver1_var = solver.IntVar(0, 1, team5_driver1.name)
            team5_driver2_var = solver.IntVar(0, 1, team5_driver2.name)
            team_vars.append(team5_var)
            driver_vars.append(team5_driver1_var)
            driver_vars.append(team5_driver2_var)

            team6_var = solver.IntVar(0, 1, team6.name)
            team6_driver1_var = solver.IntVar(0, 1, team6_driver1.name)
            team6_driver2_var = solver.IntVar(0, 1, team6_driver2.name)
            team_vars.append(team6_var)
            driver_vars.append(team6_driver1_var)
            driver_vars.append(team6_driver2_var)

            team7_var = solver.IntVar(0, 1, team7.name)
            team7_driver1_var = solver.IntVar(0, 1, team7_driver1.name)
            team7_driver2_var = solver.IntVar(0, 1, team7_driver2.name)
            team_vars.append(team7_var)
            driver_vars.append(team7_driver1_var)
            driver_vars.append(team7_driver2_var)

            team8_var = solver.IntVar(0, 1, team8.name)
            team8_driver1_var = solver.IntVar(0, 1, team8_driver1.name)
            team8_driver2_var = solver.IntVar(0, 1, team8_driver2.name)
            team_vars.append(team8_var)
            driver_vars.append(team8_driver1_var)
            driver_vars.append(team8_driver2_var)

            team9_var = solver.IntVar(0, 1, team9.name)
            team9_driver1_var = solver.IntVar(0, 1, team9_driver1.name)
            team9_driver2_var = solver.IntVar(0, 1, team9_driver2.name)
            team_vars.append(team9_var)
            driver_vars.append(team9_driver1_var)
            driver_vars.append(team9_driver2_var)

            team10_var = solver.IntVar(0, 1, team10.name)
            team10_driver1_var = solver.IntVar(0, 1, team10_driver1.name)
            team10_driver2_var = solver.IntVar(0, 1, team10_driver2.name)
            team_vars.append(team10_var)
            driver_vars.append(team10_driver1_var)
            driver_vars.append(team10_driver2_var)

            # Limit the number of drivers that can be picked
            solver.Add(team1_driver1_var + team1_driver2_var + team2_driver1_var + team2_driver2_var + team3_driver1_var + team3_driver2_var + team4_driver1_var + team4_driver2_var + team5_driver1_var + team5_driver2_var + team6_driver1_var + team6_driver2_var + team7_driver1_var + team7_driver2_var + team8_driver1_var + team8_driver2_var + team9_driver1_var + team9_driver2_var + team10_driver1_var + team10_driver2_var == n_drivers)

            # Limit the number of teams that can be picked
            solver.Add(team1_var + team2_var + team3_var + team4_var + team5_var + team6_var + team7_var + team8_var + team9_var + team10_var == n_teams)

            # Limit the budget
            solver.Add(team1_driver1_var * team1_driver1.price + team1_driver2_var * team1_driver2.price + team2_driver1_var * team2_driver1.price + team2_driver2_var * team2_driver2.price + team3_driver1_var * team3_driver1.price + team3_driver2_var * team3_driver2.price + team4_driver1_var * team4_driver1.price + team4_driver2_var * team4_driver2.price + team5_driver1_var * team5_driver1.price + team5_driver2_var * team5_driver2.price + team6_driver1_var * team6_driver1.price + team6_driver2_var * team6_driver2.price + team7_driver1_var * team7_driver1.price + team7_driver2_var * team7_driver2.price + team8_driver1_var * team8_driver1.price + team8_driver2_var * team8_driver2.price + team9_driver1_var * team9_driver1.price + team9_driver2_var * team9_driver2.price + team10_driver1_var * team10_driver1.price + team10_driver2_var * team10_driver2.price + team1_var * team1.price + team2_var * team2.price + team3_var * team3.price + team4_var * team4.price + team5_var * team5.price + team6_var * team6.price + team7_var * team7.price + team8_var * team8.price + team9_var * team9.price + team10_var * team10.price <= budget)

            # Define the max function
            solver.Maximize(team1_driver1_var * team1_driver1.get_expected_points() + team1_driver2_var * team1_driver2.get_expected_points() + team2_driver1_var * team2_driver1.get_expected_points() + team2_driver2_var * team2_driver2.get_expected_points() + team3_driver1_var * team3_driver1.get_expected_points() + team3_driver2_var * team3_driver2.get_expected_points() + team4_driver1_var * team4_driver1.get_expected_points() + team4_driver2_var * team4_driver2.get_expected_points() + team5_driver1_var * team5_driver1.get_expected_points() + team5_driver2_var * team5_driver2.get_expected_points() + team6_driver1_var * team6_driver1.get_expected_points() + team6_driver2_var * team6_driver2.get_expected_points() + team7_driver1_var * team7_driver1.get_expected_points() + team7_driver2_var * team7_driver2.get_expected_points() + team8_driver1_var * team8_driver1.get_expected_points() + team8_driver2_var * team8_driver2.get_expected_points() + team9_driver1_var * team9_driver1.get_expected_points() + team9_driver2_var * team9_driver2.get_expected_points() + team10_driver1_var * team10_driver1.get_expected_points() + team10_driver2_var * team10_driver2.get_expected_points() + team1_var * team1.get_expected_points() + team2_var * team2.get_expected_points() + team3_var * team3.get_expected_points() + team4_var * team4.get_expected_points() + team5_var * team5.get_expected_points() + team6_var * team6.get_expected_points() + team7_var * team7.get_expected_points() + team8_var * team8.get_expected_points() + team9_var * team9.get_expected_points() + team10_var * team10.get_expected_points())

            # Solve the system
            status = solver.Solve()

            optimal_team_t = None
            optimal_drivers_t = []
            expected_points = 0
            if status == pywraplp.Solver.OPTIMAL:
                for i in range(len(team_vars)):
                    if team_vars[i].solution_value() == 1:
                        optimal_team_t = copy.deepcopy(teams[i])
                        expected_points += optimal_team_t.get_expected_points()
                for i in range(len(driver_vars)):
                    if driver_vars[i].solution_value() == 1:
                        optimal_drivers_t.append(copy.deepcopy(drivers[i]))
                        expected_points += drivers[i].get_expected_points()

                if expected_points > optimal_expectation:
                    optimal_expectation = expected_points
                    optimal_team = optimal_team_t
                    optimal_drivers = optimal_drivers_t

            # Remove the drivers turbo driver
            drivers[d1].turbo_driver = False

            # Reset the free substitution
            drivers[d2].substitute = sub

    print("OPTIMAL EXPECTATION " + ("WITH" if wildcard else "WITHOUT") + " WILDCARD")
    print_team_expectation(optimal_team, optimal_drivers)
