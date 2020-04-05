#testcomment and two
from random import random
from itertools import combinations 
from operator import itemgetter, attrgetter

game_results = []
for i in range(30):
	game_results.append([i, 0, 0]) #stored as team num, wins, losses

#Simulates play between two teams
def game_play(t1, r1, t2, r2): #t1 - num of team 1, r1 - ranking of t1 0-1, etc.
	if (r1+r2)*random() < r1:
		game_results[t1][1] += 1
		game_results[t2][2] += 1
	else:
		game_results[t1][2] += 1
		game_results[t2][1] += 1

rating = []
for i in range(6):
	div_rating = []
	for j in range(5):
		div_rating.append([i*5+j,random()]) # ratings for teams are randomly generated and held throughout season
	rating.append(div_rating)

for i in rating: #16 in division games
	div_games = list(combinations(i,2))
	for j in div_games:
		for k in range(4):
			game_play(j[0][0],j[0][1],j[1][0],j[1][1]) 

for i in range(2): #3 in conference, out of division games, 6 games missing
	inter_div = list(combinations(range(3),2))
	for j in inter_div:
		for k in range(5):
			for l in range(5):
				for m in range(3):
					t1 = rating[j[0] + 3*i][k]
					t2 = rating[j[1] + 3*i][l]
					game_play(t1[0],t1[1],t2[0],t2[1])



conf_1 = rating[0]+rating[1]+rating[2] #merge divs into conferences
conf_2 = rating[3]+rating[4]+rating[5]
for i in conf_1: #30 out of conference games
	for j in conf_2:
		for k in range(2):
			game_play(i[0],i[1],j[0],j[1])

conf_1_r = sorted(game_results[0:15], key = lambda x: x[2]) #sort based on wins
conf_2_r = sorted(game_results[15:30], key = lambda x: x[2])

for i in conf_1_r:
	print i

print '\n'

for i in conf_2_r:
	print i