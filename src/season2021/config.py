from src.season2021.variable import Team, Driver

GPs = ["Bahrain", "Imola", "Portugal", "Spain", "Monaco", "Azerbaijan", "France", "Styria", "Austria", "Great Britain", "Hungary", "Belgium", "Netherlands", "Monza", "Russia", "Turkey", "United States", "Mexico", "Brazil", "Qatar", "Saudi Arabia", "Abu Dhabi"]

# -------------- Mercedes --------------
team1_driver1 = Driver(name="Hamilton",
                       start_point_expectation=40.82,
                       prices=[33.5, 33.4, 33.3, 33.3, 33.3, 33.2, 33.1, 33.1, 33.0, 33.0, 33.0, 33.0, 33.0, 33.0, 33.0],
                       points=[45, 40, 43, 44, 37, 5, 36, 38, 25, 65, 45, 22.5, 41, 1, 52],
                       race_positions=[1, 2, 1, 1, 7, 15, 2, 2, 4, 1, 2, 3, 2, 17, 1],
                       qualy_positions=[2, 1, 2, 1, 7, 2, 2, 3, 4, 1, 1, 3, 2, 2, 4])
team1_driver2 = Driver(name="Bottas",
                       start_point_expectation=25.59,
                       prices=[23.6, 23.5, 23.3, 23.3, 23.1, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.4],
                       points=[32, -9, 32, 27, 3, 4, 22, 34, 37, 41, -3, 7.5, 27, 57, 33],
                       race_positions=[3, 18, 3, 3, 19, 12, 4, 3, 2, 3, 15, 12, 3, 3, 5],
                       qualy_positions=[3, 8, 1, 3, 3, 10, 3, 2, 5, 3, 2, 8, 3, 1, 7])
team1 = Team(name="Mercedes",
             start_point_expectation=59.6,
             prices=[38.0, 37.8, 37.6, 37.6, 37.5, 37.3, 37.3, 37.2, 37.2, 37.1, 37.1, 37.1, 37.1, 37.2, 37.2, 37.2],
             points=[67, 36, 70, 66, 25, 9, 53, 62, 72, 86, 42, 32, 58, 66, 75],
             driver1=team1_driver1,
             driver2=team1_driver2)

# -------------- Red Bull --------------
team2_driver1 = Driver(name="Verstappen",
                       start_point_expectation=26.88,
                       prices=[24.8, 25.1, 25.3, 25.3, 25.4, 25.5, 25.5, 25.6, 25.7, 25.7, 25.7, 25.7, 25.7, 25.7, 25.6],
                       points=[35, 44, 37, 41, 60, 9, 49, 44, 49, 18, 9, 32, 44, 14, 33],
                       race_positions=[2, 1, 2, 2, 1, 17, 1, 1, 1, 19, 9, 1, 1, 17, 2],
                       qualy_positions=[1, 3, 3, 2, 2, 3, 1, 1, 1, 2, 3, 1, 1, 3, 20])
team2_driver2 = Driver(name="Perez",
                       start_point_expectation=21.5,
                       prices=[18.4, 18.4, 18.3, 18.2, 18.0, 18.2, 18.4, 18.8, 18.8, 18.8, 18.6, 18.5, 18.4, 18.4, 18.3],
                       points=[23, 5, 23, 23, 28, 51, 38, 22, 14, 22, 0, 3, 16, 28, 8],
                       race_positions=[5, 11, 4, 5, 4, 1, 3, 4, 6, 16, 15, 20, 8, 5, 9],
                       qualy_positions=[11, 2, 4, 8, 9, 7, 4, 5, 3, 5, 4, 7, 16, 9, 9])
team2 = Team(name="Red Bull",
             start_point_expectation=48.0,
             prices=[25.9, 26.0, 26.1, 26.1, 26.0, 26.1, 26.2, 26.5, 26.6, 26.7, 26.6, 26.6, 26.6, 26.4, 26.4, 26.4],
             points=[53, 44, 55, 59, 78, 45, 72, 61, 63, 43, 14, 29, 55, 47, 36],
             driver1=team2_driver1,
             driver2=team2_driver2)

