from src.season2021.config import *
from src.season2021.variable import Team
from ortools.linear_solver import pywraplp
import numpy as np

all_teams = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team10]
all_drivers = [team1_driver1, team1_driver2, team2_driver1, team2_driver2, team3_driver1, team3_driver2, team4_driver1, team4_driver2, team5_driver1, team5_driver2, team6_driver1, team6_driver2, team7_driver1, team7_driver2, team8_driver1, team8_driver2, team9_driver1, team9_driver2, team10_driver1, team10_driver2]


class FantasyTeam:
    def __init__(self, team: Team, drivers: list, budget, GP_number, subs: int = 0):
        self.team = team
        self.drivers = drivers
        self.GP_number = GP_number
        self.subs = subs

        if round(self.get_price_pre_GP(), 1) > round(budget, 1):
            raise Exception("You cannot afford this team")

        cash = budget - self.get_price_pre_GP()
        self.budget_at_GP = self.get_price_at_GP() + cash
        self.budget_pre_GP = budget

        if len(drivers) != 5:
            raise Exception("Fantasy team must be at 5 drivers")

    def to_string(self, indents: int = 0):
        indent_str = "".join(["\t" for i in range(indents)]) if indents > 0 else ""
        team_str = ""
        team_str += "\n" + indent_str + "GP: " + GPs[self.GP_number]
        team_str += "\n" + indent_str + "Team: " + self.team.name
        team_str += "\n" + indent_str + "\tPrice: " + str(self.team.get_price(self.GP_number))
        team_str += "\n" + indent_str + "\tExpected Points: " + str(round(self.team.get_expected_points(self.GP_number), 2))
        if self.GP_number < self.team.N_GP:
            team_str += "\n" + indent_str + "\tActual Points: " + str(round(self.team.get_points(self.GP_number), 2))
        for i in range(len(self.drivers)):
            team_str += "\n" + indent_str + "Driver " + str(i + 1) + ": " + self.drivers[i].name
            team_str += "\n" + indent_str + "\tPrice: " + str(self.drivers[i].get_price(self.GP_number))
            team_str += "\n" + indent_str + "\tExpected Points: " + str(round(self.drivers[i].get_expected_points(self.GP_number), 2))
            if self.GP_number < self.team.N_GP:
                team_str += "\n" + indent_str + "\tActual Points: " + str(round(self.drivers[i].get_points(self.GP_number), 2))
        if self.subs > 3:
            team_str += "\n" + indent_str + str(self.subs - 3) + "0 points penalty for " + str(self.subs) + " substitutions"
        team_str += "\n" + indent_str + "Total Team Price: " + str(round(self.get_price_at_GP(), 1))
        team_str += "\n" + indent_str + "Total Budget Pre GP: " + str(round(self.budget_pre_GP, 1))
        team_str += "\n" + indent_str + "Total Budget At GP: " + str(round(self.budget_at_GP, 1))
        team_str += "\n" + indent_str + "Total Expected Points: " + str(round(self.get_expected_points(), 2)) + " with turbo-driver " + self.best_expected_turbo_driver().name
        if self.GP_number < self.team.N_GP:
            team_str += "\n" + indent_str + "Total Actual Points: " + str(round(self.get_points(use_best_expected_turbo_driver=False), 2)) + " with best turbo-driver " + self.best_turbo_driver().name
            team_str += "\n" + indent_str + "Total Actual Points: " + str(round(self.get_points(use_best_expected_turbo_driver=True), 2)) + " with best expected turbo-driver " + self.best_expected_turbo_driver().name

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

    def get_points(self, use_best_expected_turbo_driver: bool = False):
        points = self.team.get_points(self.GP_number)
        turbo_driver = self.best_expected_turbo_driver() if use_best_expected_turbo_driver else self.best_turbo_driver()
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
        return str(str(self.GP_number) + "_" + self.team.name + '_' + '_'.join(driver_names))

    def get_price_at_GP(self):
        total_price = self.team.get_price(self.GP_number)
        for driver in self.drivers:
            total_price += driver.get_price(self.GP_number)

        return total_price

    def get_price_pre_GP(self):
        total_price = self.team.get_price(self.GP_number - 1)
        for driver in self.drivers:
            total_price += driver.get_price(self.GP_number - 1)

        return total_price

    def get_budget_at_GP(self):
        return self.budget_at_GP

    def get_budget_pre_GP(self):
        return self.budget_pre_GP


