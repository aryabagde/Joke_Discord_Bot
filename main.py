# Since this BOT will stop working as soon as we close the window 
# For that we need to create a replit web server(which will enter in sleeping mode after an hour of last request)
# For that we need uptime robot which will keep pinging the replit web server
import discord;
import os;
import requests;
import json;
import random;
from alive import alive
from replit import db


client = discord.Client() # discord.py library
# asynchronus library discord.py

db["sad_words"] = ["sad", "depressed", "unhappy", "angry", "depressing", "miserable"]    # words that user will say

db["starter_jokes"] = ["Chalna mc", "Hatt bc", "Get it together Bitch", "Fuck offf bitch","Share it with your bf/gf, Ohh u don't have one that's why you are sharing with me XD"]  #words that bot will say

def get_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
  json_data = json.loads(response.text)
  joke = json_data["joke"]
  return joke

@client.event            # registering that event
async def on_ready():    # this event will be called when bot is ready to use
  print("We have logged in as {0.user}".format(client)) # we will print when the bot is ready
  # 0 will be replaced by client(client name)
@client.event
async def on_message(message):  # defined method in discord.py library * this method will be triggered each time a message is received *
  if message.author == client.user:  # We don't want to do anything when the message is from bot
    return 

  msg = message.content

  if msg.startswith('#joke'):
    joke = get_joke();
    await message.channel.send(joke)   # message will be sent that to the channel

  if any(word in msg for word in db["sad_words"]):
    await message.channel.send(random.choice(db["starter_jokes"]))

my_secret = os.environ['TOKEN'] # .env file i which the TOKEN consists of token

alive()
client.run(my_secret)  # Run the bot