import numpy as np


class Variable:

    def __init__(self, name, start_point_expectation, prices: list, points: list, race_positions: list, top10_race, qualy_positions: list, top10_qualy, streak_length: int):
        """

        :param name:
        :param start_point_expectation:
        :param prices:
        :param points:
        :param race_positions:
        :param qualy_positions:
        :param streak_length:
        """
        self.name = name
        self.prices = np.array(prices)
        self.points = np.array(points)
        self.race_positions = np.array(race_positions)
        self.qualy_positions = np.array(qualy_positions)
        self.streak_length = streak_length

        if not (len(prices) - 1 == len(points) == len(race_positions) == len(qualy_positions)):
            raise Exception("Missing data for variable " + name)

        self.N_GP = len(points)

        self.expected_points = np.empty(self.N_GP + 1)
        self.expected_points[0] = start_point_expectation

        qualy_consecutive = 0
        finish_consecutive = 0
        for i in range(self.N_GP):
            qualy_steak_prob = ((10 - np.average(self.qualy_positions[:i+1]) + 1) / 5) + (np.average(top10_qualy[:i+1]) / 2)
            race_steak_prob = ((10 - np.average(self.race_positions[:i+1]) + 1) / 5) + (np.average(top10_race[:i+1]) / 2)
            race_i_expected_points = 0
            if top10_qualy[i] == 1:
                qualy_consecutive += 1
                if qualy_consecutive == self.streak_length:
                    race_i_expected_points += 5 * qualy_steak_prob
                    # Remove from the points array to get the raw number of points
                    self.points[i] -= 5
                    qualy_consecutive = 0
            else:
                qualy_consecutive = 0
            if top10_race[i] == 10:
                finish_consecutive += 1
                if finish_consecutive == self.streak_length:
                    race_i_expected_points += 10 * race_steak_prob
                    # Remove from the points array to get the raw number of points
                    self.points -= 10
                    finish_consecutive = 0
            else:
                finish_consecutive = 0

            race_i_expected_points += np.average(self.points[:i+1])
            # Maybe penalty for variance

            self.expected_points[i+1] = race_i_expected_points

        self.points = np.array(points)

    def get_points(self, GP_number):
        if GP_number >= self.N_GP:
            raise Exception("No points data for GP number " + str(GP_number))
        return self.points[GP_number]

    def get_expected_points(self, GP_number):
        if GP_number > self.N_GP:
            raise Exception("Cannot predict points for GP number " + str(GP_number))
        return self.expected_points[GP_number]

    def get_price(self, GP_number):
        if GP_number > self.N_GP:
            raise Exception("No price data for GP number " + str(GP_number))
        return self.prices[GP_number]


class Driver(Variable):
    def __init__(self, name, start_point_expectation, prices: list, points: list, race_positions: list, qualy_positions: list):
        top10_race = np.zeros(len(race_positions))
        top10_race[np.array(race_positions) >= 10] = 1
        top10_qualy = np.zeros(len(qualy_positions))
        top10_qualy[np.array(qualy_positions) >= 10] = 1
        super(Driver, self).__init__(name, start_point_expectation, prices, points, race_positions, top10_race, qualy_positions, top10_qualy, 5)


class Team(Variable):
    def __init__(self, name, start_point_expectation, prices: list, points: list, driver1: Driver, driver2: Driver):
        top10_race = np.zeros(len(points))
        top10_race[np.array(driver1.race_positions) >= 10 and np.array(driver2.race_positions) >= 10] = 1
        top10_qualy = np.zeros(len(points))
        top10_qualy[np.array(driver1.qualy_positions) >= 10 and np.array(driver2.qualy_positions) >= 10] = 1
        average_race_position = (driver1.race_positions + driver2.race_positions) / 2
        average_qualy_position = (driver1.qualy_positions + driver2.qualy_positions) / 2
        super(Team, self).__init__(name, start_point_expectation, prices, points, average_race_position, top10_race, average_qualy_position, top10_qualy, 3)


if __name__ == '__main__':
    a = Variable("Vettel", 20, prices=[20.4, 20.5, 20.7, 20.7, 20, 20, 20], points=[22, 13, 20, 21, 30, 14], qualy_positions=[5, 4, 6, 10, 3, 5], race_positions=[5, 3, 8, 9, 12, 8], streak_length=5)