class FantasyTeamSequence:
    def __init__(self, start_team: FantasyTeam):
        self.team_sequence = [start_team]

    def add_team(self, next_team: FantasyTeam):
        self.team_sequence.append(next_team)

    def get_total_points(self, use_best_expected_turbo_driver: bool = False):
        total = 0
        for team in self.team_sequence:
            total += team.get_points(use_best_expected_turbo_driver=use_best_expected_turbo_driver)
        return total

    def get_total_expected_points(self):
        total = 0
        for team in self.team_sequence:
            total += team.get_expected_points()
        return total

    def to_string(self):
        team_str = ""
        for team in self.team_sequence:
            team_str += team.to_string() + "\n"
        team_str += "\nTotal Expected Cumulative Points: " + str(round(self.get_total_expected_points(), 2))
        team_str += "\nTotal Actual Cumulative Points: " + str(round(self.get_total_points(use_best_expected_turbo_driver=False), 2)) + " with best turbo-driver"
        team_str += "\nTotal Actual Cumulative Points: " + str(round(self.get_total_points(use_best_expected_turbo_driver=True), 2)) + " with best expected turbo-driver"
        return team_str


def get_potential_best_teams_next_GP(current_team: FantasyTeam, include: list = [], exclude: list = []):
    if len(include) == 0 and len(exclude) == 0:
        potential_teams = [FantasyTeam(current_team.team, current_team.drivers, current_team.get_budget_at_GP(), current_team.GP_number + 1, 0)]
    else:
        potential_teams = []
    for i in range(1 if len(include) == 0 and len(exclude) == 0 else 0, 7):
        try:
            potential_teams.append(__get_best_team_next_GP(current_team, True, i, include, exclude))
        except:
            pass

    if (len(potential_teams)) == 0:
        raise Exception("No teams can satisfy the conditions")

    team_points = np.array(list(map(lambda team: team.get_expected_points(), potential_teams)))
    std = np.std(team_points)
    max = np.max(team_points)

    potential_teams_keep = []

    for i in range(len(potential_teams)):
        if team_points[i] >= max - std:
            potential_teams_keep.append(potential_teams[i])

    return potential_teams_keep


def get_historical_best_team_sequence():
    starting_teams = get_best_starter_teams(expectation=False)
    potential_sequences = []
    cache = {}
    for starting_team in starting_teams:
        potential_sequences.append(get_historical_best_team_sequence_after(starting_team, cache))
    potential_sequences = sorted(potential_sequences, key=lambda seq: seq.get_total_points())
    return potential_sequences[0]


def get_historical_best_team_sequence_after(team: FantasyTeam, cache):
    best_teams = get_best_teams_next_GP(current_team=team)
    best_sequence = FantasyTeamSequence(team)

    if team.GP_number == info["N_GP"] - 2:
        # Final race next. Just maximize points.
        best_teams = sorted(best_teams, key=lambda t: t.get_points())
        best_sequence.add_team(best_teams[0])
        return best_sequence

    potential_sequences = []
    for t in best_teams:
        potential_sequences.append(get_historical_best_team_sequence_after(t, cache))
    potential_sequences = sorted(potential_sequences, key=lambda seq: seq.get_total_points())
    for t in potential_sequences[0].team_sequence:
        best_sequence.add_team(t)
    return best_sequence


