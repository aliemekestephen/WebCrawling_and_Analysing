# Web Scrapping App
###This is a simple python application which scrapes a webpage, converts scrapped information into a Pandas dataframe and saves the dataframe in a Database. This app can also read the saved data from the database and plot some data.

###
###Requirements:
- python3.10 installed on your computer
- Docker <img height="32" width="32" src="https://skills.thijs.gg/icons?i=docker">
- PostgreSQL <img height="32" width="32" src="https://skills.thijs.gg/icons?i=postgres">

###
###Cloning procedure:
- prepare a project folder and clone the app with this link: https://github.com/aliemekestephen/WebCrawling_and_Analysing.git

###Running the app in Docker
- Start up Docker and make sure Docker desktop is connected
- open up a terminal and enter the following commands:

    `docker pull postgres` ----- To pull the postgres and create the postgres image </br>
`docker build -t 'scrapper:1.0.0' .` ----- To create the scrapper app </br>

  The next step is to create our own network within Docker, so we can link the app and database to use the same network </br>
`docker network create "network_name"` ----- To create the Docker network </br>
`docker network ls"` ----- to view the various networks available in the docker. your network should be in the list. </br>
`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' scrapper` ----- to view the various networks available in the docker. your network should be in the list. </br>
`docker network  inspect "network_name"` ----- Inspect the "network_name" network. Copy the gateway </br>
- open the project folder in an IDE of your choice
- Open the Database_Connection.py go to line 18, replace "localhost" with the Gateway IP address you copied
- type in the following code in the terminal to run the containers: </br>
  `docker run -d --rm -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=1Thesaint -e POSTGRES_DB=Data_Hive --name postgres --net "network_name" postgres` </br>
  `docker run -it --rm --name scrapper --net "network_name" scrapper:1.0.0` </br> </br>
 The scapper application should launch.
  Thanks and have fun!
<!--
