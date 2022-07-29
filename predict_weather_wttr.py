import requests

def predict_weather():
  city = input('Please enter a city: ')
  url = (f'https://wttr.in/{city}')
  try:
    data = requests.get(url)
    T = data.text
  except:
    T = "Error Occurred"
  print(T)

def main():
  print("\t\tWelcome to this Weather Forecaster!\n\n")
  print("Just enter the city you want the weather report for and click Enter!\n\n")

  predict_weather()

if __name__ == "__main__":
  main()
