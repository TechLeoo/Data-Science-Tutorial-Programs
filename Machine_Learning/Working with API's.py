import requests
import pandas as pd

url = "https://numbersapi.p.rapidapi.com/42/trivia"

querystring = {"fragment":"true","notfound":"floor","json":"true"}

headers = {
	"X-RapidAPI-Key": "826302b233mshc1b686eb91eda58p1f7018jsnd7fc33b414de",
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

name = input("Name: ")
age = int(input("Age: "))

question = int(input("\nWill you like to learn some interesting math fact? \nPRESS 1: Yes\nPRESS 2: No \nResponse: "))
if question == 1:
    store = response.json()
    result = store["text"]
    number = store["number"]
    print(f"\n\n{result} is {str(number)}".capitalize())
elif question == 2:
    print("Goodbye!")
else:
    print("Invalid Input")
