from playsound import playsound
import os
path = os.path.abspath(os.getcwd()).strip().replace(" ", "").replace("//", "/")

'''
LINK TO FIND SOUNDS: https://freesound.org/browse/tags/press/?page=2#sound
LINK TO CROP SOUNDS: https://clideo.com/editor/cut-audio

PIP INSTALL COMMAND: pip install playsound==1.2.2 
        OR:
                    pip3.7 install playsound==1.2.2
                    pip3 install -U PyObjC
'''

def updateSounds():
    sounds = {}
    openingSound = path + '/sounds/Bubbles_Opening.wav'
    clingButtonSound = path + '/sounds/ClingButton.wav'
    scifiButtonSound = path + '/sounds/SciFiButton.wav'
    successSound = path + '/sounds/Success.wav'
    sounds["OPENING"] = openingSound
    sounds["CLING"] = clingButtonSound
    sounds["SCIFI"] = scifiButtonSound
    sounds["SUCCESS"] = successSound
    return sounds
    
SOUNDS = updateSounds()

# PLAY SOUND:
def playSound(soundName: str):
    sound = soundName.upper()
    playsound(SOUNDS[sound], False)
