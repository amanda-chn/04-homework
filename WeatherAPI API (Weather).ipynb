{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# WeatherAPI (Weather)\n",
    "\n",
    "Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.\n",
    "\n",
    "Be sure to take advantage of both the documentation and the API Explorer!\n",
    "\n",
    "## 0) Import any libraries you might need\n",
    "\n",
    "- *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*\n",
    "- *Tip: Remember you only need to import requests once!*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).\n",
    "\n",
    "- *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*\n",
    "- *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*\n",
    "- *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*\n",
    "- *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* \n",
    "- *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "marrakesh_url = \"http://api.weatherapi.com/v1/current.json?key=712a676012bf49fbbe9183818221506 &q=marrakesh&aqi=no\"\n",
    "marrakesh_response = requests.get(marrakesh_url)\n",
    "marrakesh_data = marrakesh_response.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#marrakesh_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2) What's the current wind speed? How much warmer does it feel than it actually is?\n",
    "\n",
    "- *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*\n",
    "- *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#marrakesh_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The current wind speed in Marrakesh is 14.3.\n"
     ]
    }
   ],
   "source": [
    "wind_speed = marrakesh_data['current']['gust_mph']\n",
    "print(f'The current wind speed in Marrakesh is {wind_speed}.')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Right now it feels 2.0F warmer than it actually is in Marrakesh.\n"
     ]
    }
   ],
   "source": [
    "current_temp = marrakesh_data['current']['temp_f']\n",
    "feels_temp = marrakesh_data['current']['feelslike_f']\n",
    "difference_temp = feels_temp - current_temp\n",
    "\n",
    "print(f'Right now it feels {difference_temp:.2}F warmer than it actually is in Marrakesh.')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?\n",
    "\n",
    "- *Tip: Check the documentation!*\n",
    "- *Tip: If you aren't sure what something means, ask in Slack*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "marrakesh_moon_url = \"http://api.weatherapi.com/v1/astronomy.json?key=712a676012bf49fbbe9183818221506 &q=marrakesh&dt=2022-06-16\"\n",
    "marrakesh_moon_response = requests.get(marrakesh_moon_url)\n",
    "marrakesh_moon_data = marrakesh_moon_response.json()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#marrakesh_moon_data['astronomy']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'location': {'name': 'Marrakesh',\n",
       "  'region': '',\n",
       "  'country': 'Morocco',\n",
       "  'lat': 31.63,\n",
       "  'lon': -8.0,\n",
       "  'tz_id': 'Africa/Casablanca',\n",
       "  'localtime_epoch': 1655325121,\n",
       "  'localtime': '2022-06-15 21:32'},\n",
       " 'astronomy': {'astro': {'sunrise': '06:26 AM',\n",
       "   'sunset': '08:39 PM',\n",
       "   'moonrise': '11:13 PM',\n",
       "   'moonset': '08:16 AM',\n",
       "   'moon_phase': 'Full Moon',\n",
       "   'moon_illumination': '86'}}}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "marrakesh_moon_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There will be a Full Moon tommorrow in Marrakesh.\n"
     ]
    }
   ],
   "source": [
    "moon_visibility = marrakesh_moon_data['astronomy']['astro']['moon_phase']\n",
    "print(f'There will be a {moon_visibility} tommorrow in Marrakesh.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4) What's the difference between the high and low temperatures for today?\n",
    "\n",
    "- *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "forecast_today_url = \"http://api.weatherapi.com/v1/forecast.json?key=712a676012bf49fbbe9183818221506&q=Marrakesh&days=1&aqi=no&alerts=no\"\n",
    "forecast_today_response = requests.get(forecast_today_url)\n",
    "forecast_today_data = forecast_today_response.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['location', 'current', 'forecast'])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forecast_today_data.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Today the low temp is 73.2F and the high temp is 101.3F.\n"
     ]
    }
   ],
   "source": [
    "forecastday_list = forecast_today_data['forecast']['forecastday']\n",
    "\n",
    "for forecast in forecastday_list:\n",
    "    min_temp = forecast['day']['mintemp_f']\n",
    "    max_temp = forecast['day']['maxtemp_f']\n",
    "    print(f'Today the low temp is {min_temp}F and the high temp is {max_temp}F.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## 4.5) How can you avoid the \"oh no I don't have the data any more because I made another request\" problem in the future?\n",
    "\n",
    "What variable(s) do you have to rename, and what would you rename them?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "rename:\n",
    "url, response, and the data file name"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.\n",
    "\n",
    "I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).\n",
    "\n",
    "- *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "forecast_url = \"http://api.weatherapi.com/v1/forecast.json?key=712a676012bf49fbbe9183818221506&q=Marrakesh&days=3&aqi=no&alerts=no\"\n",
    "forecast_response = requests.get(forecast_url)\n",
    "forecast_data = forecast_response.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "forecast_list = forecast_data['forecast']['forecastday']\n",
    "#print(forecast_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "On 2022-06-15 the max temp is 101.3F.\n",
      "On 2022-06-16 the max temp is 99.7F.\n",
      "On 2022-06-17 the max temp is 108.5F.\n"
     ]
    }
   ],
   "source": [
    "for forecast in forecast_list:\n",
    "    forecast_date = forecast['date']\n",
    "    forecast_high_temps = forecast['day']['maxtemp_f']\n",
    "    print(f'On {forecast_date} the max temp is {forecast_high_temps}F.')\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.\n",
    "\n",
    "What happens? Can you figure out why it doesn't work?\n",
    "\n",
    "* *Tip: it has to do with the reason you're using an API key - maybe take a look at the \"Air Quality Data\" introduction for a hint? If you can't figure it out right now, no worries.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "forecast_week_url = \"http://api.weatherapi.com/v1/forecast.json?key=712a676012bf49fbbe9183818221506&q=Marrakesh&days=7&aqi=no&alerts=no\"\n",
    "forecast_week_response = requests.get(forecast_week_url)\n",
    "forecast_week_data = forecast_week_response.json()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "forecast_week_list = forecast_week_data['forecast']['forecastday']\n",
    "#print(forecast_week_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "On 2022-06-15 the max temp is 101.3F.\n",
      "On 2022-06-16 the max temp is 99.7F.\n",
      "On 2022-06-17 the max temp is 108.5F.\n"
     ]
    }
   ],
   "source": [
    "for forecast_week in forecast_week_list:\n",
    "    forecast_week_date = forecast_week['date']\n",
    "    forecast_week_high_temps = forecast_week['day']['maxtemp_f']\n",
    "    print(f'On {forecast_week_date} the max temp is {forecast_week_high_temps}F.')\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The API ony returns the first three days of the forecast... Is it because our current subscription with this API only gives us max 3 day forecast??"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6) What will be the hottest day in the next three days? What is the high temperature on that day?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The hottest forecasted day is 2022-06-17 with a temp of 108.5.\n"
     ]
    }
   ],
   "source": [
    "hottest_day = forecast_list[-1]['date']\n",
    "hottest_temp = forecast_list[-1]['day']['maxtemp_f']\n",
    "\n",
    "for max in forecast_list:\n",
    "    if max['day']['maxtemp_f'] > hottest_temp:\n",
    "        hottest_day = max['day']['maxtemp_f']\n",
    "        hottest_temp = max['date']\n",
    "print(f'The hottest forecasted day is {hottest_day} with a temp of {hottest_temp}.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?\n",
    "\n",
    "I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say \"{temperature} and cloudy\" instead of just the temperature. \n",
    "\n",
    "- *Tip: You'll only need one day of forecast*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "miami_forecast_url = \"http://api.weatherapi.com/v1/forecast.json?key=712a676012bf49fbbe9183818221506&q=Miami&days=1&aqi=no&alerts=no\"\n",
    "miami_forecast_response = requests.get(miami_forecast_url)\n",
    "miami_forecast_data = miami_forecast_response.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "#miami_forecast_data['forecast']['forecastday'][0]['hour'][0]['cloud']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "miami_forecast_list = miami_forecast_data['forecast']['forecastday']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "In Miami, it will be 84.2F at 2022-06-15 00:00.\n",
      "In Miami, it will be 84.0F at 2022-06-15 01:00.\n",
      "In Miami, it will be 84.0F at 2022-06-15 02:00.\n",
      "In Miami, it will be 83.8F at 2022-06-15 03:00.\n",
      "In Miami, it will be 83.8F at 2022-06-15 04:00.\n",
      "In Miami, it will be 83.5F at 2022-06-15 05:00 and cloudy.\n",
      "In Miami, it will be 83.5F at 2022-06-15 06:00 and cloudy.\n",
      "In Miami, it will be 83.5F at 2022-06-15 07:00 and cloudy.\n",
      "In Miami, it will be 83.7F at 2022-06-15 08:00.\n",
      "In Miami, it will be 84.2F at 2022-06-15 09:00.\n",
      "In Miami, it will be 84.7F at 2022-06-15 10:00.\n",
      "In Miami, it will be 90.7F at 2022-06-15 11:00.\n",
      "In Miami, it will be 91.0F at 2022-06-15 12:00.\n",
      "In Miami, it will be 91.2F at 2022-06-15 13:00.\n",
      "In Miami, it will be 91.4F at 2022-06-15 14:00.\n",
      "In Miami, it will be 91.4F at 2022-06-15 15:00.\n",
      "In Miami, it will be 90.7F at 2022-06-15 16:00.\n",
      "In Miami, it will be 89.4F at 2022-06-15 17:00.\n",
      "In Miami, it will be 87.8F at 2022-06-15 18:00.\n",
      "In Miami, it will be 86.2F at 2022-06-15 19:00.\n",
      "In Miami, it will be 84.9F at 2022-06-15 20:00.\n",
      "In Miami, it will be 84.9F at 2022-06-15 21:00.\n",
      "In Miami, it will be 84.7F at 2022-06-15 22:00.\n",
      "In Miami, it will be 84.6F at 2022-06-15 23:00.\n"
     ]
    }
   ],
   "source": [
    "for miami in miami_forecast_list:\n",
    "    miami_time = miami['hour']\n",
    "    for miami_by_hour in miami_time:\n",
    "        hours = miami_by_hour['time']\n",
    "        temp_by_hour = miami_by_hour['temp_f']  \n",
    "        miami_cloud_coverage = miami_by_hour['cloud']\n",
    "        if miami_cloud_coverage > 50:\n",
    "             print(f'In Miami, it will be {temp_by_hour}F at {hours} and cloudy.')\n",
    "        else:\n",
    "            print(f'In Miami, it will be {temp_by_hour}F at {hours}.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?\n",
    "\n",
    "- *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "In Miami, it will be above 85F for 37.5% of the time.\n"
     ]
    }
   ],
   "source": [
    "high_temp_count = 0\n",
    "temp_count = 0\n",
    "\n",
    "for miami in miami_forecast_list:\n",
    "    miami_time = miami['hour']\n",
    "    for miami_by_hour in miami_time:\n",
    "        temp_by_hour = miami_by_hour['temp_f']\n",
    "        temp_count = temp_count + 1\n",
    "        if temp_by_hour > 85:\n",
    "            high_temp_count = high_temp_count + 1\n",
    "            \n",
    "high_temp_percentage = (high_temp_count/temp_count)*100\n",
    "print(f'In Miami, it will be above 85F for {high_temp_percentage}% of the time.')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9) How much will it cost if you need to use 1,500,000 API calls?\n",
    "\n",
    "You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. \n",
    "\n",
    "* *Tip: this involves looking somewhere that isn't the normal documentation.*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you need 1.5 million calls, you'd have the get the developer plan which is $4/mo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 10) You're too poor to spend more money! What else could you do instead of give them money?\n",
    "\n",
    "* *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Can you use a diff API key???"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
