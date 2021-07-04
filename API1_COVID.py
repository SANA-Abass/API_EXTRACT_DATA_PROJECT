import requests
url = "https://covid-193.p.rapidapi.com/countries"
headers = {
    'x-rapidapi-key': "8455daf7cbmshc24b6667f2e482dp1423fcjsn639ee41624e6",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
def get_countries_from_api1():
    result = requests.request("GET", url, headers=headers)
    result_json = result.json()
    countries = [row for row in result_json['response']]
    return countries