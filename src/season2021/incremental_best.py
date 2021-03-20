from src.season2021.optimizer import get_potential_best_teams_next_GP, FantasyTeam
from src.season2021.config import GPs, driver_map, team_map

if __name__ == '__main__':
    budget = 100
    team = "Red Bull"
    driver1 = "Hamilton"
    driver2 = "Norris"
    driver3 = "Gasly"
    driver4 = "Raikkonen"
    driver5 = "Russel"
    next_GP = "Italy"
    expectation = True
    current_team = FantasyTeam(team=team_map[team], drivers=[driver_map[driver1], driver_map[driver2], driver_map[driver3], driver_map[driver4], driver_map[driver5]], GP_number=GPs.index(next_GP) - 1, budget=budget)
    next_best_teams = get_potential_best_teams_next_GP(current_team=current_team, expectation=expectation)

    for next_best_team in next_best_teams:
        print(next_best_team.to_string())
