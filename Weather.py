import python_weather
import asyncio

async def get_weather(city):
    try:
        async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
            weather = await client.get(city)
            return weather.current.temperature
    except Exception as e:
        return f"Error: {e}"

async def main():
    city = input("Enter the name of the City: ")
    temperature = await get_weather(city)
    print(f"Current temperature in {city}: {temperature}")

if __name__ == "__main__":
    asyncio.run(main())
