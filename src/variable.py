def best_for_turbo_driver(drivers: list):
    """
    :param drivers: list of drivers from which to chose turbo driver
    :return: Best driver to use for turbo driver
    """
    best = None
    for driver in drivers:
        if driver.price < 20:
            if best is None or best.get_expected_points() < driver.get_expected_points():
                best = driver

    return best


class Variable:

    def __init__(self, name, points, price, top10_qualy, top10_finish, streak_length):
        """
        Variable object that keeps track of price and points
        :param name: Name of driver or team
        :param points: Points that the driver or team scored
        :param price: Price of the driver or team
        :param top10_qualy: List of 1s and 0s indicating if the team or driver made it in the top 10 in qualifications
        :param top10_finish: List of 1s and 0s inidicating if the team or driver made it in the top 10 in the race
        :param streak_length: Length of streak needed to score bonus points
        """
        self.name = name
        self.points = points
        self.price = price
        self.top10_qualy = top10_qualy
        self.top10_finish = top10_finish
        self.streak_length = streak_length

        self.turbo_driver = False
        self.substitute = False

        if len(top10_qualy) != len(top10_finish):
            raise Exception("The length of the top 10 finish records and top 10 qualy records are not equal")

        self.n_races = len(top10_qualy)

        self.qualy_top10_ratio = sum(self.top10_qualy) / self.n_races
        self.finish_top10_ratio = sum(self.top10_finish) / self.n_races

        qualy_consecutive = 0
        finish_consecutive = 0
        for i in range(self.n_races):
            if self.top10_qualy[i] == 1:
                qualy_consecutive += 1
                if qualy_consecutive == self.streak_length:
                    qualy_consecutive = 0
            else:
                qualy_consecutive = 0
            if self.top10_finish[i] == 1:
                finish_consecutive += 1
                if finish_consecutive == self.streak_length:
                    finish_consecutive = 0
            else:
                finish_consecutive = 0

        self.qualy_bonus = qualy_consecutive == self.streak_length - 1
        self.finish_bonus = finish_consecutive == self.streak_length - 1

    def get_expected_points(self):
        """
        Calculate the expected points this driver or team could get in they next race
        :return: The expected points the driver or team could get in the next race
        """
        points = self.points

        # Remove points that were obtained in a streak
        qualy_consecutive = 0
        finish_consecutive = 0
        for i in range(self.n_races):
            if self.top10_qualy[i] == 1:
                qualy_consecutive += 1
                if qualy_consecutive == self.streak_length:
                    qualy_consecutive = 0
                    points -= 5
            else:
                qualy_consecutive = 0
            if self.top10_finish[i] == 1:
                finish_consecutive += 1
                if finish_consecutive == self.streak_length:
                    finish_consecutive = 0
                    points -= 10
            else:
                finish_consecutive = 0

        average_points_per_race = points / self.n_races

        if qualy_consecutive == self.streak_length - 1:
            # Add the points for the qualy streak with the probability that they will actually make it this next race
            average_points_per_race += 5 * self.qualy_top10_ratio
        if finish_consecutive == self.streak_length - 1:
            # Same thing for the finish streak
            average_points_per_race += 10 * self.finish_top10_ratio

        if self.turbo_driver:
            # If turbo driver, double the points
            average_points_per_race *= 2

        if self.substitute:
            # If this is a substitute with a penalty, remove points
            average_points_per_race -= 10

        return average_points_per_race
