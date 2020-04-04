#!/usr/bin/env bash

function start() {

    docker-compose up -d
    docker-compose logs -f

}

function test_server() {

    get_events 40.440549697608 -3.671225309372 20201220

}

function get_events (){
    local latitude=$1
    local longitude=$2
    local date=$3

    docker run --network 2ticket_net curlimages/curl \
        -s "server:8080/near-events/?latitude=$latitude&longitude=$longitude&date=$date"

}


function stop() {

    docker-compose down --rmi local

}

# Main options
for i in "$@"; do
  case "$i" in
    start)
          start
          ;;
    stop)
          stop
          ;;
    restart)
          stop
          start
          ;;
    get_events)
          get_events $2 $3 $4
          break;
          ;;
    test_server)
          test_server
          ;;
    *)
          echo "Usage: $0 {start,stop,restart,get_events,test_server}"
          exit 1
  esac
done