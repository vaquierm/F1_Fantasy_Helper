from src.season2021.optimizer import get_best_starter_teams

if __name__ == '__main__':
    expectation = True

    best_starter_teams = get_best_starter_teams(expectation=expectation)
    for team in best_starter_teams:
        print(team.to_string())
