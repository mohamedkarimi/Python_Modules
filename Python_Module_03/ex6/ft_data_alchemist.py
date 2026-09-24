import random

print("=== Game Data Alchemist ===")

players = ['Alice', 'bob', 'Charlie', 'dylan',
           'Emma', 'Gregory', 'john', 'kevin', 'Liam']

all_capitalized = [name.capitalize() for name in players]
capitalized_only = [name for name in players if name[0]
                    >= 'A' and name[0] <= 'Z']

score_dict = {name: random.randint(0, 1000) for name in all_capitalized}
score_average = round(sum(score_dict.values()) / len(score_dict), 2)
high_scores = {name: score for name,
               score in score_dict.items() if score > score_average}

print("Initial list of players:", players)
print("New list with all names capitalized:", all_capitalized)
print("New list of capitalized names only:", capitalized_only)
print("Score dict:", score_dict)
print("Score average is", score_average)
print("High scores:", high_scores)
