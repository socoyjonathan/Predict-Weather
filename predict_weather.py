pip install requests
pip install beautifulsoup4

from bs4 import BeautifulSoup #module designed to make screen-scraping done quickly
import requests #module helps integrate Python programs with web services

def predict_weather():
  city = input('Please enter a city: ')

  url = (f'https://www.google.com/search?q=weather{city}')
  res = requests.get(url).content
  soup = BeautifulSoup(res, 'html.parser')

  temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
  str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

  data = str.split('\n')
  time = data[0]
  sky = data[1]

  listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
  strd = listdiv[5].text
  print(strd)

  print("Temperature is", temp)
  print("Time: ", time)
  print("Sky Description: ", sky)

def main():
  print("\t\tWelcome to this Weather Forecaster with BeautifulSoup!\n\n")
  print("Just enter the city you want the weather report for and click Enter!\n\n")

  predict_weather()

if __name__ == "__main__":
  main()
