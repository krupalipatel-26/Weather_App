import requests

API_KEY = "583341bcb55f37fa1d3586387a20adf3"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)

    data = response.json()
    print("Status Code:", response.status_code)
    print(data)

    if response.status_code == 200:

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print("\n===== Weather Report =====")
        print(f"City: {city_name}, {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather}")

    else:
        print("City not found!")

except Exception as e:
    print("Error:", e)