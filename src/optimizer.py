from src.config import *
from ortools.linear_solver import pywraplp

if __name__ == '__main__':

    solver = pywraplp.Solver.CreateSolver("F1 Fantasy solver", "CBC")

    # Declare all model variables
    drivers = []
    driver_vars = []
    teams = []
    team_vars = []

    team1_var = solver.IntVar(0, 1, team1.name)
    team1_driver1_var = solver.IntVar(0, 1, team1_driver1.name)
    team1_driver2_var = solver.IntVar(0, 1, team1_driver2.name)
    teams.append(team1)
    team_vars.append(team1_var)
    drivers.append(team1_driver1)
    drivers.append(team1_driver2)
    driver_vars.append(team1_driver1_var)
    driver_vars.append(team1_driver2_var)

    team2_var = solver.IntVar(0, 1, team2.name)
    team2_driver1_var = solver.IntVar(0, 1, team2_driver1.name)
    team2_driver2_var = solver.IntVar(0, 1, team2_driver2.name)
    teams.append(team2)
    team_vars.append(team2_var)
    drivers.append(team2_driver1)
    drivers.append(team2_driver2)
    driver_vars.append(team2_driver1_var)
    driver_vars.append(team2_driver2_var)

    team3_var = solver.IntVar(0, 1, team3.name)
    team3_driver1_var = solver.IntVar(0, 1, team3_driver1.name)
    team3_driver2_var = solver.IntVar(0, 1, team3_driver2.name)
    teams.append(team3)
    team_vars.append(team3_var)
    drivers.append(team3_driver1)
    drivers.append(team3_driver2)
    driver_vars.append(team3_driver1_var)
    driver_vars.append(team3_driver2_var)

    team4_var = solver.IntVar(0, 1, team4.name)
    team4_driver1_var = solver.IntVar(0, 1, team4_driver1.name)
    team4_driver2_var = solver.IntVar(0, 1, team4_driver2.name)
    teams.append(team4)
    team_vars.append(team4_var)
    drivers.append(team4_driver1)
    drivers.append(team4_driver2)
    driver_vars.append(team4_driver1_var)
    driver_vars.append(team4_driver2_var)

    team5_var = solver.IntVar(0, 1, team5.name)
    team5_driver1_var = solver.IntVar(0, 1, team5_driver1.name)
    team5_driver2_var = solver.IntVar(0, 1, team5_driver2.name)
    teams.append(team5)
    team_vars.append(team5_var)
    drivers.append(team5_driver1)
    drivers.append(team5_driver2)
    driver_vars.append(team5_driver1_var)
    driver_vars.append(team5_driver2_var)

    team6_var = solver.IntVar(0, 1, team6.name)
    team6_driver1_var = solver.IntVar(0, 1, team6_driver1.name)
    team6_driver2_var = solver.IntVar(0, 1, team6_driver2.name)
    teams.append(team6)
    team_vars.append(team6_var)
    drivers.append(team6_driver1)
    drivers.append(team6_driver2)
    driver_vars.append(team6_driver1_var)
    driver_vars.append(team6_driver2_var)

    team7_var = solver.IntVar(0, 1, team7.name)
    team7_driver1_var = solver.IntVar(0, 1, team7_driver1.name)
    team7_driver2_var = solver.IntVar(0, 1, team7_driver2.name)
    teams.append(team7)
    team_vars.append(team7_var)
    drivers.append(team7_driver1)
    drivers.append(team7_driver2)
    driver_vars.append(team7_driver1_var)
    driver_vars.append(team7_driver2_var)

    team8_var = solver.IntVar(0, 1, team8.name)
    team8_driver1_var = solver.IntVar(0, 1, team8_driver1.name)
    team8_driver2_var = solver.IntVar(0, 1, team8_driver2.name)
    teams.append(team8)
    team_vars.append(team8_var)
    drivers.append(team8_driver1)
    drivers.append(team8_driver2)
    driver_vars.append(team8_driver1_var)
    driver_vars.append(team8_driver2_var)

    team9_var = solver.IntVar(0, 1, team9.name)
    team9_driver1_var = solver.IntVar(0, 1, team9_driver1.name)
    team9_driver2_var = solver.IntVar(0, 1, team9_driver2.name)
    teams.append(team9)
    team_vars.append(team9_var)
    drivers.append(team9_driver1)
    drivers.append(team9_driver2)
    driver_vars.append(team9_driver1_var)
    driver_vars.append(team9_driver2_var)

    team10_var = solver.IntVar(0, 1, team10.name)
    team10_driver1_var = solver.IntVar(0, 1, team10_driver1.name)
    team10_driver2_var = solver.IntVar(0, 1, team10_driver2.name)
    teams.append(team10)
    team_vars.append(team10_var)
    drivers.append(team10_driver1)
    drivers.append(team10_driver2)
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

    # Print out all the drivers
    for i in range(len(teams)):
        print("___________________________\n")
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

    if status == pywraplp.Solver.OPTIMAL:
        total_cost = 0
        total_points = solver.Objective().Value()
        print("SOLUTION")
        for i in range(len(team_vars)):
            if team_vars[i].solution_value() == 1:
                print("___________________________\n")
                print("TEAM : " + teams[i].name)
                print("\tprice  : " + str(teams[i].price))
                print("\texpected points : " + str(round(teams[i].get_expected_points(), 2)))
                total_cost += teams[i].price
        for i in range(len(driver_vars)):
            if driver_vars[i].solution_value() == 1:
                print("___________________________\n")
                print("DRIVER : " + drivers[i].name)
                print("\tprice  : " + str(drivers[i].price))
                print("\texpected points : " + str(round(drivers[i].get_expected_points(), 2)))
                total_cost += drivers[i].price
        print("___________________________\n\n")
        print("Budget: " + str(budget))
        print("Total cost: " + str(round(total_cost)))
        print("Total expected points: " + str(round(total_points, 2)))
    else:
        print("The problem does not have an optimal solution...")
