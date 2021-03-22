from src.season2021.variable import Team, Driver

GPs = ["Bahrain", "Italy"]

# -------------- Mercedes --------------
team1_driver1 = Driver(name="Hamilton",
                       start_point_expectation=40.82,
                       prices=[33.5, 33.5],
                       points=[39],
                       race_positions=[1],
                       qualy_positions=[1])
team1_driver2 = Driver(name="Bottas",
                       start_point_expectation=25.59,
                       prices=[23.6, 23],
                       points=[23],
                       race_positions=[2],
                       qualy_positions=[2])
team1 = Team(name="Mercedes",
             start_point_expectation=59.6,
             prices=[38.0, 38.1],
             points=[60],
             driver1=team1_driver1,
             driver2=team1_driver2)

# -------------- Red Bull --------------
team2_driver1 = Driver(name="Verstappen",
                       start_point_expectation=26.88,
                       prices=[24.8, 24.9],
                       points=[25],
                       race_positions=[3],
                       qualy_positions=[3])
team2_driver2 = Driver(name="Perez",
                       start_point_expectation=21.5,
                       prices=[18.4, 18.5],
                       points=[20],
                       race_positions=[4],
                       qualy_positions=[4])
team2 = Team(name="Red Bull",
             start_point_expectation=48.0,
             prices=[25.9, 25.9],
             points=[48],
             driver1=team2_driver1,
             driver2=team2_driver2)

# -------------- McLaren --------------
team3_driver1 = Driver(name="Riccardo",
                       start_point_expectation=21.41,
                       prices=[17.3, 17.3],
                       points=[19],
                       race_positions=[20],
                       qualy_positions=[20])
team3_driver2 = Driver(name="Norris",
                       start_point_expectation=17.71,
                       prices=[13.1, 13],
                       points=[12],
                       race_positions=[5],
                       qualy_positions=[5])
team3 = Team(name="McLaren",
             start_point_expectation=30.4,
             prices=[18.9, 19],
             points=[13],
             driver1=team3_driver1,
             driver2=team3_driver2)

# -------------- Ferrari --------------
team4_driver1 = Driver(name="Leclerc",
                       start_point_expectation=14.0,
                       prices=[16.8, 17],
                       points=[15],
                       race_positions=[6],
                       qualy_positions=[6])
team4_driver2 = Driver(name="Sainz",
                       start_point_expectation=12.0,
                       prices=[14.4, 14],
                       points=[13],
                       race_positions=[7],
                       qualy_positions=[7])
team4 = Team(name="Ferrari",
             start_point_expectation=21.5,
             prices=[18.1, 18],
             points=[20],
             driver1=team4_driver1,
             driver2=team4_driver2)

# -------------- Aston Martin --------------
team5_driver1 = Driver(name="Vettel",
                       start_point_expectation=10,
                       prices=[16.2, 16],
                       points=[13],
                       race_positions=[8],
                       qualy_positions=[8])
team5_driver2 = Driver(name="Stroll",
                       start_point_expectation=10.53,
                       prices=[13.9, 14],
                       points=[13],
                       race_positions=[9],
                       qualy_positions=[9])
team5 = Team(name="Aston Martin",
             start_point_expectation=28.9,
             prices=[17.6, 18],
             points=[27],
             driver1=team5_driver1,
             driver2=team5_driver2)

# -------------- Alpine --------------
team6_driver1 = Driver(name="Alonso",
                       start_point_expectation=13.0,
                       prices=[15.6, 16],
                       points=[12],
                       race_positions=[10],
                       qualy_positions=[10])
team6_driver2 = Driver(name="Ocon",
                       start_point_expectation=8.76,
                       prices=[10.10, 10],
                       points=[5],
                       race_positions=[11],
                       qualy_positions=[11])
team6 = Team(name="Alpine",
             start_point_expectation=28.1,
             prices=[15.4, 15],
             points=[25],
             driver1=team6_driver1,
             driver2=team6_driver2)

# -------------- Alpha Tauri --------------
team7_driver1 = Driver(name="Gasly",
                       start_point_expectation=11.3,
                       prices=[11.7, 12],
                       points=[11],
                       race_positions=[12],
                       qualy_positions=[12])
team7_driver2 = Driver(name="Tsunoda",
                       start_point_expectation=9.0,
                       prices=[8.8, 9],
                       points=[2],
                       race_positions=[13],
                       qualy_positions=[13])
team7 = Team(name="Alpha Tauri",
             start_point_expectation=20.9,
             prices=[12.7, 13],
             points=[21],
             driver1=team7_driver1,
             driver2=team7_driver2)

# -------------- Alfa Romeo --------------
team8_driver1 = Driver(name="Raikkonen",
                       start_point_expectation=10.53,
                       prices=[9.6, 10],
                       points=[13],
                       race_positions=[14],
                       qualy_positions=[14])
team8_driver2 = Driver(name="Giovinazzi",
                       start_point_expectation=6.06,
                       prices=[7.9, 8],
                       points=[3],
                       race_positions=[15],
                       qualy_positions=[15])
team8 = Team(name="Alfa Romeo",
             start_point_expectation=15.1,
             prices=[8.9, 9],
             points=[11],
             driver1=team8_driver1,
             driver2=team8_driver2)

# -------------- Williams --------------
team9_driver1 = Driver(name="Latifi",
                       start_point_expectation=4.71,
                       prices=[6.5, 6.5],
                       points=[2],
                       race_positions=[16],
                       qualy_positions=[16])
team9_driver2 = Driver(name="Russel",
                       start_point_expectation=4.53,
                       prices=[6.2, 6],
                       points=[5],
                       race_positions=[17],
                       qualy_positions=[17])
team9 = Team(name="Williams",
             start_point_expectation=10.4,
             prices=[6.3, 6.4],
             points=[4],
             driver1=team9_driver1,
             driver2=team9_driver2)

# -------------- Haas --------------
team10_driver1 = Driver(name="Schumacher",
                        start_point_expectation=4.0,
                        prices=[5.8, 6],
                        points=[5],
                        race_positions=[18],
                        qualy_positions=[18])
team10_driver2 = Driver(name="Mazepin",
                        start_point_expectation=4.0,
                        prices=[5.5, 5.5],
                        points=[2],
                        race_positions=[19],
                        qualy_positions=[19])
team10 = Team(name="Haas",
              start_point_expectation=9.6,
              prices=[6.1, 6],
              points=[7],
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


check_missing_data()
