from playsound import playsound

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
    openingSound = './sounds/Bubbles_Opening.wav'
    clingButtonSound = './sounds/ClingButton.wav'
    scifiButtonSound = './sounds/SciFiButton.wav'
    successSound = './sounds/Success.wav'
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