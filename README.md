# Storytime
Generate a brief story (both written and pictoral) with a plot based on several input words from a user

## rasa information

to run project must run the actions server and rasa seperatly, then UI.py.  

run the following within the rasa folder
`rasa run actions`
`rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml`

then run `python ui.py` as normal in storytime directory

TODO: create bash script to run automatically

Useful Commands:
`rasa train` to train a new assistant based on modified training data
`rasa shell` to chat with a trained assistant

https://rasa.com/docs/rasa/command-line-interface/ 