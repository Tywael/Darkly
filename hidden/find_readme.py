import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from time import sleep

BASE_URL = "http://192.168.1.101/.hidden/"
DOWNLOAD_DIR = "readmes"
flag_found = False
flag_lock = threading.Lock()

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def deep_crawl_and_check(url, path=""):
    global flag_found

    if flag_found:
        return

    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return
    except:
        return

    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a"):
        if flag_found:
            return

        href = link.get("href")
        if href in ["../", "./"]:
            continue

        full_url = urljoin(url, href)
        full_path = path + href

        if "readme" in href.lower():
            try:
                content = requests.get(full_url, timeout=30).text
                if "flag" in content.lower():
                    with flag_lock:
                        if not flag_found:
                            print(f"\n🎯 FLAG DÉTECTÉ dans : {full_path}")
                            filename = quote(full_path.strip("/").replace("/", "_"))
                            file_path = os.path.join(DOWNLOAD_DIR, filename)
                            with open(file_path, "w", encoding="utf-8") as f:
                                f.write(content.strip())
                            print(f"[✓] Flag sauvegardé dans : {file_path}")
                            print(f"\n📦 Contenu du flag :\n{content.strip()}\n")
                            flag_found = True
                    return
            except Exception as e:
                print(f"[!] Échec lecture {full_url} : {e}")

        elif href.endswith("/"):
            deep_crawl_and_check(full_url, full_path)
print("[*] Scan initial de .hidden/...\n")

top_level_folders = []

try:
    response = requests.get(BASE_URL, timeout=5)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href.endswith("/") and href not in ["./", "../"]:
                folder_url = urljoin(BASE_URL, href)
                top_level_folders.append((folder_url, href))
except Exception as e:
    print(f"[!] Erreur d'accès à .hidden/: {e}")
    exit(1)

print(f"[+] {len(top_level_folders)} dossiers de premier niveau trouvés.\n")
print("[*] Lancement des threads...\n")
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(deep_crawl_and_check, url, path) for url, path in top_level_folders]
    for future in as_completed(futures):
        if flag_found:
            break
if not flag_found:
    print("\n[✘] Aucun FLAG trouvé.")
else:
    print("\n✅ FLAG récupéré avec succès.")