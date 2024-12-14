pip install nest_asyncio

pip install aiohttp

import aiohttp
import asyncio

async def fetch_data_from_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Example API endpoint
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()  # Return the JSON response
            else:
                return {"error": f"Failed to fetch data. Status code: {response.status}"}

# Use this in environments with an active event loop
async def main():
    data = await fetch_data_from_api()
    print(data)

# Run the main function
import nest_asyncio
nest_asyncio.apply()  # To allow nested event loops in Jupyter
await main()




# --------------------------------------------




import asyncio

async def async_add(a, b):
    await asyncio.sleep(1)  # Simulate asynchronous work
    return a + b

async def main():
    result = await async_add(2, 3)
    print(result)

asyncio.run(main())  # Output: 5
