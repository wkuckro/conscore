import requests


headers = {'X-API-Key': 'd939NE7Ksk6mSmDxT1r5za8BBw4GaBBz8ndMmdaU'}
response = requests.get("https://api.propublica.org/congress/v1/115/senate/members.json", headers=headers)
response.json()
# Print the status code of the response.
print(response.json())
