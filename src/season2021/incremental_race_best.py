from src.season2021.optimizer import get_potential_best_teams_next_GP, get_best_teams_next_GP, FantasyTeam
from src.season2021.config import GPs, driver_map, team_map

if __name__ == '__main__':
    # Budget at the end of the last GP
    budget = 104.2
    # The next GP
    next_GP = "Monaco"
    # Expectation or actual results
    expectation = True
    # Your team
    team = "Red Bull"
    driver1 = "Verstappen"
    driver2 = "Leclerc"
    driver3 = "Norris"
    driver4 = "Schumacher"
    driver5 = "Ocon"
    # Names of drivers and constructors to absolutely include/exclude
    include = []
    exclude = []

    subs = 1

    current_team = FantasyTeam(team=team_map[team], drivers=[driver_map[driver1], driver_map[driver2], driver_map[driver3], driver_map[driver4], driver_map[driver5]], GP_number=GPs.index(next_GP) - 1, budget=budget, subs=subs)
    next_best_teams = sorted(get_potential_best_teams_next_GP(current_team=current_team, include=include, exclude=exclude), key=lambda f_team: -f_team.get_expected_points()) if expectation else get_best_teams_next_GP(current_team=current_team, include=include, exclude=exclude)
    for next_best_team in next_best_teams:
        print(next_best_team.to_string())
