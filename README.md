# DBI Api

This API returns in a json format info about all the Bots in the Discord Server [Discord Bots Italia](https://www.discordbotsitalia.tk/join)

Check the [website](https://dbiapi.ssebastianoo.repl.co)

# GET

`https://dbiapi.ssebastianoo.repl.co/api`

# Examples 

- Python Requests

```
import requests

r = requests.get("https://dbiapi.ssebastianoo.repl.co/api").json()

return r["Emoji Locker#7965"]["status"]["name"]
```

- Python Aiohttp

```
import aiohttp

async with aiohttp.ClientSession() as a:

    r = await a.get("https://dbiapi.ssebastianoo.repl.co/api")
    
    b = await r.json()
    
return b["Teo#8099"]["avatar_url"]
```
