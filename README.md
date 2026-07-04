# Weather_App
A Python-based Weather App that fetches real-time weather information using a weather API. Users can search for any city and instantly view current weather conditions, temperature, humidity, wind speed, and more through a simple and user-friendly interface.
# 🌦️ Weather App

A simple and efficient Python Weather App that fetches real-time weather information using a weather API. Enter the name of any city to get the latest weather details, including temperature, humidity, wind speed, and weather conditions.

---

## 📌 Features

- 🌍 Search weather by city name
- 🌡️ Real-time temperature
- ☁️ Weather description
- 💧 Humidity information
- 💨 Wind speed
- 🌅 Sunrise and sunset timings
- 📅 Date and time display
- ❌ Handles invalid city names gracefully
- 🔄 Fetches live data using a Weather API

---

## 🛠️ Built With

- Python 3
- Requests Library
- JSON
- OpenWeather API (or WeatherAPI)
- Datetime Module

---

## 📂 Project Structure

```
Weather_App/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Weather_App.git
```

### 2. Open the project folder

```bash
cd Weather_App
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Open `config.py` and add your API key.

```python
API_KEY = "YOUR_API_KEY"
```

### 5. Run the application

```bash
python main.py
```

---

## 📷 Sample Output

```
====================================
        WEATHER REPORT
====================================

City        : Mumbai
Temperature : 30°C
Condition   : Clear Sky
Humidity    : 75%
Wind Speed  : 12 km/h
Sunrise     : 06:10 AM
Sunset      : 07:18 PM

====================================
```

---

## 📚 What I Learned

- Working with REST APIs
- Sending HTTP requests using Python
- Parsing JSON data
- Exception handling
- Modular programming
- Building real-world Python applications

---

## 🚀 Future Improvements

- 7-Day Weather Forecast
- Hourly Weather Updates
- GUI Version using Tkinter
- CustomTkinter Interface
- Weather Icons
- Dark/Light Mode
- Search History
- GPS Location Support
- Temperature Unit Conversion (°C/°F)
- Weather Alerts

---

## 📦 Requirements

Install all required libraries using:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`

```
requests
```

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push to your branch
6. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Krupali**

If you found this project helpful, consider giving it a ⭐ on GitHub!
