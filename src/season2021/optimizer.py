from src.season2021.config import *
from src.season2021.variable import Team, Driver
from ortools.linear_solver import pywraplp

all_teams = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team10]
all_drivers = [team1_driver1, team1_driver2, team2_driver1, team2_driver2, team3_driver1, team3_driver2, team4_driver1, team4_driver2, team5_driver1, team5_driver2, team6_driver1, team6_driver2, team7_driver1, team7_driver2, team8_driver1, team8_driver2, team9_driver1, team9_driver2, team10_driver1, team10_driver2]


class FantasyTeam:
    def __init__(self, team: Team, drivers: list, budget, GP_number, subs: int = 0):
        self.team = team
        self.drivers = drivers
        self.GP_number = GP_number
        self.budget = budget
        self.subs = subs

        if self.get_price() > budget:
            raise Exception("You cannot afford this team")

        if len(drivers) != 5:
            raise Exception("Fantasy team must be at 5 drivers")

    def to_string(self, indents: int = 0):
        indent_str = "".join(["\t" for i in range(indents)]) if indents > 0 else ""
        team_str = ""
        team_str += "\n" + indent_str + "GP: " + GPs[self.GP_number]
        team_str += "\n" + indent_str + "Team: " + self.team.name
        team_str += "\n" + indent_str + "\tPrice: " + str(self.team.get_price(self.GP_number))
        team_str += "\n" + indent_str + "\tExpected Points: " + str(self.team.get_expected_points(self.GP_number))
        if self.GP_number < self.team.N_GP:
            team_str += "\n" + indent_str + "\tActual Points: " + str(self.team.get_points(self.GP_number))
        for i in range(len(self.drivers)):
            team_str += "\n" + indent_str + "Driver " + str(i + 1) + ": " + self.drivers[i].name
            team_str += "\n" + indent_str + "\tPrice: " + str(self.drivers[i].get_price(self.GP_number))
            team_str += "\n" + indent_str + "\tExpected Points: " + str(self.drivers[i].get_expected_points(self.GP_number))
            if self.GP_number < self.team.N_GP:
                team_str += "\n" + indent_str + "\tActual Points: " + str(self.drivers[i].get_points(self.GP_number))
        if self.subs > 3:
            team_str += "\n" + indent_str + str(self.subs - 3) + "0 points penalty for " + str(self.subs) + " substitutions"
        team_str += "\n" + indent_str + "Total Team Price: " + str(self.get_price())
        team_str += "\n" + indent_str + "Total Budget: " + str(self.budget)
        team_str += "\n" + indent_str + "Total Expected Points: " + str(self.get_expected_points()) + " with turbo-driver " + self.best_expected_turbo_driver().name
        if self.GP_number < self.team.N_GP:
            team_str += "\n" + indent_str + "Total Actual Points: " + str(self.get_points()) + " with turbo-driver " + self.best_turbo_driver().name

        return team_str

    def best_turbo_driver(self):
        max_points = 0
        turbo_driver = None
        for driver in self.drivers:
            if driver.get_price(self.GP_number) <= 20 and driver.get_expected_points(self.GP_number) > max_points:
                max_points = driver.get_points(self.GP_number)
                turbo_driver = driver
        return turbo_driver

    def best_expected_turbo_driver(self):
        max_points = 0
        turbo_driver = None
        for driver in self.drivers:
            if driver.get_price(self.GP_number) <= 20 and driver.get_expected_points(self.GP_number) > max_points:
                max_points = driver.get_expected_points(self.GP_number)
                turbo_driver = driver
        return turbo_driver

    def get_points(self):
        points = self.team.get_points(self.GP_number)
        turbo_driver = self.best_turbo_driver()
        for driver in self.drivers:
            if driver == turbo_driver:
                points += driver.get_points(self.GP_number) * 2
            else:
                points += driver.get_points(self.GP_number)
        if self.subs > 3:
            points -= (self.subs - 3) * 10
        return points

    def get_expected_points(self):
        points = self.team.get_expected_points(self.GP_number)
        turbo_driver = self.best_expected_turbo_driver()
        for driver in self.drivers:
            if driver == turbo_driver:
                points += driver.get_expected_points(self.GP_number) * 2
            else:
                points += driver.get_expected_points(self.GP_number)
        if self.subs > 3:
            points -= (self.subs - 3) * 10
        return points

    def get_team_hash(self):
        driver_names = map(lambda driver: driver.name, self.drivers)
        driver_names = sorted(driver_names)
        return str(self.GP_number + "_" + self.team.name + '_' + '_'.join(driver_names))

    def get_price(self):
        total_price = self.team.get_price(self.GP_number)
        for driver in self.drivers:
            total_price += driver.get_price(self.GP_number)

        return total_price

    def get_budget(self):
        return self.budget


