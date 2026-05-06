il faut executer tous les scripts depuis la racine du projet

Lien vers la page d'admin du namenode
[http://localhost:9870/](http://localhost:9870/)

1) realtime_data_downloader.py récupère les stations de nantes depuis l'api "Données temps-réel" de JCDECAUX. Il écrit les résultats (1 objet json par ligne) dans le fichier `./files_to_add/{epoch_time}.txt`.
2) Un volume partagé est monté sur le dossier `./files_to_add/` pour communiquer les fichiers au container docker. On rajoute le fichier à hadoop.
On supprime le fichier de `./files_to_add/` . On en a plus besoin.