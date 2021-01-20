from time import time
import discord
import os
from liquipediapy import dota
from liquipediapy import liquipediapy
from datetime import datetime
import pytz

client = discord.Client()
dota_obj = dota("Dota Match Timer Discord Bot (rafs1800@outlook.com)")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$nm'):
        liquipy_object = liquipediapy('Dota Match Schedule Timer Discord Bot (rafs1800@outlook.com)', 'dota2')
        today = datetime.now(pytz.utc)
        teamname = message.content.split("$nm ")[1]
        soup,url = liquipy_object.parse(teamname)
        match1 = soup.find("table",{"class":"wikitable wikitable-striped infobox_matches_content"})
        left_team = match1.find("td",{"class":"team-left"})
        left_team1 = left_team.find("span",{"class":"team-template-team2-short"})
        left_team2 = left_team1.find("span",{"class":"team-template-text"})
        left_team_name = left_team2.text
        right_team = match1.find("td",{"class":"team-right"})   
        right_team1 = right_team.find("span",{"class":"team-template-team-short"})
        right_team2 = right_team1.find("span",{"class":"team-template-text"})
        right_team_name = right_team2.text

        if left_team_name.lower() == teamname.lower():
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
        await message.channel.send(text_to_print)
        
client.run(os.getenv("DISCORD_BOT_TOKEN"))