# -------------- McLaren --------------
team3_driver1 = Driver(name="Riccardo",
                       start_point_expectation=21.41,
                       prices=[17.3, 16.7, 16.5, 16.2, 16.2, 16.0, 15.9, 15.9, 15.8, 15.8, 15.8, 15.7, 15.7, 15.7, 15.8],
                       points=[15, 19, 14, 23, 3, 13, 21, 3, 19, 27, 6, 20, 5, 58, 27],
                       race_positions=[7, 6, 9, 6, 12, 9, 6, 13, 7, 5, 11, 4, 11, 1, 4],
                       qualy_positions=[6, 6, 16, 7, 12, 13, 10, 13, 13, 7, 11, 4, 10, 5, 5])
team3_driver2 = Driver(name="Norris",
                       start_point_expectation=17.71,
                       prices=[13.1, 13.4, 13.7, 13.9, 13.9, 13.9, 13.9, 14.0, 14.0, 14.1, 14.2, 14.2, 14.2, 14.2, 14.2],
                       points=[29, 34, 27, 12, 49, 32, 28, 22, 31, 53, -5, 6, 13, 41, 17],
                       race_positions=[4, 3, 5, 8, 3, 5, 5, 5, 3, 4, 15, 14, 10, 2, 7],
                       qualy_positions=[7, 7, 7, 9, 5, 6, 8, 4, 2, 6, 6, 10, 13, 4, 1])
team3 = Team(name="McLaren",
             start_point_expectation=30.4,
             prices=[18.9, 18.7, 18.8, 18.9, 18.7, 18.6, 18.6, 18.6, 18.6, 18.6, 18.6, 18.7, 18.6, 18.8, 18.8, 18.8],
             points=[39, 48, 46, 30, 32, 40, 44, 20, 45, 58, 11, 22, 13, 87, 34],
             driver1=team3_driver1,
             driver2=team3_driver2)

# -------------- Ferrari --------------
team4_driver1 = Driver(name="Leclerc",
                       start_point_expectation=14.0,
                       prices=[16.8, 17.4, 17.8, 18.0, 18.3, 18.3, 18.0, 17.6, 17.6, 17.5, 17.6, 17.6, 17.7, 17.7, 17.6],
                       points=[20, 28, 22, 28, 5, 25, -2, 16, 15, 48, -6, 9, 25, 34, 11],
                       race_positions=[6, 4, 6, 4, 19, 4, 16, 7, 8, 2, 15, 8, 5, 4, 15],
                       qualy_positions=[4, 4, 8, 4, 1, 1, 7, 7, 12, 4, 7, 11, 5, 8, 15])
team4_driver2 = Driver(name="Sainz",
                       start_point_expectation=12.0,
                       prices=[14.4, 14.3, 14.4, 14.3, 14.6, 14.7, 14.7, 14.3, 14.3, 14.4, 14.4, 14.5, 14.5, 14.5, 14.4],
                       points=[11, 23, 2, 13, 36, 8, 10, 24, 28, 21, 31, 13, 13, 23, 31],
                       race_positions=[8, 5, 11, 7, 2, 8, 11, 6, 5, 6, 3, 10, 7, 6, 3],
                       qualy_positions=[8, 11, 5, 6, 4, 5, 5, 12, 11, 9, 15, 13, 6, 7, 2])
team4 = Team(name="Ferrari",
             start_point_expectation=21.5,
             prices=[18.1, 18.7, 18.9, 18.7, 19.5, 19.7, 19.3, 18.7, 18.7, 18.7, 18.8, 18.8, 18.8, 18.8, 18.8, 18.8],
             points=[26, 46, 19, 36, 51, 28, -2, 35, 38, 72, 35, 10, 33, 60, 37],
             driver1=team4_driver1,
             driver2=team4_driver2)

