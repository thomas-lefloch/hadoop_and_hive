# Exploration d'Hadoop, de MapReduce et de Hive

il faut executer tous les scripts depuis la racine du projet

Lien vers la page d'admin du namenode
[http://localhost:9870/](http://localhost:9870/)

1) realtime_data_downloader.py récupère les stations de nantes depuis l'api "Données temps-réel" de JCDECAUX. Il écrit les résultats (1 objet json par ligne) dans le fichier `./files_to_add/{epoch_time}.txt`.
2) Un volume partagé est monté sur le dossier `./files_to_add/` pour communiquer les fichiers au container docker. On rajoute le fichier à hadoop.

# Architecture hadoop
voir `docker-compose.yaml`
- 1 namenode
- 3 datanodes, Replication Factor = 1
- 1 node manager
- 1 ressource manager
- Hive + metastore (postgres)

# Dependencies
Driver postgres pour Hive metastore
https://jdbc.postgresql.org/download/ version 42.7.11. à mettre dans le dossier `./dependencies/`

# Créer les dossiers /data-lake/*
```sh 
./setup.ps1
```

# Récuperer la donnée de l'api de JCDECAUX
ne pas oublier de mettre la clé d'api dans un .env voir `.env.example` puis éxécuter
```sh 
python ./download_data/realtime_api.py
```

# Ajouter la donnée aux HDFS
```sh 
./files_to_add/add_files_to_hdfs.ps1
```

# Starting map reducers
```sh 
./map_reducers/mr1_load_factor/start.ps1
```

# Create hive table

ouvrir un shell pour les commande sql dans hive
```sh
 docker compose exec -it hiveserver2-standalone beeline -u 'jdbc:hive2://hiveserver2-standalone:10000/' 
```

executer le script `create_hive_tables.sql`