def get_best_starter_teams(expectation: bool):
    best_starter_teams = []
    best_team = get_best_team_for_GP(budget=100, GP_number=0, expectation=expectation)
    best_starter_teams.append(best_team)
    team = get_best_team_for_GP(budget=100, GP_number=0, expectation=expectation, exclude=[best_team.team.name])
    if team.get_team_hash() != best_team.get_team_hash():
        best_starter_teams.append(team)
    for driver in best_team.drivers:
        team = get_best_team_for_GP(budget=100, GP_number=0, expectation=expectation, exclude=[driver.name])
        team_hashes = list(map(lambda t: t.get_team_hash(), best_starter_teams))
        if team.get_team_hash() not in team_hashes:
            best_starter_teams.append(team)
    return sorted(best_starter_teams, key=lambda t: -(t.get_expected_points() if expectation else t.get_points()))


def follow_the_AI(starting_team: FantasyTeam):
    team_sequence = FantasyTeamSequence(starting_team)
    last_team = starting_team
    for i in range(info["N_GP"] - 1):
        last_team = __get_best_team_next_GP(current_team=last_team, expectation=True)
        team_sequence.add_team(last_team)
    return team_sequence


def get_best_teams_next_GP(current_team: FantasyTeam, include: list = [], exclude: list = []):
    if len(include) == 0 and len(exclude) == 0:
        potential_teams = [FantasyTeam(current_team.team, current_team.drivers, current_team.get_budget_at_GP(), current_team.GP_number + 1, 0)]
        potential_teams_hashes = potential_teams[0].get_team_hash()
    else:
        potential_teams = []
        potential_teams_hashes = []
    for i in range(1 if len(include) == 0 and len(exclude) == 0 else 0, 7):
        try:
            potential_team = __get_best_team_next_GP(current_team, False, i, include, exclude)
            potential_team_hash = potential_team.get_team_hash()
            if potential_team_hash not in potential_teams_hashes:
                potential_teams.append(potential_team)
                potential_teams_hashes.append(potential_team_hash)
        except:
            pass

    if (len(potential_teams)) == 0:
        raise Exception("No teams can satisfy the conditions")

    team_points = np.array(list(map(lambda team: team.get_points(), potential_teams)))
    max = np.max(team_points)
    max_indexes = np.where(team_points == max)

    max_teams = []
    for max_index in max_indexes:
        max_teams.append(potential_teams[max_index[0]])

    return max_teams


