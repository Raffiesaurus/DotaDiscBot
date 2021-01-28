# from time import time
# import discord
# import os
# from liquipediapy import dota
# from liquipediapy import liquipediapy
# from datetime import datetime
# import pytz
"""
liquipy_object = liquipediapy('Dota Match Schedule Timer Discord Bot (rafs1800@outlook.com)', 'dota2')
today = datetime.now(pytz.utc)
teamname = "TNC"
soup,url = liquipy_object.parse(teamname)

all_matches = soup.findAll("table",{"class":"wikitable wikitable-striped infobox_matches_content"})
match1 = all_matches[0]
match2 = all_matches[1]
left_team = match1.find("td",{"class":"team-left"})
left_team1 = left_team.find("span",{"class":"team-template-team2-short"})
left_team2 = left_team1.find("span",{"class":"team-template-text"})
left_team_name = left_team2.text
right_team = match1.find("td",{"class":"team-right"})   
right_team1 = right_team.find("span",{"class":"team-template-team-short"})
right_team2 = right_team1.find("span",{"class":"team-template-text"})
right_team_name = right_team2.text
left2_team = match2.find("td",{"class":"team-left"})
left2_team1 = left2_team.find("span",{"class":"team-template-team2-short"})
left2_team2 = left2_team1.find("span",{"class":"team-template-text"})
left2_team_name = left2_team2.text
right2_team = match2.find("td",{"class":"team-right"})   
right2_team1 = right2_team.find("span",{"class":"team-template-team-short"})
right2_team2 = right2_team1.find("span",{"class":"team-template-text"})
right2_team_name = right2_team2.text

if left_team_name.lower() == left2_team_name.lower():
    teamname2 = left_team_name
elif left_team_name.lower() == right2_team_name.lower():
    teamname2 = left_team_name
elif right_team_name.lower() == right2_team_name.lower():
    teamname2 = right_team_name
elif right_team_name.lower() == left2_team_name.lower():
    teamname2 = right_team_name
        
if left_team_name.lower() == teamname2.lower():
    ateamname = right_team_name
else:
    ateamname = left_team_name

match = soup.find("span",{"class":"timer-object timer-object-countdown-only"})
match = match.text
match = match.split(" UTC")[0]

datetime_object = datetime.strptime(match, '%B %d, %Y - %H:%M')
datetime_object = datetime.strftime(datetime_object,"%B %d %Y %H:%M:%S")
datetime_object = datetime.strptime(datetime_object, '%B %d %Y %H:%M:%S')

today = datetime.strftime(today,"%B %d %Y %H:%M:%S")
today = datetime.strptime(today,"%B %d %Y %H:%M:%S")
time_till_match = datetime_object - today
time_till_match = str(time_till_match)
text_to_print = "Next Match for "+teamname+" is against "+ateamname+" on: "+str(datetime_object)+" UTC.\n"+"Time till match: "+str(time_till_match)
print(text_to_print)
"""

# string1 = "$nm Liquid"
# string2 = string1.split("$nm ")
# if len(string1.split("$nm "))==1:
#     print(string2)
# else:
#     print(len(string2))

# dota_obj = dota("Dota Match Schedule Timer Discord Bot (rafs1800@outlook.com)")
# games = dota_obj.get_upcoming_and_ongoing_games()
# #print(games[0])

# teamname = games[0]['team1']
# ateamname = games[0]['team2']

# today = datetime.now(pytz.utc)
# match = games[0]['start_time']
# match = match.split(" UTC")[0]

# datetime_object = datetime.strptime(match, '%B %d, %Y - %H:%M')
# datetime_object = datetime.strftime(datetime_object,"%B %d %Y %H:%M:%S")
# datetime_object = datetime.strptime(datetime_object, '%B %d %Y %H:%M:%S')

# today = datetime.strftime(today,"%B %d %Y %H:%M:%S")
# today = datetime.strptime(today,"%B %d %Y %H:%M:%S")
# time_till_match = datetime_object - today
# time_till_match = str(time_till_match)

# if time_till_match[0] == '-':
#     text_to_print = "Ongoing Match is "+teamname+" vs "+ateamname+". Tournament: "+games[0]['tournament']
#     print(text_to_print)
# else:
#     text_to_print = "Upcoming Match is "+teamname+" vs "+ateamname+". Tournament: "+games[0]['tournament']+"\nTime till match: "+str(time_till_match)
#     print(text_to_print)

string = "$nm "
additional = string.split("$nm ")
print(len(additional))