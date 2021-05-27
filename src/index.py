from workers.upload import upload
from workers.fetch_images import fetch

import sched, time

async def eventLoop():
    time.sleep(6000)
    eventLoop()

fetch()