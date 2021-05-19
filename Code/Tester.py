# from time import time
# import discord
# import os
# from liquipediapy import dota
# from liquipediapy import liquipediapy
# from datetime import datetime
# import pytz
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas

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

string = "$table NA Upper"
additional = string.split("$table ")
region = additional[1].split(" ")[0]
division = additional[1].split(" ")[1]

eu_lower = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/Europe/Lower_Division"
cis_lower = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/CIS/Lower_Division"
na_lower = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/North_America/Lower_Division"
sa_lower = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/South_America/Lower_Division"
sea_lower = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/Southeast_Asia/Lower_Division"
cn_lower = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/China/Lower_Division"
eu_upper = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/Europe/Upper_Division"
cis_upper = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/CIS/Upper_Division"
na_upper = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/North_America/Upper_Division"
sa_upper = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/South_America/Upper_Division"
sea_upper = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/Southeast_Asia/Upper_Division"
cn_upper = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/1/China/Upper_Division"

if region == "NA":
    if division == "Upper":
        url = na_upper
    elif division == "Lower":
        url = na_lower
elif region == "SA":
    if division == "Upper":
        url = sa_upper
    elif division == "Lower":
        url = sa_lower
elif region == "EU":
    if division == "Upper":
        url = eu_upper
    elif division == "Lower":
        url = eu_lower
elif region == "SEA":
    if division == "Upper":
        url = sea_upper
    elif division == "Lower":
        url = sea_lower
elif region == "CIS":
    if division == "Upper":
        url = cis_upper
    elif division == "Lower":
        url = cis_lower
elif region == "CN":
    if division == "Upper":
        url = cn_upper
    elif division == "Lower":
        url = cn_lower        

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find("table",{"class":"wikitable wikitable-bordered grouptable"})
rows = table.findAll("tr",{"data-toggle-area-content":"6"})
#teams = table.findAll("td",{"class":"grouptableslot"})
ij=0
data = []

for ij in range(0,8):
    teams = rows[ij].find("td",{"class":"grouptableslot"})
    score = rows[ij].findAll("td",{"width":"35px"})
    scores = score[0].text + "\t\t" +score[1].text
    result = teams.text + "\t\t" + scores
    print(str(score[0].text)+"\n\n")
    data.append([ij+1, teams.text, score[0].text, score[1].text])

for ij in range(0,8):

    teams = rows[ij].find("td",{"class":"grouptableslot"})
    score = rows[ij].findAll("td",{"width":"35px"})
    scores = score[0].text + "\t\t" +score[1].text
    result = teams.text + "\t\t" + scores
    data.append([ij+1, teams.text, score[0].text, score[1].text])

headers=["Position", "Team", "Serires Score", "Map Score"]
end_table = tabulate(data, headers=["Position", "Team", "Series Score", "Map Score"])
print(end_table)
#print (tabulate(data, headers=["Position", "Team", "Serires Score", "Map Score"]))
"""
"""
url = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/Rankings"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.findAll("table",{"class":"wikitable"})[1]
rows = table.findAll("tr")
ij=0
data = []
for i in range(2,14):
    team = rows[i].find("span",{"class":"team-template-team-standard"}).text
    points = rows[i].findAll("td")[2].text
    data.append([ij+1, team, points])
    ij+=1
end_table = tabulate(data, headers=["Position", "Team", "Points"])
print(end_table)
"""
#print(rows[2])
#points = table.find("td")
#print(points)

"""
for ij in range(0,8):

    teams = team[ij].text
    score = rows[ij].findAll("td",{"width":"35px"})
    scores = score[0].text + "\t\t" +score[1].text
    result = teams.text + "\t\t" + scores
    data.append([ij+1, teams.text, score[0].text, score[1].text])
    #await message.channel.send(str(ij+1) + " " +team.text + " " + score[0].text + " " + score[1].text)
"""

from bs4 import BeautifulSoup
from tabulate import tabulate
import requests
url = "https://liquipedia.net/dota2/Dota_Pro_Circuit/2021/Rankings"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.findAll("table",{"class":"wikitable"})[1]
rows = table.findAll("tr")
ij=0
data = []
for i in range(2,20):
    team = rows[i].find("span",{"class":"team-template-team-standard"}).text
    points = rows[i].findAll("td")[2].text
    if points.find("P")>0:
        pos = points.index("P")
        points = points[:pos]
    print(points)