# -------------- Aston Martin --------------
team5_driver1 = Driver(name="Vettel",
                       start_point_expectation=10,
                       prices=[16.2, 15.4, 15.1, 15.0, 14.9, 14.9, 15.0, 15.2, 15.2, 15.2, 15.2, 15.2, 15.3, 15.3, 15.3],
                       points=[12, 1, 4, 3, 28, 36, 16, 7, 4, -1, -14, 18, 6, 4, -1],
                       race_positions=[15, 15, 13, 13, 5, 2, 9, 12, 17, 19, 15, 5, 13, 12, 12],
                       qualy_positions=[18, 13, 10, 13, 8, 11, 12, 14, 8, 10, 10, 5, 17, 11, 11])
team5_driver2 = Driver(name="Stroll",
                       start_point_expectation=10.53,
                       prices=[13.9, 13.6, 13.6, 13.5, 13.4, 13.4, 13.3, 13.3, 13.3, 13.3, 13.3, 13.3, 13.3, 13.3, 13.3],
                       points=[11, 22, 8, 8, 17, -20, 7, 16, 0, 22, -13, 4, 8, 22, 4],
                       race_positions=[10, 7, 14, 11, 8, 17, 10, 8, 13, 8, 15, 18, 12, 7, 11],
                       qualy_positions=[10, 10, 17, 11, 13, 19, 19, 10, 10, 15, 12, 15, 12, 12, 8])
team5 = Team(name="Aston Martin",
             start_point_expectation=28.9,
             prices=[17.6, 16.9, 16.6, 16.5, 16.4, 16.4, 16.4, 16.4, 16.4, 16.4, 16.4, 16.5, 16.5, 16.5, 16.5, 16.5],
             points=[18, 18, 7, 6, 40, 31, 23, 18, -1, 29, 6, 18, 9, 19, -2],
             driver1=team5_driver1,
             driver2=team5_driver2)

# -------------- Alpine --------------
team6_driver1 = Driver(name="Alonso",
                       start_point_expectation=13.0,
                       prices=[15.6, 15.2, 15.0, 15.0, 14.8, 14.8, 14.8, 14.8, 14.8, 14.8, 14.9, 15.0, 15.2, 15.2, 15.1],
                       points=[-8, 14, 17, -5, 10, 23, 17, 11, 17, 35, 28, 4, 23, 21, 22],
                       race_positions=[19, 10, 8, 17, 13, 6, 8, 9, 10, 7, 4, 11, 6, 8, 6],
                       qualy_positions=[9, 15, 13, 10, 17, 9, 9, 9, 14, 11, 9, 14, 9, 13, 6])
team6_driver2 = Driver(name="Ocon",
                       start_point_expectation=8.76,
                       prices=[10.1, 9.7, 9.9, 10.3, 10.5, 10.5, 10.4, 10.4, 10.2, 10.1, 10.0, 10.2, 10.3, 10.3, 10.3],
                       points=[11, 13, 18, 9, 14, -13, 0, 8, -14, 10, 47, 13, 9, 20, -5],
                       race_positions=[13, 9, 7, 9, 9, 17, 14, 14, 20, 9, 1, 7, 9, 10, 14],
                       qualy_positions=[16, 9, 6, 5, 11, 12, 11, 9, 17, 13, 8, 9, 8, 14, 10])
team6 = Team(name="Alpine",
             start_point_expectation=28.1,
             prices=[15.4, 15.1, 15.0, 15.2, 15.2, 15.1, 15.3, 15.2, 15.1, 15.1, 15.1, 15.1, 15.2, 15.2, 15.2, 15.2],
             points=[13, 16, 30, -1, 19, 20, 12, 14, 13, 28, 70, 13, 27, 24, 12],
             driver1=team6_driver1,
             driver2=team6_driver2)

# -------------- Alpha Tauri --------------
team7_driver1 = Driver(name="Gasly",
                       start_point_expectation=11.3,
                       prices=[11.7, 11.7, 11.7, 11.7, 11.5, 11.7, 11.8, 11.9, 11.9, 11.9, 11.9, 11.9, 11.9, 11.9, 11.9],
                       points=[2, 13, 10, 13, 22, 43, 18, -5, 15, 8, 30, 16, 28, -10, 6],
                       race_positions=[17, 8, 10, 10, 6, 3, 7, 19, 9, 11, 5, 6, 4, 19, 13],
                       qualy_positions=[5, 5, 9, 12, 6, 4, 6, 6, 6, 12, 5, 6, 4, 6, 12])
