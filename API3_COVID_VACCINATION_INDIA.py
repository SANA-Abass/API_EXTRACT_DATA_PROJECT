"""
utiliser Python pour obtenir et traiter des données à partir d'une API. Nous utilisons l'API récemment publiée de Co-Win (la plateforme de vaccination de l'Inde) pour obtenir des données de la plateforme et nous envoyer une alerte lorsqu'il y a des créneaux de vaccination disponibles dans les sept prochains jours.
"""


#********************************************** DATABASE MYSQL ***************************************


#********************************************** GET DATA FROM OUR API2 ***************************************
import datetime
import requests
def create_session_info(center, session):
    return {"name": center["name"],
            "date": session["date"],
            "capacity": session["available_capacity"],
            "age_limit": session["min_age_limit"]}

def get_sessions(data):
    for center in data["centers"]:
        for session in center["sessions"]:
            yield create_session_info(center, session)

def is_available(session):
    return session["capacity"] > 0

def is_eighteen_plus(session):
    return session["age_limit"] == 18

def get_for_seven_days(start_date):
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
    params = {"district_id": 571, "date": start_date.strftime("%d-%m-%Y")}
    resp = requests.get(url, params=params)#headers=headers paramètre facultatif necessaire pour le mail
    data = resp.json()
    return [session for session in get_sessions(data) if is_eighteen_plus(session) and is_available(session)]

def create_output(session_info):
    return f"{session_info['date']} - {session_info['name']} ({session_info['capacity']})"

# test


"""
import email
import smtplib

username = ""
password = ""
#gestion de mail
if not content:
    print("No availability")
else:
    email_msg = email.message.EmailMessage()
    email_msg["Subject"] = "Vaccination Slot Open"
    email_msg["From"] = username
    email_msg["To"] = username
    email_msg.set_content(content)

    with smtplib.SMTP(host='smtp.gmail.com', port='587') as server:
        server.starttls()
        server.login(username, password)
        server.send_message(email_msg, username, username)
        
# liens utiles:
#https://apisetu.gov.in/public/api/cowin/cowin-public-v2
#https://www.youtube.com/watch?v=reeeNhl5rTY
"""
