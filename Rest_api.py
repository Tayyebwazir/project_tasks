# Task no 4:
# I select openweathermap 
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Enter your API key here
api_key = "79c13298cc3f3baaad9c6d6ced84809a"

# Sir this is url for openweathermap 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Function to get weather data and convert to DataFrame
def get_weather_data(city_name):
    # Complete URL variable to store complete URL address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
   
    response = requests.get(complete_url)
    
    
    data = response.json()
    
    # Check if city is found
    if data.get("cod") == 200:  
        y = data["main"]
        z = data["weather"]
        
        # Store values in a dictionary
        weather_data = {
            'City': city_name,
            'Temperature (K)': y.get("temp"),
            'Pressure (hPa)': y.get("pressure"),
            'Humidity (%)': y.get("humidity"),
            'Weather Description': z[0].get("description") if z else "No description"
        }
        
        # Convert to DataFrame
        df = pd.DataFrame([weather_data])
        return df
    else:
        print(f"City Not Found: {data.get('message')}")
        return None


city_name = input("Enter city name: ")
df = get_weather_data(city_name)

if df is not None:
    
    df['Temperature (C)'] = df['Temperature (K)'] - 273.15  # Convert to Celsius

    # Static Visualization using matplotlib and seaborn
    sns.barplot(data=df, x='City', y='Temperature (C)')
    plt.title('Temperature in Celsius')
    plt.show()

    sns.barplot(data=df, x='City', y='Humidity (%)')
    plt.title('Humidity Percentage')
    plt.show()

   
    fig = px.bar(df, x='City', y='Temperature (C)', title='Temperature in Celsius')
    fig.show()

    fig = px.bar(df, x='City', y='Humidity (%)', title='Humidity Percentage')
    fig.show()










