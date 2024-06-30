from stem import Signal
from stem.control import Controller
import requests
import time

# Tor kontrol portuna bağlanmak için şifre
TOR_PASSWORD = 'TurkHackTeam'

def get_tor_session():
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session

def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=TOR_PASSWORD)
        controller.signal(Signal.NEWNYM)

def get_current_ip(session):
    try:
        response = session.get("http://httpbin.org/ip")
        return response.json()["origin"]
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    while True:
        renew_tor_ip()
        session = get_tor_session()
        current_ip = get_current_ip(session)
        print(f"Current IP: {current_ip}")
        time.sleep(5)
