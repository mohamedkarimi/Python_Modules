import random


ALL_ACHIEVEMENTS = (
    "First Steps",
    "Speed Runner",
    "Treasure Hunter",
    "Boss Slayer",
    "Master Explorer",
    "Crafting Genius",
    "Sharp Mind",
    "World Savior",
    "Collector Supreme",
    "Strategist",
    "Survivor",
    "Unstoppable",
    "Hidden Path Finder",
    "Untouchable",
)


def gen_player_achievements():
    common_achievement = set(("Untouchable",))
    other_achievements = (
        "First Steps",
        "Speed Runner",
        "Treasure Hunter",
        "Boss Slayer",
        "Master Explorer",
        "Crafting Genius",
        "Sharp Mind",
        "World Savior",
        "Collector Supreme",
        "Strategist",
        "Survivor",
        "Unstoppable",
        "Hidden Path Finder",
    )
    count = random.randint(4, 8)
    random_achievements = set(random.sample(other_achievements, count))
    return common_achievement.union(random_achievements)


print("=== Achievement Tracker System ===")

alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

print("Player Alice:", alice)
print("Player Bob:", bob)
print("Player Charlie:", charlie)
print("Player Dylan:", dylan)

all_distinct = alice.union(bob).union(charlie).union(dylan)
common_achievements = alice.intersection(
    bob).intersection(charlie).intersection(dylan)

alice_only = alice.difference(bob.union(charlie).union(dylan))
bob_only = bob.difference(alice.union(charlie).union(dylan))
charlie_only = charlie.difference(alice.union(bob).union(dylan))
dylan_only = dylan.difference(alice.union(bob).union(charlie))

all_game_achievements = set(ALL_ACHIEVEMENTS)

alice_missing = all_game_achievements.difference(alice)
bob_missing = all_game_achievements.difference(bob)
charlie_missing = all_game_achievements.difference(charlie)
dylan_missing = all_game_achievements.difference(dylan)

print("All distinct achievements:", all_distinct)
print("Common achievements:", common_achievements)

print("Only Alice has:", alice_only)
print("Only Bob has:", bob_only)
print("Only Charlie has:", charlie_only)
print("Only Dylan has:", dylan_only)

print("Alice is missing:", alice_missing)
print("Bob is missing:", bob_missing)
print("Charlie is missing:", charlie_missing)
print("Dylan is missing:", dylan_missing)
