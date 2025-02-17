#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:02:26 2021

@author: admin
"""

#Declaire variable for list of gamers
gamers = [] 

#Function for adding new gamers to the list
def add_gamer(gamer, gamers_list):
    if (gamer.get("name") != None) and (gamer.get("availability") != None):
        gamers_list.append(gamer)        
    
#Add new gamers
kimberly = {'name': 'Kimberly Warner', 'availability': ['Monday', 'Tuesday', 'Friday']}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
print(gamers)

#Function for frequency table
def build_daily_frequency_table():
    return {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
count_availability = build_daily_frequency_table()

#Function for updating frequency table
def calculate_availability(gamers_list, available_frequency):
    for day in available_frequency:
        for gamer in gamers_list:
            if day in gamer.get('availability'):
                available_frequency[day] += 1
    return available_frequency
#print(calculate_availability(gamers, count_availability))

#Function for finding the best night
def find_best_night(availability_table):
    best_day = 'Monday'
    for day in availability_table:
        if availability_table.get(day) > availability_table.get(best_day):
            best_day = day
    return best_day
game_night = find_best_night(count_availability)
#print(game_night)

#Function for printing the list of available gamers on the best night
def available_on_night(gamers_list, day):
    available_gamers = []
    for gamer in gamers_list:
        if day in gamer.get('availability'):
            available_gamers.append(gamer.get('name'))
    return available_gamers
attending_game_night = available_on_night(gamers, game_night)
#print(attending_game_night)

#Email form for gamers
form_email = """
Dear {name},

The Sorcery Society is delighted to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
Your Majesty
"""

#Function for generating emails
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer, day_of_week=day, game=game))
        
send_email(attending_game_night, game_night, "Abruptly Goblins!")

#Function for finding the second night
def another_night_gamers(gamers_list, day):
    another_gamers = []
    for gamer in gamers_list:
        if day not in gamer.get('availability'):
             another_gamers.append(gamer)
    return another_gamers

unable_to_attend_best_night = another_night_gamers(gamers, game_night)
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
#print(second_night)
#print(second_night_availability)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")