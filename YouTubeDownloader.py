from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError


lien = input("Saisissez un lien YouTube valide ")

#     Test de la syntaxe correcte d'un lien youtube
# Ex: "https://www.youtube.com/watch?v=Hi7Rx3En7-k"
# "https://youtu.be/rF0mD3Ao3Rs?si=hKjxx1KSpN8K6LWO"
try:
    youtube_video = YouTube(lien)

except RegexMatchError:
    print("==" * 100)
    print(f"(lien)\nErreur: Ce lien ne correspond pas à un lien d'une video Youtube")

else:
    try:
        # Obtention et affichage du titre
        print("==" * 100)
        print("TITRE : " + youtube_video.title)
        ##Obtention de la durée de la vidéo en  sécondes  et quelques traitement pour la mettre en minutes et sécondes
        duree = youtube_video.length / 60
        min = int(duree)
        sec = (duree - min) * 60
        # Obtention et affichage du nom de l'auteur/l'artiste
        print("AUTEUR : " + youtube_video.author)
        # Affichage de la durée de la vidéo
        print("DUREE : " + str(min) + " M " + "{0: .1f}".format(sec) + " Sec")

        print("==" * 100)
        # Recherche des videos et audios disponilees
        print("Les videos disponibles sont : ")
        print("===" * 50)
        # Obtention et affichage de la liste des vidéos disponbles selon les qualités
        for stream_video in youtube_video.streams.filter(progressive=True):
            print(stream_video)
        print("___" * 50)
        print("Les audios disponibles sont : ")
        print("==" * 50)
        # Obtention et affichage de la liste des audios disponbles selon les qualités
        for stream_audio in youtube_video.streams.filter(only_audio=True):
            print(stream_audio)

    except VideoUnavailable as e:
        print(e)
    else:

        # Les vidéos et les audios sont désignés par des identifiants qu'on appelle des itag c'est à partir de ceux-ci qu'on peut selectionner soit la
        #     # video ou l'audio à telecharger
        print("==" * 100)
        choix = input("Saisissez le (itag) correspondant à votre choix ou saisissez 0 pour telecharger la haute qualité vidéo")
        if choix == "0":
            # Avec youtube_video.streams.get_highest_resolution() on obtient la meilleur qualité vidéo/son sans avoir à choisir avec un itag
            downloaded_stream = youtube_video.streams.get_highest_resolution()
            # Obtention et affichage de la taille du fichier choisi à télecharger
            poids = youtube_video.streams.get_highest_resolution().filesize_mb
            print("Taille : " + str(poids) + " Mo")
        else:
            # Code qui s'execute si on a choisi avec un itag plutot que de télecharger la meilleur qualité vidéo/son
            downloaded_stream = youtube_video.streams.get_by_itag(int(choix))
            poids = youtube_video.streams.get_by_itag(int(choix)).filesize_mb
            print("Taille : " + str(poids) + " Mo")

        valider = input("Appuyez sur la touche Enter pour continuer")
        print("Télechargement en cours...")
        # Télechargement du fichier choisi
        downloaded_stream.download()
        print("Téléchargement terminé")

    # @LKanan