def __get_best_team_next_GP(current_team: FantasyTeam, expectation: bool = False, subs: int = -1, include: list = [], exclude: list = []):
    solver = pywraplp.Solver.CreateSolver("F1 Fantasy solver", "CBC")

    team_hash = current_team.get_team_hash()

    GP_number = current_team.GP_number + 1

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
    GP_number -= 1
    solver.Add(team1_driver1_var * team1_driver1.get_price(GP_number) + team1_driver2_var * team1_driver2.get_price(GP_number) + team2_driver1_var * team2_driver1.get_price(GP_number) + team2_driver2_var * team2_driver2.get_price(GP_number) + team3_driver1_var * team3_driver1.get_price(GP_number) + team3_driver2_var * team3_driver2.get_price(GP_number) + team4_driver1_var * team4_driver1.get_price(GP_number) + team4_driver2_var * team4_driver2.get_price(GP_number) + team5_driver1_var * team5_driver1.get_price(GP_number) + team5_driver2_var * team5_driver2.get_price(GP_number) + team6_driver1_var * team6_driver1.get_price(GP_number) + team6_driver2_var * team6_driver2.get_price(GP_number) + team7_driver1_var * team7_driver1.get_price(GP_number) + team7_driver2_var * team7_driver2.get_price(GP_number) + team8_driver1_var * team8_driver1.get_price(GP_number) + team8_driver2_var * team8_driver2.get_price(GP_number) + team9_driver1_var * team9_driver1.get_price(GP_number) + team9_driver2_var * team9_driver2.get_price(GP_number) + team10_driver1_var * team10_driver1.get_price(GP_number) + team10_driver2_var * team10_driver2.get_price(GP_number) + team1_var * team1.get_price(GP_number) + team2_var * team2.get_price(GP_number) + team3_var * team3.get_price(GP_number) + team4_var * team4.get_price(GP_number) + team5_var * team5.get_price(GP_number) + team6_var * team6.get_price(GP_number) + team7_var * team7.get_price(GP_number) + team8_var * team8.get_price(GP_number) + team9_var * team9.get_price(GP_number) + team10_var * team10.get_price(GP_number) <= current_team.get_budget_at_GP())
    GP_number += 1

    # If there is a required number of subs, add the restriction
    if subs != -1:
        team1_sub = 0 if team1.name in team_hash else 1
        team2_sub = 0 if team2.name in team_hash else 1
        team3_sub = 0 if team3.name in team_hash else 1
        team4_sub = 0 if team4.name in team_hash else 1
        team5_sub = 0 if team5.name in team_hash else 1
        team6_sub = 0 if team6.name in team_hash else 1
        team7_sub = 0 if team7.name in team_hash else 1
        team8_sub = 0 if team8.name in team_hash else 1
        team9_sub = 0 if team9.name in team_hash else 1
        team10_sub = 0 if team10.name in team_hash else 1
        team1_driver1_sub = 0 if team1_driver1.name in team_hash else 1
        team2_driver1_sub = 0 if team2_driver1.name in team_hash else 1
        team3_driver1_sub = 0 if team3_driver1.name in team_hash else 1
        team4_driver1_sub = 0 if team4_driver1.name in team_hash else 1
        team5_driver1_sub = 0 if team5_driver1.name in team_hash else 1
        team6_driver1_sub = 0 if team6_driver1.name in team_hash else 1
        team7_driver1_sub = 0 if team7_driver1.name in team_hash else 1
        team8_driver1_sub = 0 if team8_driver1.name in team_hash else 1
        team9_driver1_sub = 0 if team9_driver1.name in team_hash else 1
        team10_driver1_sub = 0 if team10_driver1.name in team_hash else 1
        team1_driver2_sub = 0 if team1_driver2.name in team_hash else 1
        team2_driver2_sub = 0 if team2_driver2.name in team_hash else 1
        team3_driver2_sub = 0 if team3_driver2.name in team_hash else 1
        team4_driver2_sub = 0 if team4_driver2.name in team_hash else 1
        team5_driver2_sub = 0 if team5_driver2.name in team_hash else 1
        team6_driver2_sub = 0 if team6_driver2.name in team_hash else 1
        team7_driver2_sub = 0 if team7_driver2.name in team_hash else 1
        team8_driver2_sub = 0 if team8_driver2.name in team_hash else 1
        team9_driver2_sub = 0 if team9_driver2.name in team_hash else 1
        team10_driver2_sub = 0 if team10_driver2.name in team_hash else 1
        solver.Add(team1_sub * team1_var + team2_sub * team2_var + team3_sub * team3_var + team4_sub * team4_var + team5_sub * team5_var + team6_sub * team6_var + team7_sub * team7_var + team8_sub * team8_var + team9_sub * team9_var + team10_sub * team10_var + team1_driver1_sub * team1_driver1_var + team1_driver2_sub * team1_driver2_var + team2_driver1_sub * team2_driver1_var + team2_driver2_sub * team2_driver2_var + team3_driver1_sub * team3_driver1_var + team3_driver2_sub * team3_driver2_var + team4_driver1_sub * team4_driver1_var + team4_driver2_sub * team4_driver2_var + team5_driver1_sub * team5_driver1_var + team5_driver2_sub * team5_driver2_var + team6_driver1_sub * team6_driver1_var + team6_driver2_sub * team6_driver2_var + team7_driver1_sub * team7_driver1_var + team7_driver2_sub * team7_driver2_var + team8_driver1_sub * team8_driver1_var + team8_driver2_sub * team8_driver2_var + team9_driver1_sub * team9_driver1_var + team9_driver2_sub * team9_driver2_var + team10_driver1_sub * team10_driver1_var + team10_driver2_sub * team10_driver2_var == subs)

    # Include the specific requirements
    if team1.name in include:
        solver.Add(team1_var == 1)
    if team1.name in exclude:
        solver.Add(team1_var == 0)
    if team2.name in include:
        solver.Add(team2_var == 1)
    if team2.name in exclude:
        solver.Add(team2_var == 0)
    if team3.name in include:
        solver.Add(team3_var == 1)
    if team3.name in exclude:
        solver.Add(team3_var == 0)
    if team4.name in include:
        solver.Add(team4_var == 1)
    if team4.name in exclude:
        solver.Add(team4_var == 0)
    if team5.name in include:
        solver.Add(team5_var == 1)
    if team5.name in exclude:
        solver.Add(team5_var == 0)
    if team6.name in include:
        solver.Add(team6_var == 1)
    if team6.name in exclude:
        solver.Add(team6_var == 0)
    if team7.name in include:
        solver.Add(team7_var == 1)
    if team7.name in exclude:
        solver.Add(team7_var == 0)
    if team8.name in include:
        solver.Add(team8_var == 1)
    if team8.name in exclude:
        solver.Add(team8_var == 0)
    if team9.name in include:
        solver.Add(team9_var == 1)
    if team9.name in exclude:
        solver.Add(team9_var == 0)
    if team10.name in include:
        solver.Add(team10_var == 1)
    if team10.name in exclude:
        solver.Add(team10_var == 0)
    if team1_driver1.name in include:
        solver.Add(team1_driver1_var == 1)
    if team1_driver1.name in exclude:
        solver.Add(team1_driver1_var == 0)
    if team2_driver1.name in include:
        solver.Add(team2_driver1_var == 1)
    if team2_driver1.name in exclude:
        solver.Add(team2_driver1_var == 0)
    if team3_driver1.name in include:
        solver.Add(team3_driver1_var == 1)
    if team3_driver1.name in exclude:
        solver.Add(team3_driver1_var == 0)
    if team4_driver1.name in include:
        solver.Add(team4_driver1_var == 1)
    if team4_driver1.name in exclude:
        solver.Add(team4_driver1_var == 0)
    if team5_driver1.name in include:
        solver.Add(team5_driver1_var == 1)
    if team5_driver1.name in exclude:
        solver.Add(team5_driver1_var == 0)
    if team6_driver1.name in include:
        solver.Add(team6_driver1_var == 1)
    if team6_driver1.name in exclude:
        solver.Add(team6_driver1_var == 0)
    if team7_driver1.name in include:
        solver.Add(team7_driver1_var == 1)
    if team7_driver1.name in exclude:
        solver.Add(team7_driver1_var == 0)
    if team8_driver1.name in include:
        solver.Add(team8_driver1_var == 1)
    if team8_driver1.name in exclude:
        solver.Add(team8_driver1_var == 0)
    if team9_driver1.name in include:
        solver.Add(team9_driver1_var == 1)
    if team9_driver1.name in exclude:
        solver.Add(team9_driver1_var == 0)
    if team10_driver1.name in include:
        solver.Add(team10_driver1_var == 1)
    if team10_driver1.name in exclude:
        solver.Add(team10_driver1_var == 0)
    if team1_driver2.name in include:
        solver.Add(team1_driver2_var == 1)
    if team1_driver2.name in exclude:
        solver.Add(team1_driver2_var == 0)
    if team2_driver2.name in include:
        solver.Add(team2_driver2_var == 1)
    if team2_driver2.name in exclude:
        solver.Add(team2_driver2_var == 0)
    if team3_driver2.name in include:
        solver.Add(team3_driver2_var == 1)
    if team3_driver2.name in exclude:
        solver.Add(team3_driver2_var == 0)
    if team4_driver2.name in include:
        solver.Add(team4_driver2_var == 1)
    if team4_driver2.name in exclude:
        solver.Add(team4_driver2_var == 0)
    if team5_driver2.name in include:
        solver.Add(team5_driver2_var == 1)
    if team5_driver2.name in exclude:
        solver.Add(team5_driver2_var == 0)
    if team6_driver2.name in include:
        solver.Add(team6_driver2_var == 1)
    if team6_driver2.name in exclude:
        solver.Add(team6_driver2_var == 0)
    if team7_driver2.name in include:
        solver.Add(team7_driver2_var == 1)
    if team7_driver2.name in exclude:
        solver.Add(team7_driver2_var == 0)
    if team8_driver2.name in include:
        solver.Add(team8_driver2_var == 1)
    if team8_driver2.name in exclude:
        solver.Add(team8_driver2_var == 0)
    if team9_driver2.name in include:
        solver.Add(team9_driver2_var == 1)
    if team9_driver2.name in exclude:
        solver.Add(team9_driver2_var == 0)
    if team10_driver2.name in include:
        solver.Add(team10_driver2_var == 1)
    if team10_driver2.name in exclude:
        solver.Add(team10_driver2_var == 0)

    # Define the max function
    solver.Maximize(team1_driver1_var * team1_driver1_points + team1_driver2_var * team1_driver2_points + team2_driver1_var * team2_driver1_points + team2_driver2_var * team2_driver2_points + team3_driver1_var * team3_driver1_points + team3_driver2_var * team3_driver2_points + team4_driver1_var * team4_driver1_points + team4_driver2_var * team4_driver2_points + team5_driver1_var * team5_driver1_points + team5_driver2_var * team5_driver2_points + team6_driver1_var * team6_driver1_points + team6_driver2_var * team6_driver2_points + team7_driver1_var * team7_driver1_points + team7_driver2_var * team7_driver2_points + team8_driver1_var * team8_driver1_points + team8_driver2_var * team8_driver2_points + team9_driver1_var * team9_driver1_points + team9_driver2_var * team9_driver2_points + team10_driver1_var * team10_driver1_points + team10_driver2_var * team10_driver2_points + team1_var * team1_points + team2_var * team2_points + team3_var * team3_points + team4_var * team4_points + team5_var * team5_points + team6_var * team6_points + team7_var * team7_points + team8_var * team8_points + team9_var * team9_points + team10_var * team10_points)

    # Solve the system
    status = solver.Solve()

    optimal_team = None
    optimal_drivers = []
    sub_count = 0
    if status == pywraplp.Solver.OPTIMAL:
        for i in range(len(team_vars)):
            if team_vars[i].solution_value() == 1:
                optimal_team = all_teams[i]
                if all_teams[i].name not in team_hash:
                    sub_count += 1
        for i in range(len(driver_vars)):
            if driver_vars[i].solution_value() == 1:
                optimal_drivers.append(all_drivers[i])
                if all_drivers[i].name not in team_hash:
                    sub_count += 1
    else:
        raise Exception("No teams can satisfy the conditions")

    return FantasyTeam(optimal_team, optimal_drivers, current_team.get_budget_at_GP(), GP_number, sub_count if GP_number != 0 else 0)


