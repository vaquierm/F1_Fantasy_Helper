from src.season2021.optimizer import get_historical_best_team_sequence

if __name__ == '__main__':
    best_team_sequence = get_historical_best_team_sequence()
    print(best_team_sequence.to_string())
