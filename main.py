import discord
from discord.ext import tasks
import os
import json
from server import keep_alive
import datetime

client = discord.Client()

@client.event
async def on_ready():

  print("Bot ready as", client.user)
  bots.start()

@tasks.loop(seconds = 5)
async def bots():

  with open("data/bots.json", "r") as f:

    l = json.load(f)

  guild = client.get_guild(611322575674671107)

  for a in guild.members:

    if a.bot:

      if a.activity:

        activity_name = a.activity.name
        activity_type = a.activity.type

      else:

        activity_name = "No Activity"
        activity_type = "No Activity"

      l[str(a)] = {"username": str(a), "name": str(a.name), "id": a.id, "avatar_url": str(a.avatar_url), "activity": {"name": str(activity_name), "type": str(activity_type)}, "status": str(a.status)}

  with open("data/bots.json", "w") as f:

    json.dump(l, f, indent = 4)

  with open("data/logs.txt", "a") as f:

    f.write(f"\n[{datetime.datetime.now().strftime('%d %B %Y [%I:%M:%S %p]')}] - Updated bots.json")

keep_alive()
client.run(os.environ.get("token"))