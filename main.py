import pandas as pd
from datetime import datetime
from instagram_private_api import Client
from py_pinterest import PinterestAPI

# Lecture du fichier Excel
df = pd.read_excel("chemin_vers_le_fichier_excel.xlsx")

# Configuration de l'API Instagram
username = "votre_nom_d_utilisateur"
password = "votre_mot_de_passe"
api = Client(username, password)

# Configuration de l'API Pinterest
pinterest_email = "votre_email_pinterest"
pinterest_password = "votre_mot_de_passe_pinterest"
pinterest_board = "nom_de_votre_tableau"

# Parcours des lignes du fichier Excel
for index, row in df.iterrows():
    nom_publication = row["Nom de la publication"]
    description = row["Description"]
    titre = row["Titre"]
    hashtags = row["Hashtags"]
    date_publication = row["Date de publication"]

    # Conversion de la date de publication en format datetime
    date_publication = datetime.strptime(date_publication, "%Y-%m-%d %H:%M:%S")

    # Planification de la publication sur Instagram
    api.post_photo("chemin_vers_la_photo.jpg", caption=f"{titre}\n\n{description}\n\n{hashtags}", upload_id=None,
                   options={"date": date_publication.timestamp()})

    # Planification de la publication sur Pinterest
    pinterest_api = PinterestAPI(pinterest_email, pinterest_password)
    pinterest_api.login()
    pinterest_api.create_pin(image_path="chemin_vers_l_image.jpg", board_name=pinterest_board,
                             title=titre, description=f"{description}\n\n{hashtags}")

