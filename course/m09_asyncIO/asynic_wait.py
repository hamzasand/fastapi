# Lecture 9.2 - async / await / coroutines  (still ~3 seconds!)
import asyncio
import time

# "async def" -> a COROUTINE function. Calling it does NOT run it.
async def endpoint(route: str) -> str:
    print(f">> handling {route}")

    # asyncio.sleep is the async twin of time.sleep -> it must be awaited
    await asyncio.sleep(1)

    print(f"<< response {route}")
    return route

async def server():
    tests = (
        "GET /product?id=1001",
        "PATCH /product?id=1004",
        "GET /product?id=1003",
    )

    start = time.perf_counter()

    for route in tests:
        result = await endpoint(route)
        print("Result:", result)

    end = time.perf_counter()
    print(f"Time taken: { end - start:.2f} seconds")

asyncio.run(server())