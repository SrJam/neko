from anekos import NekosLifeClient, SFWImageTags
from asyncio import get_event_loop
import requests
from download import download
from set_wall import change

client = NekosLifeClient()

name = 'act_wallpaper.jpg'

async def main():
    result = await client.image(SFWImageTags.WALLPAPER)
    url = result.url
    download(url, name)
    change(name)
    
loop = get_event_loop()
loop.run_until_complete(main())