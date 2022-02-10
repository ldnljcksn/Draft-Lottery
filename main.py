import random
import pandas as pd


teams_wins_dict = {'Houston': 0,
                   'Detroit': 1,
                   'Orlando': 2,
                   'Oklahoma City': 3,
                   'Cleveland': 4,
                   'Minnesota': 5,
                   'Toronto': 6,
                   'Sacramento': 7,
                   'Chicago': 8,
                   'New Orleans': 9,
                   'Charlotte': 10,
                   'San Antonio': 11,
                   'Indiana': 12,
                   'Golden State': 13
                   }

draft_odds = [[0 for i in range(14)] for j in range(14)]
team_first = 0
runs = 100000
for j in range(0, runs):
    draft_list = []
    team = None
    i = 0
    while i < 14:
        num = random.randrange(0, 384)
        if num in range(0, 17):
            team = 'Houston'
        elif num in range(17, 37):
            team = 'Detroit'
        elif num in range(37, 58):
            team = 'Orlando'
        elif num in range(58, 80):
            team = 'Oklahoma City'
        elif num in range(80, 102):
            team = 'Cleveland'
        elif num in range(102, 125):
            team = 'Minnesota'
        elif num in range(125, 152):
            team = 'Toronto'
        elif num in range(152, 183):
            team = 'Sacramento'
        elif num in range(183, 214):
            team = 'Chicago'
        elif num in range(214, 245):
            team = 'New Orleans'
        elif num in range(245, 278):
            team = 'Charlotte'
        elif num in range(278, 311):
            team = 'San Antonio'
        elif num in range(311, 345):
            team = 'Indiana'
        elif num in range(345, 384):
            team = 'Golden State'

        if team not in draft_list:
            draft_list.append(team)
            # print(str(14 - i) + '.', team, str(teams_wins_dict[team]) + '-' + str(82 - teams_wins_dict[team]))
            i += 1

    for each_team in draft_list:
        draft_odds[teams_wins_dict[each_team]][13 - draft_list.index(each_team)] += 1


for each_line in draft_odds:
    each_line = [(100 * x / runs) for x in each_line]
    print(each_line)

df = pd.DataFrame(draft_odds)
df.to_csv('draft_odds.csv', index=False, header=False)
