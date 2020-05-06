# DBI Api

This API returns in a json format info about all the Bots in the Discord Server [Discord Bots Italia](https://www.discordbotsitalia.tk/join)

Check the [website](https://api.dbi.seba.gq)

# GET

`https://api.dbi.seba.gq/api`

# Examples 

- Python Requests

```
import requests

r = requests.get("https://api.dbi.seba.gq/api").json()

return r["609087387695316992"]["status"]["name"]
```

- Python Aiohttp

```
import aiohttp

async with aiohttp.ClientSession() as a:

    r = await a.get("https://api.dbi.seba.gq/api")
    
    b = await r.json()
    
return b["607040796780134422"]["avatar_url"]
```
