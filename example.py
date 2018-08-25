"""
Copyright (c) 2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import asyncio

import aiohttp

from volkszaehler import Volkszaehler

HOST = 'demo.volkszaehler.org'
UUID = '57acbef0-88a9-11e4-934f-6b0f9ecd95a8'


async def main():
    """The main part of the example script."""
    async with aiohttp.ClientSession() as session:
        zaehler = Volkszaehler(loop, session, UUID, host=HOST)

        # Get the data
        await zaehler.get_data()

        print("Average:", zaehler.average)
        print("Max:", zaehler.max)
        print("Min:", zaehler.min)
        print("Consumption:", zaehler.consumption)
        print("Data tuples:", zaehler.tuples)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())