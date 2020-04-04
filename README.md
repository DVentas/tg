### Buy Tickets Architecture

Architecture for building recomendation events ticket system. 

This repository is the initial work to has a local environment for developers.

We provide method to run Postgis Database, with init data about places (in madrid), 
events in this places (randomly) and tickets for this events (randomly).

The principal script is main.sh, and has five principal functions:

Init environment

`./main.sh start`

Stop and clean environment.

`./main.sh stop`

Stop and then start environment.

`./main.sh restart`

Call with rest to server to test with fixed data.

`./main.sh test_server`

Query events by latitude longitude and date

`./main.sh get_events 40.440549697608 -3.671225309372 20201220`

After start, jupyter notebook is accesible by web browser in http://localhost:8888

`http://localhost:8888/`