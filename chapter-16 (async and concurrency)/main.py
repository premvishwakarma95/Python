# Your first async function
# Python provides a standard-library module called asyncio.
import asyncio

async def greet():
    print("Hello Prem")
    await asyncio.sleep(2)
    print("Welcome to async Python")

asyncio.run(greet())



# Run operations concurrently with "gather()"
import asyncio
import time

async def fetch_carrier(carrier_id):
    print(f"Fetching carrier {carrier_id}")

    await asyncio.sleep(2)

    print(f"Finished carrier {carrier_id}")
    return {"id": carrier_id}

async def main():
    start = time.perf_counter()

    carriers = await asyncio.gather(
        fetch_carrier(1),
        fetch_carrier(2),
        fetch_carrier(3),
    )

    print(carriers)
    print(f"Time: {time.perf_counter() - start:.2f} seconds")

asyncio.run(main())