def get_best_team(budget, GP_number: int, expectation: bool=False, subs: int = -1, not_in_team: list = []):
    solver = pywraplp.Solver.CreateSolver("F1 Fantasy solver", "CBC")

    # Declare all model variables
    driver_vars = []
    team_vars = []

    team1_var = solver.IntVar(0, 1, team1.name)
    team1_driver1_var = solver.IntVar(0, 1, team1_driver1.name)
    team1_driver2_var = solver.IntVar(0, 1, team1_driver2.name)
    team1_points = team1.get_expected_points(GP_number) if expectation else team1.get_points(GP_number)
    team1_driver1_points = team1_driver1.get_expected_points(GP_number) if expectation else team1_driver1.get_points(GP_number)
    team1_driver2_points = team1_driver2.get_expected_points(GP_number) if expectation else team1_driver2.get_points(GP_number)
    team_vars.append(team1_var)
    driver_vars.append(team1_driver1_var)
    driver_vars.append(team1_driver2_var)

    team2_var = solver.IntVar(0, 1, team2.name)
    team2_driver1_var = solver.IntVar(0, 1, team2_driver1.name)
    team2_driver2_var = solver.IntVar(0, 1, team2_driver2.name)
    team2_points = team2.get_expected_points(GP_number) if expectation else team2.get_points(GP_number)
    team2_driver1_points = team2_driver1.get_expected_points(GP_number) if expectation else team2_driver1.get_points(GP_number)
    team2_driver2_points = team2_driver2.get_expected_points(GP_number) if expectation else team2_driver2.get_points(GP_number)
    team_vars.append(team2_var)
    driver_vars.append(team2_driver1_var)
    driver_vars.append(team2_driver2_var)

    team3_var = solver.IntVar(0, 1, team3.name)
    team3_driver1_var = solver.IntVar(0, 1, team3_driver1.name)
    team3_driver2_var = solver.IntVar(0, 1, team3_driver2.name)
    team3_points = team3.get_expected_points(GP_number) if expectation else team3.get_points(GP_number)
    team3_driver1_points = team3_driver1.get_expected_points(GP_number) if expectation else team3_driver1.get_points(GP_number)
    team3_driver2_points = team3_driver2.get_expected_points(GP_number) if expectation else team3_driver2.get_points(GP_number)
    team_vars.append(team3_var)
    driver_vars.append(team3_driver1_var)
    driver_vars.append(team3_driver2_var)

    team4_var = solver.IntVar(0, 1, team4.name)
    team4_driver1_var = solver.IntVar(0, 1, team4_driver1.name)
    team4_driver2_var = solver.IntVar(0, 1, team4_driver2.name)
    team4_points = team4.get_expected_points(GP_number) if expectation else team4.get_points(GP_number)
    team4_driver1_points = team4_driver1.get_expected_points(GP_number) if expectation else team4_driver1.get_points(GP_number)
    team4_driver2_points = team4_driver2.get_expected_points(GP_number) if expectation else team4_driver2.get_points(GP_number)
    team_vars.append(team4_var)
    driver_vars.append(team4_driver1_var)
    driver_vars.append(team4_driver2_var)

    team5_var = solver.IntVar(0, 1, team5.name)
    team5_driver1_var = solver.IntVar(0, 1, team5_driver1.name)
    team5_driver2_var = solver.IntVar(0, 1, team5_driver2.name)
    team5_points = team5.get_expected_points(GP_number) if expectation else team5.get_points(GP_number)
    team5_driver1_points = team5_driver1.get_expected_points(GP_number) if expectation else team5_driver1.get_points(GP_number)
    team5_driver2_points = team5_driver2.get_expected_points(GP_number) if expectation else team5_driver2.get_points(GP_number)
    team_vars.append(team5_var)
    driver_vars.append(team5_driver1_var)
    driver_vars.append(team5_driver2_var)

    team6_var = solver.IntVar(0, 1, team6.name)
    team6_driver1_var = solver.IntVar(0, 1, team6_driver1.name)
    team6_driver2_var = solver.IntVar(0, 1, team6_driver2.name)
    team6_points = team6.get_expected_points(GP_number) if expectation else team6.get_points(GP_number)
    team6_driver1_points = team6_driver1.get_expected_points(GP_number) if expectation else team6_driver1.get_points(GP_number)
    team6_driver2_points = team6_driver2.get_expected_points(GP_number) if expectation else team6_driver2.get_points(GP_number)
    team_vars.append(team6_var)
    driver_vars.append(team6_driver1_var)
    driver_vars.append(team6_driver2_var)

    team7_var = solver.IntVar(0, 1, team7.name)
    team7_driver1_var = solver.IntVar(0, 1, team7_driver1.name)
    team7_driver2_var = solver.IntVar(0, 1, team7_driver2.name)
    team7_points = team7.get_expected_points(GP_number) if expectation else team7.get_points(GP_number)
    team7_driver1_points = team7_driver1.get_expected_points(GP_number) if expectation else team7_driver1.get_points(GP_number)
    team7_driver2_points = team7_driver2.get_expected_points(GP_number) if expectation else team7_driver2.get_points(GP_number)
    team_vars.append(team7_var)
    driver_vars.append(team7_driver1_var)
    driver_vars.append(team7_driver2_var)

    team8_var = solver.IntVar(0, 1, team8.name)
    team8_driver1_var = solver.IntVar(0, 1, team8_driver1.name)
    team8_driver2_var = solver.IntVar(0, 1, team8_driver2.name)
    team8_points = team8.get_expected_points(GP_number) if expectation else team8.get_points(GP_number)
    team8_driver1_points = team8_driver1.get_expected_points(GP_number) if expectation else team8_driver1.get_points(GP_number)
    team8_driver2_points = team8_driver2.get_expected_points(GP_number) if expectation else team8_driver2.get_points(GP_number)
    team_vars.append(team8_var)
    driver_vars.append(team8_driver1_var)
    driver_vars.append(team8_driver2_var)

    team9_var = solver.IntVar(0, 1, team9.name)
    team9_driver1_var = solver.IntVar(0, 1, team9_driver1.name)
    team9_driver2_var = solver.IntVar(0, 1, team9_driver2.name)
    team9_points = team9.get_expected_points(GP_number) if expectation else team9.get_points(GP_number)
    team9_driver1_points = team9_driver1.get_expected_points(GP_number) if expectation else team9_driver1.get_points(GP_number)
    team9_driver2_points = team9_driver2.get_expected_points(GP_number) if expectation else team9_driver2.get_points(GP_number)
    team_vars.append(team9_var)
    driver_vars.append(team9_driver1_var)
    driver_vars.append(team9_driver2_var)

    team10_var = solver.IntVar(0, 1, team10.name)
    team10_driver1_var = solver.IntVar(0, 1, team10_driver1.name)
    team10_driver2_var = solver.IntVar(0, 1, team10_driver2.name)
    team10_points = team10.get_expected_points(GP_number) if expectation else team10.get_points(GP_number)
    team10_driver1_points = team10_driver1.get_expected_points(GP_number) if expectation else team10_driver1.get_points(GP_number)
    team10_driver2_points = team10_driver2.get_expected_points(GP_number) if expectation else team10_driver2.get_points(GP_number)
    team_vars.append(team10_var)
    driver_vars.append(team10_driver1_var)
    driver_vars.append(team10_driver2_var)

    # Limit the number of drivers that can be picked to five
    solver.Add(team1_driver1_var + team1_driver2_var + team2_driver1_var + team2_driver2_var + team3_driver1_var + team3_driver2_var + team4_driver1_var + team4_driver2_var + team5_driver1_var + team5_driver2_var + team6_driver1_var + team6_driver2_var + team7_driver1_var + team7_driver2_var + team8_driver1_var + team8_driver2_var + team9_driver1_var + team9_driver2_var + team10_driver1_var + team10_driver2_var == 5)

    # Limit the number of teams that can be picked to one
    solver.Add(team1_var + team2_var + team3_var + team4_var + team5_var + team6_var + team7_var + team8_var + team9_var + team10_var == 1)

    # Limit the budget
    solver.Add(team1_driver1_var * team1_driver1.get_price(GP_number) + team1_driver2_var * team1_driver2.get_price(GP_number) + team2_driver1_var * team2_driver1.get_price(GP_number) + team2_driver2_var * team2_driver2.get_price(GP_number) + team3_driver1_var * team3_driver1.get_price(GP_number) + team3_driver2_var * team3_driver2.get_price(GP_number) + team4_driver1_var * team4_driver1.get_price(GP_number) + team4_driver2_var * team4_driver2.get_price(GP_number) + team5_driver1_var * team5_driver1.get_price(GP_number) + team5_driver2_var * team5_driver2.get_price(GP_number) + team6_driver1_var * team6_driver1.get_price(GP_number) + team6_driver2_var * team6_driver2.get_price(GP_number) + team7_driver1_var * team7_driver1.get_price(GP_number) + team7_driver2_var * team7_driver2.get_price(GP_number) + team8_driver1_var * team8_driver1.get_price(GP_number) + team8_driver2_var * team8_driver2.get_price(GP_number) + team9_driver1_var * team9_driver1.get_price(GP_number) + team9_driver2_var * team9_driver2.get_price(GP_number) + team10_driver1_var * team10_driver1.get_price(GP_number) + team10_driver2_var * team10_driver2.get_price(GP_number) + team1_var * team1.get_price(GP_number) + team2_var * team2.get_price(GP_number) + team3_var * team3.get_price(GP_number) + team4_var * team4.get_price(GP_number) + team5_var * team5.get_price(GP_number) + team6_var * team6.get_price(GP_number) + team7_var * team7.get_price(GP_number) + team8_var * team8.get_price(GP_number) + team9_var * team9.get_price(GP_number) + team10_var * team10.get_price(GP_number) <= budget)

    # If there is a required number of subs, add the restriction
    if subs != -1:
        team1_sub = 1 if team1.name in not_in_team else 0
        team2_sub = 1 if team2.name in not_in_team else 0
        team3_sub = 1 if team3.name in not_in_team else 0
        team4_sub = 1 if team4.name in not_in_team else 0
        team5_sub = 1 if team5.name in not_in_team else 0
        team6_sub = 1 if team6.name in not_in_team else 0
        team7_sub = 1 if team7.name in not_in_team else 0
        team8_sub = 1 if team8.name in not_in_team else 0
        team9_sub = 1 if team9.name in not_in_team else 0
        team10_sub = 1 if team10.name in not_in_team else 0
        team1_driver1_sub = 1 if team1_driver1.name in not_in_team else 0
        team2_driver1_sub = 1 if team2_driver1.name in not_in_team else 0
        team3_driver1_sub = 1 if team3_driver1.name in not_in_team else 0
        team4_driver1_sub = 1 if team4_driver1.name in not_in_team else 0
        team5_driver1_sub = 1 if team5_driver1.name in not_in_team else 0
        team6_driver1_sub = 1 if team6_driver1.name in not_in_team else 0
        team7_driver1_sub = 1 if team7_driver1.name in not_in_team else 0
        team8_driver1_sub = 1 if team8_driver1.name in not_in_team else 0
        team9_driver1_sub = 1 if team9_driver1.name in not_in_team else 0
        team10_driver1_sub = 1 if team10_driver1.name in not_in_team else 0
        team1_driver2_sub = 1 if team1_driver2.name in not_in_team else 0
        team2_driver2_sub = 1 if team2_driver2.name in not_in_team else 0
        team3_driver2_sub = 1 if team3_driver2.name in not_in_team else 0
        team4_driver2_sub = 1 if team4_driver2.name in not_in_team else 0
        team5_driver2_sub = 1 if team5_driver2.name in not_in_team else 0
        team6_driver2_sub = 1 if team6_driver2.name in not_in_team else 0
        team7_driver2_sub = 1 if team7_driver2.name in not_in_team else 0
        team8_driver2_sub = 1 if team8_driver2.name in not_in_team else 0
        team9_driver2_sub = 1 if team9_driver2.name in not_in_team else 0
        team10_driver2_sub = 1 if team10_driver2.name in not_in_team else 0
        solver.Add(team1_sub * team1_var + team2_sub * team2_var + team3_sub * team3_var + team4_sub * team4_var + team5_sub * team5_var + team6_sub * team6_var + team7_sub * team7_var + team8_sub * team8_var + team9_sub * team9_var + team10_sub * team10_var + team1_driver1_sub * team1_driver1_var + team1_driver2_sub * team1_driver2_var + team2_driver1_sub * team2_driver1_var + team2_driver2_sub * team2_driver2_var + team3_driver1_sub * team3_driver1_var + team3_driver2_sub * team3_driver2_var + team4_driver1_sub * team4_driver1_var + team4_driver2_sub * team4_driver2_var + team5_driver1_sub * team5_driver1_var + team5_driver2_sub * team5_driver2_var + team6_driver1_sub * team6_driver1_var + team6_driver2_sub * team6_driver2_var + team7_driver1_sub * team7_driver1_var + team7_driver2_sub * team7_driver2_var + team8_driver1_sub * team8_driver1_var + team8_driver2_sub * team8_driver2_var + team9_driver1_sub * team9_driver1_var + team9_driver2_sub * team9_driver2_var + team10_driver1_sub * team10_driver1_var + team10_driver2_sub * team10_driver2_var == subs)

    # Define the max function
    solver.Maximize(team1_driver1_var * team1_driver1_points + team1_driver2_var * team1_driver2_points + team2_driver1_var * team2_driver1_points + team2_driver2_var * team2_driver2_points + team3_driver1_var * team3_driver1_points + team3_driver2_var * team3_driver2_points + team4_driver1_var * team4_driver1_points + team4_driver2_var * team4_driver2_points + team5_driver1_var * team5_driver1_points + team5_driver2_var * team5_driver2_points + team6_driver1_var * team6_driver1_points + team6_driver2_var * team6_driver2_points + team7_driver1_var * team7_driver1_points + team7_driver2_var * team7_driver2_points + team8_driver1_var * team8_driver1_points + team8_driver2_var * team8_driver2_points + team9_driver1_var * team9_driver1_points + team9_driver2_var * team9_driver2_points + team10_driver1_var * team10_driver1_points + team10_driver2_var * team10_driver2_points + team1_var * team1_points + team2_var * team2_points + team3_var * team3_points + team4_var * team4_points + team5_var * team5_points + team6_var * team6_points + team7_var * team7_points + team8_var * team8_points + team9_var * team9_points + team10_var * team10_points)

    # Solve the system
    status = solver.Solve()

    optimal_team = None
    optimal_drivers = []
    if status == pywraplp.Solver.OPTIMAL:
        for i in range(len(team_vars)):
            if team_vars[i].solution_value() == 1:
                optimal_team = all_teams[i]
        for i in range(len(driver_vars)):
            if driver_vars[i].solution_value() == 1:
                optimal_drivers.append(all_drivers[i])
    else:
        raise Exception("Cannot solve system")

    return FantasyTeam(optimal_team, optimal_drivers, budget, GP_number)