team7_driver2 = Driver(name="Tsunoda",
                       start_point_expectation=9.0,
                       prices=[8.8, 9.4, 9.2, 8.9, 8.6, 8.4, 8.4, 8.4, 8.5, 8.5, 8.5, 8.4, 8.3, 8.3, 8.3],
                       points=[16, 6, 2, -14, 2, 13, 6, 13, -2, 17, 20, 3, -13, -10, -2],
                       race_positions=[9, 12, 15, 20, 16, 7, 13, 10, 12, 10, 6, 15, 19, 20, 17],
                       qualy_positions=[13, 20, 14, 16, 16, 8, 19, 8, 7, 16, 16, 17, 15, 17, 13])
team7 = Team(name="Alpha Tauri",
             start_point_expectation=20.9,
             prices=[12.7, 13.2, 13.0, 12.8, 12.6, 12.6, 12.6, 12.7, 12.7, 12.7, 12.7, 12.7, 12.6, 12.6, 12.6, 12.6],
             points=[13, 19, 7, 9, 19, 41, 24, 18, 3, 18, 40, 15, 25, 6, -1],
             driver1=team7_driver1,
             driver2=team7_driver2)

# -------------- Alfa Romeo --------------
team8_driver1 = Driver(name="Raikkonen",
                       start_point_expectation=10.53,
                       prices=[9.6, 9.4, 9.4, 9.3, 9.4, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.2, 9.2, 9.2, 9.1],
                       points=[12, 13, -13, 15, 9, 17, 2, 15, 4, 7, 15, 3, 4, 10, 21],
                       race_positions=[11, 13, 20, 12, 11, 10, 17, 11, 15, 15, 10, 19, 15, 14, 8],
                       qualy_positions=[14, 16, 15, 17, 14, 14, 17, 18, 16, 17, 13, 19, 18, 19, 16])
team8_driver2 = Driver(name="Giovinazzi",
                       start_point_expectation=6.06,
                       prices=[7.9, 7.8, 7.8, 7.8, 7.8, 8.0, 8.0, 8.0, 8.0, 8.0, 8.1, 8.0, 8.0, 8.0, 8.0],
                       points=[5, 8, 8, 4, 11, 6, 6, 5, 10, 12, 5, 6, 3, 8, 4],
                       race_positions=[12, 14, 12, 15, 10, 11, 15, 15, 14, 13, 13, 13, 14, 13, 16],
                       qualy_positions=[12, 17, 12, 14, 10, 19, 13, 15, 15, 14, 14, 16, 7, 10, 18])
team8 = Team(name="Alfa Romeo",
             start_point_expectation=15.1,
             prices=[8.9, 8.9, 8.9, 8.9, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.1, 9.1, 9.1, 9.1],
             points=[12, 22, 5, 14, 15, 23, 3, 15, 9, 12, 15, 5, 2, 11, 20],
             driver1=team8_driver1,
             driver2=team8_driver2)

# -------------- Williams --------------
team9_driver1 = Driver(name="Latifi",
                       start_point_expectation=4.71,
                       prices=[6.5, 6.5, 6.5, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4],
                       points=[1, -13, 2, 8, 8, 5, 0, 4, 6, 10, 21, 5, 16, 11, 2],
                       race_positions=[18, 18, 18, 16, 15, 16, 18, 17, 16, 14, 7, 9, 16, 11, 19],
                       qualy_positions=[17, 14, 18, 19, 18, 16, 16, 16, 18, 18, 18, 12, 14, 16, 14])
team9_driver2 = Driver(name="Russel",
                       start_point_expectation=4.53,
                       prices=[6.2, 6.2, 6.2, 6.3, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.3],
                       points=[10, -11, 3, 10, 10, 3, 12, -11, 5, 16, 18, 25, 0, 21, 8],
                       race_positions=[14, 18, 16, 14, 14, 17, 12, 19, 11, 12, 8, 2, 17, 9, 10],
                       qualy_positions=[15, 12, 11, 15, 15, 15, 14, 11, 9, 8, 17, 2, 11, 15, 3])