def get_best_team_for_GP(budget, GP_number: int, expectation: bool = False, include: list = [], exclude: list = []):
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

    # Include the specific requirements
    if team1.name in include:
        solver.Add(team1_var == 1)
    if team1.name in exclude:
        solver.Add(team1_var == 0)
    if team2.name in include:
        solver.Add(team2_var == 1)
    if team2.name in exclude:
        solver.Add(team2_var == 0)
    if team3.name in include:
        solver.Add(team3_var == 1)
    if team3.name in exclude:
        solver.Add(team3_var == 0)
    if team4.name in include:
        solver.Add(team4_var == 1)
    if team4.name in exclude:
        solver.Add(team4_var == 0)
    if team5.name in include:
        solver.Add(team5_var == 1)
    if team5.name in exclude:
        solver.Add(team5_var == 0)
    if team6.name in include:
        solver.Add(team6_var == 1)
    if team6.name in exclude:
        solver.Add(team6_var == 0)
    if team7.name in include:
        solver.Add(team7_var == 1)
    if team7.name in exclude:
        solver.Add(team7_var == 0)
    if team8.name in include:
        solver.Add(team8_var == 1)
    if team8.name in exclude:
        solver.Add(team8_var == 0)
    if team9.name in include:
        solver.Add(team9_var == 1)
    if team9.name in exclude:
        solver.Add(team9_var == 0)
    if team10.name in include:
        solver.Add(team10_var == 1)
    if team10.name in exclude:
        solver.Add(team10_var == 0)
    if team1_driver1.name in include:
        solver.Add(team1_driver1_var == 1)
    if team1_driver1.name in exclude:
        solver.Add(team1_driver1_var == 0)
    if team2_driver1.name in include:
        solver.Add(team2_driver1_var == 1)
    if team2_driver1.name in exclude:
        solver.Add(team2_driver1_var == 0)
    if team3_driver1.name in include:
        solver.Add(team3_driver1_var == 1)
    if team3_driver1.name in exclude:
        solver.Add(team3_driver1_var == 0)
    if team4_driver1.name in include:
        solver.Add(team4_driver1_var == 1)
    if team4_driver1.name in exclude:
        solver.Add(team4_driver1_var == 0)
    if team5_driver1.name in include:
        solver.Add(team5_driver1_var == 1)
    if team5_driver1.name in exclude:
        solver.Add(team5_driver1_var == 0)
    if team6_driver1.name in include:
        solver.Add(team6_driver1_var == 1)
    if team6_driver1.name in exclude:
        solver.Add(team6_driver1_var == 0)
    if team7_driver1.name in include:
        solver.Add(team7_driver1_var == 1)
    if team7_driver1.name in exclude:
        solver.Add(team7_driver1_var == 0)
    if team8_driver1.name in include:
        solver.Add(team8_driver1_var == 1)
    if team8_driver1.name in exclude:
        solver.Add(team8_driver1_var == 0)
    if team9_driver1.name in include:
        solver.Add(team9_driver1_var == 1)
    if team9_driver1.name in exclude:
        solver.Add(team9_driver1_var == 0)
    if team10_driver1.name in include:
        solver.Add(team10_driver1_var == 1)
    if team10_driver1.name in exclude:
        solver.Add(team10_driver1_var == 0)
    if team1_driver2.name in include:
        solver.Add(team1_driver2_var == 1)
    if team1_driver2.name in exclude:
        solver.Add(team1_driver2_var == 0)
    if team2_driver2.name in include:
        solver.Add(team2_driver2_var == 1)
    if team2_driver2.name in exclude:
        solver.Add(team2_driver2_var == 0)
    if team3_driver2.name in include:
        solver.Add(team3_driver2_var == 1)
    if team3_driver2.name in exclude:
        solver.Add(team3_driver2_var == 0)
    if team4_driver2.name in include:
        solver.Add(team4_driver2_var == 1)
    if team4_driver2.name in exclude:
        solver.Add(team4_driver2_var == 0)
    if team5_driver2.name in include:
        solver.Add(team5_driver2_var == 1)
    if team5_driver2.name in exclude:
        solver.Add(team5_driver2_var == 0)
    if team6_driver2.name in include:
        solver.Add(team6_driver2_var == 1)
    if team6_driver2.name in exclude:
        solver.Add(team6_driver2_var == 0)
    if team7_driver2.name in include:
        solver.Add(team7_driver2_var == 1)
    if team7_driver2.name in exclude:
        solver.Add(team7_driver2_var == 0)
    if team8_driver2.name in include:
        solver.Add(team8_driver2_var == 1)
    if team8_driver2.name in exclude:
        solver.Add(team8_driver2_var == 0)
    if team9_driver2.name in include:
        solver.Add(team9_driver2_var == 1)
    if team9_driver2.name in exclude:
        solver.Add(team9_driver2_var == 0)
    if team10_driver2.name in include:
        solver.Add(team10_driver2_var == 1)
    if team10_driver2.name in exclude:
        solver.Add(team10_driver2_var == 0)

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

