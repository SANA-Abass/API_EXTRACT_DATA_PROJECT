import DB_MANAGER
from datetime import datetime
import API1_COVID
import API2_VACOVID
import API3_COVID_VACCINATION_INDIA

def main():
    # content = "\n".join([create_output(session_info) for session_info in get_for_seven_days(datetime.today())])
    data_list = API3_COVID_VACCINATION_INDIA.get_for_seven_days(datetime.today())
    indice = 0
    for row in data_list :
        hospital_name = row['name']
        date_vacination = row['date']
        capacity = row['capacity']
        day, month, year = date_vacination.split('-')
        tmp = '-'.join([year, month, day])
        date_format_sql = datetime.strptime(tmp, '%Y-%m-%d').__format__("%Y-%m-%d")

        sql1 = "INSERT IGNORE INTO vaccination_session_tbl(date_vacination, capacity) VALUES (%s, %s)"
        val1 = (date_format_sql, capacity)
        DB_MANAGER.insert_into_tble(sql1, val1)


        sql2 = "INSERT IGNORE INTO hospital_tbl(id_hospital, hospital_name) VALUES (%s, %s)"
        val2 = (indice, hospital_name)
        DB_MANAGER.insert_into_tble(sql2, val2)
        indice = indice + 1
    # query = "select * from vaccination_tble"
    # DB_MANAGER.select_all(query)




    countries = API1_COVID.get_countries_from_api1()
    for i in range(len(countries)):
        tmp_country = countries[i]
        country_query = "INSERT IGNORE INTO country_tble (id_country, name_country) VALUES (%s, %s)"
        DB_MANAGER.insert_into_tble(country_query, (i, tmp_country))




    res = API2_VACOVID.get_covid_stats_for_past_six_months_of_india()
    for row in res:
        date_stats = row['date']
        new_cases = row['new_cases']
        total_cases = row['total_cases']
        total_deaths = row['total_deaths']
        new_deaths = row['new_deaths']
        total_tests = row['total_tests']
        new_tests = row['new_tests']

        sql3 = "INSERT IGNORE INTO statistique_tbl(new_cas, total_cas, total_death, new_death, total_test, new_test, date_stats) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val3 = (new_cases, total_cases, total_deaths, new_deaths, total_tests, new_tests, date_stats)
        DB_MANAGER.insert_into_tble(sql3, val3)


main()