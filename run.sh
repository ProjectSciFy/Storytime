#!/bin/bash

if [[ $(lsof -i:5002) ]]; then
    kill $(lsof -t -i:5002)
fi

if [[ $(lsof -i:5055) ]]; then
    kill $(lsof -t -i:5055)
fi

cd rasa
rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml &
rasa run actions &
cd ..
sleep 60
python3.7 ui.py 

