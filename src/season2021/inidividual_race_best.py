from src.season2021.optimizer import get_best_team
from src.season2021.config import GPs

if __name__ == '__main__':
    budget = 100
    GP = "Bahrain"
    best_team = get_best_team(budget=budget, GP_number=GPs.index(GP), expectation=True)

    print(best_team.to_string())
