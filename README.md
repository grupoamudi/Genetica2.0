# Genetica2.0

## Dependencies

Run the following command to get all dependencies

```
pip -r requirements.txt
```

To start the server

```
set FLASK_APP=server.py 
flask run
```

## How will it work?

The program will be a web server. It will serve a client file: index.html.

The server will analyse if there's any recorded files. If there is it will load them. If not, it will create them.
Every X ticks, some mutation will occour.

Every X votes it will close de pool and execute the genetic crossing

The server will then receive messages
- "connected": A new user connected
- "vote" (json): Choses one of the images to vote
- "disconnected": A user has disconnected

The server will broadcast the following messages
- "update_generations": instructs the client to get new images
