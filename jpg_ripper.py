import os
import requests

def download_images(file_path):
    with open(file_path, 'r') as file:
        links = file.readlines()

    # Links verarbeiten
    for index, link in enumerate(links):
        link = link.strip()
        if not link.endswith(".jpg"):
            continue  # Nur .jpg-Dateien herunterladen

        try:
            print(f"Lade Bild {index + 1}: {link}")
            response = requests.get(link, stream=True)
            response.raise_for_status() 

            # Dateiname aus URL extrahieren
            filename = os.path.join(os.getcwd(), link.split("/")[-1])

            # Bild speichern
            with open(filename, 'wb') as img_file:
                for chunk in response.iter_content(chunk_size=8192):
                    img_file.write(chunk)
        except Exception as e:
            print(f"Fehler beim Herunterladen von {link}: {e}")

# Pfad zur Datei mit den Links
input_file = "links.txt"

# Skript ausführen
download_images(input_file)
