
import streamlit as st
import random

def get_rounds(num):
    rounds = []
    while num > 1:
        rounds.append(num)
        num //= 2
    rounds.append(2)
    return rounds

def generate_singles_fixtures(participants):
    st.subheader("Singles Fixtures")
    if participants < 2:
        st.write("Not enough participants for singles event.")
        return
    rounds = get_rounds(participants)
    for r in rounds:
        st.write(f"Round of {r}")

def generate_doubles_fixtures(participants):
    st.subheader("Doubles Fixtures")
    if participants % 2 != 0:
        st.write("Please only enter an even number as an odd number of participants cannot be accommodated into the doubles event format 😊")
        return
    teams = participants // 2
    st.write(f"Total Doubles Teams: {teams}")
    rounds = get_rounds(teams)
    for r in rounds:
        st.write(f"Round of {r}")

def generate_team_fixtures(participants):
    st.subheader("Team Fixtures")
    if participants % 3 != 0:
        st.write("Please only enter a number divisible by 3 as the total number of participants cannot be accommodated into the team events format 😊")
        return
    teams = participants // 3
    st.write(f"Total Teams: {teams}")
    rounds = get_rounds(teams)
    for r in rounds:
        st.write(f"Round of {r}")

st.title("AI Based Table Tennis Championship Fixtures Creator")
participants = st.number_input("How many participants will take part in the tournament?", min_value=1)
singles = st.number_input("How many participants will take part in the singles event?", min_value=0)
doubles = st.number_input("How many participants will take part in the doubles event?", min_value=0)
teams = st.number_input("How many participants will take part in the team events?", min_value=0)

if st.button("Generate Fixtures"):
    generate_singles_fixtures(singles)
    generate_doubles_fixtures(doubles)
    generate_team_fixtures(teams)
