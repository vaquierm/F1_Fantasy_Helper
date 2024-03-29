from src.season2021.optimizer import get_best_team_for_GP
from src.season2021.config import GPs

if __name__ == '__main__':
    # Your budget at the end of last GP
    budget = 109.8
    # The target GP
    GP = "Brazil"
    # Expectation or actual results
    expectation = True
    # Names of drivers and constructors to absolutely include/exclude
    include = []
    exclude = []

    best_team = get_best_team_for_GP(budget=budget, GP_number=GPs.index(GP), expectation=expectation, include=include, exclude=exclude)
    print(best_team.to_string())
