
# Question-1
arr = [1, 2, 3, 4, 5]

arr.append(6)

print(arr)


# Question-2

arr = [1,2,3,4,5]

num_elements = int(input("How many elements do you want to add to the array? "))

for i in range(num_elements):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

print("The final array is:", arr)


# Question-3

import json

json_data = '''
{
  "date": "2023-02-20",
  "explanation": "This is the sample picture of Blackhole, which is residing in our galaxy.",
  "hdurl": "https://apod.nasa.gov/apod/image.jpg",
  "media_type": "image",
  "service_version": "v1",
  "title": "The Center of the Milky Way Galaxy",
  "url": "https://apod.nasa.gov/apod/image.jpg"
}
'''

data = json.loads(json_data)
print("Explanation:", data["explanation"])
print("Title:", data["title"])


# Question-4

import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


# Question-5

import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    timestamp = data["timestamp"]
    
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Timestamp:", timestamp)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


#Q6

import requests
import pandas as pd
import time

url = "http://api.open-notify.org/iss-now.json"

num_records = 100

timestamps = []
latitudes = []
longitudes = []

for _ in range(num_records):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        timestamp = data.get("timestamp")
        iss_position = data.get("iss_position", {})

        latitude = iss_position.get("latitude")
        longitude = iss_position.get("longitude")
        
        timestamps.append(timestamp)
        latitudes.append(latitude)
        longitudes.append(longitude)

        time.sleep(10)  
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        break

df = pd.DataFrame({
        "Timestamp": timestamps,
        "Latitude": latitudes,
        "Longitude": longitudes
})

df.to_csv("iss_location_data.csv", index=False)

print("Data has been written to iss_location_data.csv")