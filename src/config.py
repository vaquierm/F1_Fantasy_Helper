from src.variable import Variable

team1 = Variable(name="Mercedes", points=644, price=32.3, top10_qualy=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], top10_finish=[1, 1, 1, 0, 1, 1, 1, 1, 1, 1], streak_length=3)
team1_driver1 = Variable(name="Hamilton", points=414, price=31.4, top10_qualy=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], top10_finish=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], streak_length=5)
team1_driver2 = Variable(name="Botas", points=315, price=29.4, top10_qualy=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], top10_finish=[1, 1, 1, 0, 1, 1, 1, 1, 1, 1], streak_length=5)

team2 = Variable(name="Red Bull", points=438, price=24.2, top10_qualy=[1, 1, 0, 0, 1, 1, 1, 1, 1, 1], top10_finish=[0, 1, 1, 1, 1, 1, 1, 0, 0, 0], streak_length=3)
team2_driver1 = Variable(name="Verstappen", points=278, price=26.1, top10_qualy=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], top10_finish=[0, 1, 1, 1, 1, 1, 1, 0, 0, 1], streak_length=5)
team2_driver2 = Variable(name="Albon", points=175, price=20.5, top10_qualy=[1, 1, 0, 0, 1, 1, 1, 1, 1, 1], top10_finish=[0, 1, 1, 1, 1, 1, 1, 0, 1, 0], streak_length=5)

team3 = Variable(name="Racing Point", points=287, price=11.0, top10_qualy=[1, 0, 1, 0, 1, 1, 1, 1, 1, 0], top10_finish=[0, 1, 1, 0, 1, 1, 1, 1, 0, 0], streak_length=3)
team3_driver1 = Variable(name="Stroll", points=135, price=10.6, top10_qualy=[1, 0, 1, 1, 1, 1, 1, 1, 1, 0], top10_finish=[0, 1, 1, 1, 1, 1, 1, 1, 0, 0], streak_length=5)
team3_driver2 = Variable(name="Perez", points=157, price=9.9, top10_qualy=[1, 0, 1, 0, 1, 1, 1, 1, 1, 1], top10_finish=[1, 1, 1, 0, 1, 1, 1, 1, 1, 1], streak_length=5)

team4 = Variable(name="McLaren", points=258, price=15.7, top10_qualy=[1, 1, 1, 1, 0, 1, 1, 1, 0, 1], top10_finish=[1, 1, 0, 0, 0, 1, 0, 1, 0, 0], streak_length=3)
team4_driver1 = Variable(name="Norris", points=192, price=13.0, top10_qualy=[1, 1, 1, 1, 1, 1, 1, 1, 0, 1], top10_finish=[1, 1, 0, 1, 1, 1, 1, 1, 1, 0], streak_length=5)
team4_driver2 = Variable(name="Sainz", points=91, price=15.3, top10_qualy=[1, 1, 1, 1, 0, 1, 1, 1, 1, 1], top10_finish=[1, 1, 1, 0, 0, 1, 0, 1, 0, 0], streak_length=5)

team5 = Variable(name="Renault", points=276, price=12.3, top10_qualy=[0, 1, 0, 1, 0, 0, 1, 0, 0, 1], top10_finish=[0, 0, 0, 1, 0, 0, 1, 1, 0, 1], streak_length=3)
team5_driver1 = Variable(name="Riccardo", points=181, price=14.2, top10_qualy=[1, 1, 0, 1, 1, 0, 1, 1, 1, 1], top10_finish=[0, 1, 1, 1, 0, 0, 1, 1, 1, 1], streak_length=5)
team5_driver2 = Variable(name="Ocon", points=105, price=12.1, top10_qualy=[0, 1, 0, 1, 0, 0, 1, 0, 0, 1], top10_finish=[1, 0, 0, 1, 1, 0, 1, 1, 0, 1], streak_length=5)

team6 = Variable(name="Ferrari", points=202, price=25.8, top10_qualy=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], top10_finish=[1, 0, 0, 1, 0, 0, 0, 0, 1, 0], streak_length=3)
team6_driver1 = Variable(name="Leclerc", points=114, price=23.3, top10_qualy=[1, 0, 1, 1, 1, 1, 0, 0, 1, 0], top10_finish=[1, 0, 0, 1, 1, 0, 0, 0, 1, 1], streak_length=5)
team6_driver2 = Variable(name="Vettel", points=57, price=20.4, top10_qualy=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], top10_finish=[1, 0, 1, 1, 0, 1, 0, 0, 1, 0], streak_length=5)

team7 = Variable(name="AlphaTauri", points=199, price=12.8, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 1, 0, 1], streak_length=3)
team7_driver1 = Variable(name="Gasly", points=111, price=10.9, top10_qualy=[0, 1, 1, 0, 1, 1, 0, 1, 0, 1], top10_finish=[1, 0, 0, 1, 0, 1, 1, 1, 0, 1], streak_length=5)
team7_driver2 = Variable(name="Kvyat", points=93, price=9.8, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 1, 0, 0, 1, 0, 0, 1, 1, 1], streak_length=5)

team8 = Variable(name="Alpha Romeo", points=153, price=8.3, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=3)
team8_driver1 = Variable(name="Giovinazzi", points=61, price=8.7, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=5)
team8_driver2 = Variable(name="Raikkonen", points=97, price=9.5, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 1, 0], streak_length=5)

team9 = Variable(name="Haas", points=101, price=7.8, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=3)
team9_driver1 = Variable(name="Grosjean", points=54, price=5.8, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=5)
team9_driver2 = Variable(name="Magnussen", points=-1, price=7.6, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], streak_length=5)

team10 = Variable(name="Williams", points=97, price=6.3, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=3)
team10_driver1 = Variable(name="Russel", points=46, price=5.9, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=5)
team10_driver2 = Variable(name="Latifi", points=56, price=6.6, top10_qualy=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], top10_finish=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], streak_length=5)

# INPUT YOUR CURRENT TEAM AND DRIVERS HERE
my_team = team1
my_drivers = [team1_driver1, team3_driver1, team3_driver2, team4_driver1, team9_driver1]

# INPUT YOUR TOTAL BUDGET HERE
budget = 105.0

# True or False do you have a wildcard available
wildcard = False
