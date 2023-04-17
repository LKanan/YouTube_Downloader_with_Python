from pytube import YouTube
import re
lien= input("Saisissez un lien YouTube valide ")
# Ex: lien="https://www.youtube.com/watch?v=Hi7Rx3En7-k"
regex1=re.compile(r'^(https://www.youtube.com/watch\?v=)\b[A-Za-z0-9._%+-]{11}\b')
regex2=re.compile(r'^(https://m.youtube.com/watch\?v=)\b[A-Za-z0-9._%+-=&]{55}\b')
#Niveau de vérification du lien entré par l'utilisateur pour s'assurer que c'est un lien YouTube
while True:
    if regex1.search(lien) or regex2.search(lien) :
        youtube_video= YouTube(lien)
        break 
    else:
        print("=="*100)
        print("( "+lien+" ) n'est pas un lien valide")
        lien= input("Saisissez un lien YouTube valide ")
#Si le lien est celui de YouTube on execute le code ci-bas
try:
    #Obtention et affichage du titre
    print("TITRE : " + youtube_video.title)
    ##Obtention de la durée de la vidéo en  sécondes  et quelques traitement pour la mettre en minutes et sécondes
    duree=youtube_video.length/60
    min=int(duree)
    sec=(duree-min)*60
    #Obtention et affichage du nom de l'auteur/l'artiste
    print("AUTEUR : " + youtube_video.author)
    #Affichage de la durée de la vidéo
    print("DUREE : " + str(min) + " M "+ "{0: .1f}".format(sec)+" Sec")
    print("Les videos disponibles sont : ")
    print("==="*50)
    #Obtention et affichage de la liste des vidéos disponbles selon les qualités
    for stream_video in youtube_video.streams.filter(progressive=True):
         print(stream_video)
    print("___"*50)
    print("Les audios disponibles sont : ")
    print("=="*50)
    #Obtention et affichage de la liste des audios disponbles selon les qualités
    for stream_audio in youtube_video.streams.filter(only_audio=True):
         print(stream_audio) 
    #Les vidéos et les audios sont désignés par des identifiants qu'on appelle des itag c'est à partir de ceux-ci qu'on peut selectionner soit la
    # video ou l'audio à telecharger 
    choix=input("Saisissez le (itag) correspondant à votre choix ou saisissez 0 pour telecharger la haute qualité vidéo  ")
    if choix=="0":
    #Avec youtube_video.streams.get_highest_resolution() on obtient la meilleur qualité vidéo/son sans avoir à choisir avec un itag
        downloaded_stream=youtube_video.streams.get_highest_resolution()
        #Obtention et affichage de la taille du fichier choisi à télecharger
        poids=youtube_video.streams.get_highest_resolution().filesize_mb
        print("Taille : "+str(poids)+" Mo")
    else:
    #Code qui s'execute si on a choisi avec un itag plutot que de télecharger la meilleur qualité vidéo/son
        downloaded_stream=youtube_video.streams.get_by_itag(int(choix))
        poids=youtube_video.streams.get_by_itag(int(choix)).filesize_mb
        print("Taille : "+str(poids)+" Mo")
    print("Télechargement en cours...")
    #Télechargement du fichier choisi
    downloaded_stream.download()
    print("Téléchargement terminé")
except:
    print("Ce lien ne correspond à aucune vidéo YouTube ou vérifiez votre connexion")
#@LKanan