team9 = Team(name="Williams",
             start_point_expectation=10.4,
             prices=[6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3],
             points=[6, 4, 0, 13, 13, 3, 7, 3, 6, 19, 34, 26, 11, 25, 5],
             driver1=team9_driver1,
             driver2=team9_driver2)

# -------------- Haas --------------
team10_driver1 = Driver(name="Schumacher",
                        start_point_expectation=4.0,
                        prices=[5.8, 5.7, 5.7, 5.8, 5.9, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.7],
                        points=[11, 11, 11, 7, 0, 15, 4, 13, 9, 8, 9, 6, 6, 13, -12],
                        race_positions=[16, 16, 17, 18, 18, 13, 19, 16, 18, 18, 12, 16, 18, 15, 20],
                        qualy_positions=[19, 18, 19, 18, 20, 17, 15, 19, 19, 19, 20, 18, 19, 18, 17])
team10_driver2 = Driver(name="Mazepin",
                        start_point_expectation=4.0,
                        prices=[5.5, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3],
                        points=[-14, 6, 4, 4, 11, 10, 0, 6, 4, 11, -12, 3, -14, -8, 2],
                        race_positions=[19, 17, 18, 19, 17, 14, 20, 18, 19, 17, 14, 17, 20, 16, 18],
                        qualy_positions=[20, 19, 20, 20, 19, 18, 18, 20, 20, 20, 19, 20, 20, 20, 19])
team10 = Team(name="Haas",
              start_point_expectation=9.6,
              prices=[6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1],
              points=[7, 12, 10, 6, 11, 20, -1, 14, 8, 12, 12, 5, 2, 13, 0],
              driver1=team10_driver1,
              driver2=team10_driver2)

# ---------------------------------------------------------------------------------------------------- #

driver_map = {
    team1_driver1.name: team1_driver1,
    team1_driver2.name: team1_driver2,
    team2_driver1.name: team2_driver1,
    team2_driver2.name: team2_driver2,
    team3_driver1.name: team3_driver1,
    team3_driver2.name: team3_driver2,
    team4_driver1.name: team4_driver1,
    team4_driver2.name: team4_driver2,
    team5_driver1.name: team5_driver1,
    team5_driver2.name: team5_driver2,
    team6_driver1.name: team6_driver1,
    team6_driver2.name: team6_driver2,
    team7_driver1.name: team7_driver1,
    team7_driver2.name: team7_driver2,
    team8_driver1.name: team8_driver1,
    team8_driver2.name: team8_driver2,
    team9_driver1.name: team9_driver1,
    team9_driver2.name: team9_driver2,
    team10_driver1.name: team10_driver1,
    team10_driver2.name: team10_driver2,
}

team_map = {
    team1.name: team1,
    team2.name: team2,
    team3.name: team3,
    team4.name: team4,
    team5.name: team5,
    team6.name: team6,
    team7.name: team7,
    team8.name: team8,
    team9.name: team9,
    team10.name: team10,
}

info = {
    "N_GP": -1
}


def check_missing_data():
    import numpy as np
    teams = []
    for team_name in team_map:
        teams.append(team_map[team_name])
    drivers = []
    for driver_name in driver_map:
        drivers.append(driver_map[driver_name])

    team_points_N = np.array(list(map(lambda team: len(team.points), teams)))
    driver_points_N = np.array(list(map(lambda driver: len(driver.points), drivers)))

    N_GP = max(np.max(team_points_N), np.max(driver_points_N))
    info["N_GP"] = N_GP
    missing = False
    for i in range(len(teams)):
        if team_points_N[i] < N_GP:
            missing = True
            print("Missing data for team: " + teams[i].name)
    for i in range(len(drivers)):
        if driver_points_N[i] < N_GP:
            missing = True
            print("Missing data for driver: " + drivers[i].name)
    if missing:
        raise Exception("Missing data")

    if N_GP > len(GPs):
        raise Exception("Missing GP names")


check_missing_data()
