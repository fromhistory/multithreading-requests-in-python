import requests
from datetime import datetime
import threading
import time

WEBSITE = "https://ifconfig.co/json"

# Create a list of timestamps

timestamps = ["09:15:25", "11:58:23", "13:45:09", "13:45:09", "13:45:09", "17:22:00", "17:22:00", "21:08:00"]


# Convert timestamps to a dictionary in order to know the frequency of identical timestamps

dictionary_of_timestamps = {item: timestamps.count(item) for item in timestamps}

# Function to make an API request


def response_api():
    """
    Sends an API request to a designated website
    :return: prints JSON-format data retrieved from the website
    """
    response = requests.get(url=WEBSITE)
    data = response.json()
    print(data)

# Measures time now on the local machine
# Checks if time now is in the dictionary of timestamps
# Makes an API request(s) as many times as the number of identical timestamps in the dictionary
# Uses multi-threading for concurrent API requests


while True:
    time.sleep(1)
    time_now = str(datetime.now().time().replace(microsecond=0))
    if time_now in dictionary_of_timestamps.keys():

        threads = []

        for _ in range(dictionary_of_timestamps[time_now]):
            t = threading.Thread(target=response_api)
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()



