from src.season2021.optimizer import get_best_team_for_GP
from src.season2021.config import GPs

if __name__ == '__main__':
    budget = 100
    GP = "Bahrain"
    expectation = True
    best_team = get_best_team_for_GP(budget=budget, GP_number=GPs.index(GP), expectation=expectation, include=["Hamilton"], exclude=[])

    print(best_team.to_string())
