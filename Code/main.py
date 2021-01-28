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
        additional = message.content.split("$nm ")[1]

        if not additional.isnumeric():
            teamname = additional
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
            if time_till_match[0] == '-':
                text_to_print = "Match for "+teamname+" against "+ateamname+" is ongoing!"
            else:
                text_to_print = "Next Match for "+teamname+" is against "+ateamname+" on: "+str(datetime_object)+" UTC.\n"+"Time till match: "+str(time_till_match)
            await message.channel.send(text_to_print)
        
        elif additional.isnumeric():
            number = int(additional)
            ongoing_list=[]
            upcoming_list=[]
            dota_obj = dota("Dota Match Schedule Timer Discord Bot (rafs1800@outlook.com)")
            games = dota_obj.get_upcoming_and_ongoing_games()
            for i in range(0, number):
                teamname = games[i]['team1']
                ateamname = games[i]['team2']

                today = datetime.now(pytz.utc)
                match = games[i]['start_time']
                match = match.split(" UTC")[0]

                datetime_object = datetime.strptime(match, '%B %d, %Y - %H:%M')
                datetime_object = datetime.strftime(datetime_object,"%B %d %Y %H:%M:%S")
                datetime_object = datetime.strptime(datetime_object, '%B %d %Y %H:%M:%S')

                today = datetime.strftime(today,"%B %d %Y %H:%M:%S")
                today = datetime.strptime(today,"%B %d %Y %H:%M:%S")
                time_till_match = datetime_object - today
                time_till_match = str(time_till_match)

                if time_till_match[0] == '-':
                    ongoing_list.append(teamname+" vs "+ateamname+". Tournament: "+games[i]['tournament'])                
                else:
                    upcoming_list.append(teamname+" vs "+ateamname+". Tournament: "+games[i]['tournament']+"\nTime till match: "+str(time_till_match))
            if len(ongoing_list) > 0:
                await message.channel.send("**Ongoing Matches:**")               
                for text_to_print in ongoing_list:
                    await message.channel.send(text_to_print)
            if len(upcoming_list) > 0:
                await message.channel.send("\n**Upcoming Matches:**")
                for text_to_print in upcoming_list:
                    await message.channel.send(text_to_print)

    
    if message.content.startswith('$help'):
        text_to_print = "**Commands:**\n$nm [Number]- Returns the requested number of ongoing/next match to be played according to Liquipedia.\n$nm [Team Name] - Returns the upcoming match and time for the requested team.\n$help - Gives list of commands."
        await message.channel.send(text_to_print)


client.run(os.getenv("DISCORD_BOT_TOKEN"))