from timezonefinder import TimezoneFinder
from pytz import timezone
from datetime import datetime
from requests import get
from string import capwords
from bot.utils import embed_md
from config.config import load_config
from matrix.bot import Context


def get_api_key():
    cfg = load_config()

    return cfg["OPENWEATHER_APIKEY"]


def get_timezone(data: any) -> datetime:
    """Get the timezone for the given city.

    :param data: The weather data to get the timezone for.
    :type data: Any | None
    :return: The timezone based on Longitude and Latitude.
    :rtype: datetime.tzinfo
    """
    longitude = float(data["coord"]["lon"])
    latitude = float(data["coord"]["lat"])
    timezone_finder = TimezoneFinder()

    result = timezone_finder.timezone_at(lng=longitude, lat=latitude)
    return datetime.now(timezone(str(result)))


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert a temperature in Kelvin to Celsius.

    :param kelvin: The temperature in Kelvin.
    :type kelvin: float
    :return: The temperature in Celsius.
    :rtype: float
    """
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Convert a temperature in Kelvin to fahrenheit.

    :param kelvin: The temperature in Kelvin.
    :type kelvin: float
    :return: The temperature in fahrenheit.
    :rtype: float
    """
    return kelvin * 1.8 - 459.67


async def get_weather(city: str):
    """Retrieve weather information for the specified city.

    :param city: The name of the city to retrieve weather information for
    :type city: str
    :return: A dictionary containing the weather information, or None if the city was not found
    :rtype: dict
    """
    OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/"
    APIKEY = get_api_key()

    # complete_url to retreive weather info
    response = get(f"{OPENWEATHER_BASE_URL}/weather?appid={APIKEY}&q={city}")

    # code 200 means the city is found otherwise, city is not found
    if response.status_code == 200:
        return response.json()
    return None


async def weather(ctx: Context):
    """Display weather information for the specified city.

    :param ctx: the Discord context for the command
    :type ctx: Context
    :param city_input: The name of the city to display weather information for
    :type city_input: str
    :return: This function sends an embed message to the Discord channel
    """

    get_event = getattr(ctx.event, "body", "")
    get_city = get_event.find(" ")
    city_input = get_event[get_city + 1:]

    city = capwords(city_input)
    data_weather = await get_weather(city)
    timezone_city = get_timezone(data_weather)

    # Now data_weather contains lists of data
    # from the city inputer by the user
    if data_weather:
        main = data_weather["main"]
        visibility = data_weather["visibility"]
        current_temperature = main["temp"]

        fahrenheit = kelvin_to_fahrenheit(int(current_temperature))
        celsius = kelvin_to_celsius(int(current_temperature))

        feels_like = main["feels_like"]
        feels_like_fahrenheit = kelvin_to_fahrenheit(int(feels_like))
        feels_like_celsius = kelvin_to_celsius(int(feels_like))

        current_pressure = main["pressure"]
        current_humidity = main["humidity"]
        forcast = data_weather["weather"]
        weather_description = forcast[0]["description"]

        str_d = f"""
**Description**\n
{capwords(weather_description)}

**Visibility**\n
{visibility}m | {round(visibility * 3.280839895)}ft\n

**Temperature**\n
{round(fahrenheit, 2)}°F | {round(celsius, 2)}°C

**Feels Like**\n
{round(feels_like_fahrenheit, 2)}°F | {round(feels_like_celsius, 2)}°C

**Atmospheric Pressure**\n
{current_pressure} hPa

**Humidity**\n
{current_humidity}%
"""

        embed = embed_md.make_embed(
            title=city,
            description=timezone_city.strftime("%m/%d/%Y %H:%M"),
            field=str_d,
        )

    else:
        embed = embed_md.make_embed(description=f"{city} No Found!")
    await ctx.send(embed)
