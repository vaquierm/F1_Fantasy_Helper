from src.variable import Variable

team1 = Variable(name="Mercedes", points=882, price=32.4, top10_qualy=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], top10_finish=[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0], streak_length=3)
team1_driver1 = Variable(name="Hamilton", points=603, price=31.5, top10_qualy=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], top10_finish=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], streak_length=5)
team1_driver2 = Variable(name="Botas", points=374, price=29.4, top10_qualy=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], top10_finish=[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0], streak_length=5)

team2 = Variable(name="Red Bull", points=544, price=24.2, top10_qualy=[1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], top10_finish=[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], streak_length=3)
team2_driver1 = Variable(name="Verstappen", points=368, price=26.1, top10_qualy=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], top10_finish=[0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1], streak_length=5)
team2_driver2 = Variable(name="Albon", points=186, price=20.3, top10_qualy=[1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], top10_finish=[0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1], streak_length=5)

team3 = Variable(name="Racing Point", points=441, price=10.8, top10_qualy=[1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1], top10_finish=[0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1], streak_length=3)
team3_driver1 = Variable(name="Stroll", points=153, price=10.2, top10_qualy=[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1], top10_finish=[0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1], streak_length=5)
team3_driver2 = Variable(name="Perez", points=278, price=9.9, top10_qualy=[1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], top10_finish=[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], streak_length=5)

team4 = Variable(name="McLaren", points=378, price=15.7, top10_qualy=[1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], top10_finish=[1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1], streak_length=3)
team4_driver1 = Variable(name="Norris", points=220, price=12.8, top10_qualy=[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0], top10_finish=[1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1], streak_length=5)
team4_driver2 = Variable(name="Sainz", points=188, price=15.1, top10_qualy=[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0], top10_finish=[1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1], streak_length=5)

team5 = Variable(name="Renault", points=372, price=12.7, top10_qualy=[0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1], top10_finish=[0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0], streak_length=3)
team5_driver1 = Variable(name="Riccardo", points=282, price=14.5, top10_qualy=[1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], top10_finish=[0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], streak_length=5)
team5_driver2 = Variable(name="Ocon", points=100, price=12.0, top10_qualy=[0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1], top10_finish=[1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0], streak_length=5)

team6 = Variable(name="Ferrari", points=335, price=25.6, top10_qualy=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1], streak_length=3)
team6_driver1 = Variable(name="Leclerc", points=220, price=23.3, top10_qualy=[1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0], top10_finish=[1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], streak_length=5)
team6_driver2 = Variable(name="Vettel", points=114, price=20.3, top10_qualy=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1], streak_length=5)

team7 = Variable(name="AlphaTauri", points=303, price=12.9, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], streak_length=3)
team7_driver1 = Variable(name="Gasly", points=178, price=11.1, top10_qualy=[0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0], top10_finish=[1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0], streak_length=5)
team7_driver2 = Variable(name="Kvyat", points=135, price=9.9, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], top10_finish=[0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0], streak_length=5)

team8 = Variable(name="Alpha Romeo", points=223, price=8.4, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], streak_length=3)
team8_driver1 = Variable(name="Giovinazzi", points=86, price=8.6, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], top10_finish=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], streak_length=5)
team8_driver2 = Variable(name="Raikkonen", points=147, price=9.5, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0], streak_length=5)

team9 = Variable(name="Haas", points=140, price=7.8, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=3)
team9_driver1 = Variable(name="Grosjean", points=74, price=6.0, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], streak_length=5)
team9_driver2 = Variable(name="Magnussen", points=8, price=7.5, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=5)

team10 = Variable(name="Williams", points=142, price=6.6, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=3)
team10_driver1 = Variable(name="Russel", points=46, price=5.8, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=5)
team10_driver2 = Variable(name="Latifi", points=76, price=6.6, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=5)

# INPUT YOUR CURRENT TEAM AND DRIVERS HERE
#my_team = team1
#my_drivers = [team1_driver1, team3_driver2, team5_driver1, team7_driver1, team9_driver1]
#my_team = team3
#my_drivers = [team1_driver1, team3_driver1, team3_driver2, team4_driver1, team2_driver1]
my_team = team1
my_drivers = [team2_driver1, team4_driver1, team5_driver1, team8_driver1, team10_driver1]
#my_team = team3
#my_drivers = [team1_driver2, team2_driver1, team3_driver1, team3_driver2, team4_driver1]

# INPUT YOUR TOTAL BUDGET HERE
budget = 100.3


# True or False do you have a wildcard available
wildcard = True
