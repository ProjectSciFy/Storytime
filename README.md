# Storytime
Generate a brief story (both written and pictoral) with a plot based on several input words from a user

## rasa information

A bash script has been created to run the two servers and correspoinding UI.
From the storytime folder, run:
`bash run.py`

to run project must run the actions server and rasa seperatly, then UI.py.  

run the following within the rasa folder
`rasa run actions`
`rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml`

then run `python ui.py` as normal in storytime directory


Useful Commands:
`rasa train` to train a new assistant based on modified training data
`rasa shell` to chat with a trained assistant

https://rasa.com/docs/rasa/command-line-interface/ 