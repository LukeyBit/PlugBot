# PlugBot
A simple bot that each day sends its subscribers a message on Telegram with a graph of the electricity prices for the next 24 hours in zone S3, Sweden.

## How it works
This simple bot allows users to subscribe or unsibscribe to the service for free, through a simple Telegram message. The list of subscribers is stored in a Postgresql database. 
The bot collects the electricity prices from Nordpool's API and creates a graph of them using pandas and matplotlib, which it then sends to the subscribers!

## How to use
The bot can be run on any machine supporting Python and/or Docker. The Docker images can be found on Docker Hub (link below).

### Running with Docker
Use the build the image with the environment variables `DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT` being set to the correct information for your database. Alternatively use docker compose.

[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](https://hub.docker.com/r/lukeybit/plugbot/)

### Running without Docker
To run the bot without Docker, simply clone the project, create a `.env` file containing the `DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT` variables, and run the `main.py` file at the root of the project.
