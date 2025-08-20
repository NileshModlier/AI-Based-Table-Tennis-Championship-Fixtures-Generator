
import random

def get_rounds(num):
    rounds = []
    while num > 1:
        rounds.append(num)
        num //= 2
    rounds.append(2)
    return rounds

def generate_singles_fixtures(participants):
    print("
Singles Fixtures:")
    if participants < 2:
        print("Not enough participants for singles event.")
        return
    rounds = get_rounds(participants)
    for r in rounds:
        print(f"Round of {r}")

def generate_doubles_fixtures(participants):
    print("
Doubles Fixtures:")
    if participants % 2 != 0:
        print("Please only enter an even number as an odd number of participants cannot be accommodated into the doubles event format 😊")
        return
    teams = participants // 2
    print(f"Total Doubles Teams: {teams}")
    rounds = get_rounds(teams)
    for r in rounds:
        print(f"Round of {r}")

def generate_team_fixtures(participants):
    print("
Team Fixtures:")
    if participants % 3 != 0:
        print("Please only enter a number divisible by 3 as the total number of participants cannot be accommodated into the team events format 😊")
        return
    teams = participants // 3
    print(f"Total Teams: {teams}")
    rounds = get_rounds(teams)
    for r in rounds:
        print(f"Round of {r}")

# User Input
participants = int(input("How many participants will take part in the tournament? "))
singles = int(input("How many participants will take part in the singles event? "))
doubles = int(input("How many participants will take part in the doubles event? "))
teams = int(input("How many participants will take part in the team events? "))

# Generate Fixtures
generate_singles_fixtures(singles)
generate_doubles_fixtures(doubles)
generate_team_fixtures(teams)
