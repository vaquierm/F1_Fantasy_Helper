from src.season2021.optimizer import follow_the_AI, FantasyTeam
from src.season2021.config import GPs, driver_map, team_map

if __name__ == '__main__':
    # Starting team
    team = "Red Bull"
    driver1 = "Hamilton"
    driver2 = "Norris"
    driver3 = "Gasly"
    driver4 = "Raikkonen"
    driver5 = "Russel"

    starting_team = FantasyTeam(team=team_map[team], drivers=[driver_map[driver1], driver_map[driver2], driver_map[driver3], driver_map[driver4], driver_map[driver5]], GP_number=0, budget=100)
    team_sequence = follow_the_AI(starting_team)
    print(team_sequence.to_string())
