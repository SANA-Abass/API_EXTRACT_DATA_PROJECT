import requests

def get_covid_stats_for_past_six_months_of_all_countries():
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/covid-ovid-data/"

    headers = {
        'x-rapidapi-key': "8455daf7cbmshc24b6667f2e482dp1423fcjsn639ee41624e6",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
    result = requests.request("GET", url, headers=headers)
    result_json = result.json()
    return  result_json
print(get_covid_stats_for_past_six_months_of_all_countries())



def get_covid_stats_for_past_six_months_of_india():
    url1 = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/covid-ovid-data/sixmonth/IND"

    headers1 = {
        'x-rapidapi-key': "8455daf7cbmshc24b6667f2e482dp1423fcjsn639ee41624e6",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
    result = requests.request("GET", url1, headers=headers1)
    result_json = result.json()
    return result_json









