from loguru import logger as lg
import pyttsx3
from TTS import Voice
import multiprocessing


class VoiceAssistant:
    def __init__(self):
        lg.info("Initialize Vassita")

        lg.info("Initialize voice output")
        self.tts = Voice()
        voices = self.tts.get_voice_keys_by_language("German")
        if len(voices) > 0:
            lg.info("Stimme {} gesetzt", voices[0])
            self.tts.set_voice(voices[0])
        else:
            lg.warning("Es wurden keine Stimmen gefunden.")
        self.tts.say("Initialisierung beendet, ich bin bereit!")
        lg.debug("Voice output initialized")

    def run(self):
        lg.info("Vassita started!")


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')

    vassita = VoiceAssistant()
    lg.info("App is running")
    vassita.run()
