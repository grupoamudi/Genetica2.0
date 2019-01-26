# Genetica2.0

This is project of image generation with Genetic Algorithms.

## Dependencies

Run the following command to get all dependencies

```
pip install -r requirements.txt
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

## Contributing

This project is open for contributions. 

To submit a contribution, please fork the repository and submit a Pull Request with your changes. In each commit, please follow the default git commit messages.

Don't forget to [configure your remote for](https://help.github.com/articles/configuring-a-remote-for-a-fork/) and also [sync it with the upstream repository](https://help.github.com/articles/syncing-a-fork/).

We also suggest creating a separate branch for each different feature under development.

### Git default commit messages.

* [FCT] Description (New functionality added)
* [BUG.xx] Bug description (When solved) (For bugs – xx: Bug number in the issue tracker).
* [WIP] Description (Work in Progress – Lacks testing)
* [UPD] Updated to version 1.x.y (New Release – Can go to production)
* [DOC] Added doc (New Documentation)
* [QLTY] Description (Code refactoring and general beauty parameters)
* [OPT] Description (Optimizations – The code has been optimized)

