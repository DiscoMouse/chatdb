# chatdb
A simple Docker compose script with a Python script to dump chat_downloader data to a mongodb instance

Docker/Docker Desktop is required on the host.
```
git clone https://github.com/DiscoMouse/chatdb.git
cd chatdb
docker compose up -d --build
```
It should build two containers:

### A python container 

You can connect to this through VS Code (requires Docker extension) by pressing F1 and selecting connect to running docker container, and then selecting the Python container. The vs code terminal window should open the /code directory within the conatiner to enable you to run or edit or create new python scripts within it as needed. This directory uses docker volumes to map to the code directory in the root of the chatdb directory. This means any changes you make here will be saved even if you delete your containers.

### A database container

Mongodb installed with port 27017 mapped to the host you can use Mongodb shell or compass on the host to run queries.
The database is saved to a volume (it should create a directory called db in the chatdb directory you cloned) and you can safely delete containers and recreate them without losing any data, but please note that any changes to the login credentials in the docker-compose.yml will be ignored on subsequent container builds as mongodb credentials are stored in the database. Change the credentials from the default before running the script or you'll need to do this using mongosh or compass.
