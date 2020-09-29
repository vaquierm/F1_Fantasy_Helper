# 🏎 F1 Fantasy Helper

Every year during the formula 1 season, many of the fans partake in a game of [fantasy](https://fantasy.formula1.com) to see who can make th best predictions.
This program uses initeger linear programming and statistics from previous races of the season to maximize the expectation of points and returns the best team to do so.
The results of the analysis can help the player pick the best team, advice you on when to trade which drivers, and wich driver to play special cards (See the rules of the game) on.

## Rules of the game

### 📃 Picking your team

The player starts with a budget of 100m. The player must pick a team concisting of 1 car constructor and 5 drivers. Each drivers and car constructor have a price based on their performance in the last Formula 1 season.

Here is an example team 

<p align="center">
  <img src="img/example_team.PNG" width="300" />
</p>

### 💨 Turbo Driver

Each week, you can select one driver below the price of 20m to be your Turbo Driver (TD). The points that this driver will earn will be doubled for this raceweek. This card can be moved to any of your drivers for free each week. However, if the driver does not finish the race and loses points, the lost points are also doubled which is a risk to think about.

### ♻ Substitutions

Each week, the player can decide to trade drivers and car constructor. One substitution is free each week. However, additional substitution will cost 10 points each. 

### 🃏 Wildcard

The player only has two wildcard play throughout the season. One in the first half, and one in the second half. When playing the wildcard, the player can make as many substitutions they like for free before the next race.

### 📈 Dynamic Pricing

<p align="center">
  <img src="img/dynamic_pricing.PNG" width="350" />
</p>

Each week, all substitutions are aggregated and price changes are applied to the drivers and constructors. When many players wand to trade a certain driver onto their team, their price increases. Same goes for price decrease.

## Point System

### Qualyfying

- **1pt** Did not progress to Q2
- **2pts** Progressed to Q2 but did not progress to Q3
- **3pts** Progressed to Q3
- **2pts** Qualified ahead of team mate (driver only)
- **-5pts** Did not qualify (driver only)
- **-10pts** Disqualification from qualifying (driver only)

Qualifying Position Bonuses:

**10pts** pole, **9pts** 2nd, **8pts** 3rd, **7pts** 4th, **6pts** 5th, **5pts** 6th, **4pts** 7th, **3pts** 8th, **2pts** 9th, **1pt** 10th

### Race
- **1pt** Finished race
- **3pts** Finished ahead of team mate (driver only)
- **2pts** Finished race, position gained (per place gained, max. +10 pts)
- **5pts** Fastest lap (driver only)
- **-2pts** Started race within Top 10, finished race but lost position (per place lost, max. -10 pts)
- **-1pt** Started race outside Top 10, finished race but lost position (per place lost, max. -5 pts)
- **-15pts** Does not finish (driver only)
- **-20pts** Disqualification from race (driver only)

Race Finish Bonuses:

**25pts** 1st, **18pts** 2nd, **15pts** 3rd, **12pts** 4th, **10pts** 5th, **8pts** 6th, **6pts** 7th, **4pts** 8th, **2pts** 9th, **1pt** 10th

### Streaks

- **5pts** Driver Qualifying - driver qualifies in Top 10 for 5 races in a row
- **10pts** Driver Race - driver finishes race in Top 10 for 5 races in a row
- **5pts** Constructor Qualifying - both drivers qualify in Top 10 for 3 races in a row
- **10pts** Constructor Race - both drivers finish race in Top 10 for 3 races in a row

<p align="center">
  <img src="img/streaks.PNG" width="350" />
</p>

These streaks are very important to think about when substituing drivers. If a driver that is not in the players team is about to reach both the qualifying and race finish streaks, it might be worth it to pay a substitution penalty of 10 points to get this driver onto the team. This way, with the TD card, this driver could potentially rack up an additional 30 points on top of the regular points that it will get from the regular scoring. In the above picture, we can see that Riccardo is about to reach both streaks (indicated by the Q and R counters where he has 4/5). Riccardo has been pretty concistant in finishing in the top 10 and will likely achieve the streak. This is a good trade, which also has potential to increase your total budget as many people will want hin on their team, his price is likely to increase lots this raceweek.



