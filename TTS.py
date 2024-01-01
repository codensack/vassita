from loguru import logger as lg
import time, pyttsx3
import multiprocessing

def __speak__(text, voice_id):
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()

class Voice:
    def __init__(self):
        self.process = None
        self.voice_id = """HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_DE-DE_HEDDA_11.0"""

    def say(self, text):
        if self.process:
            self.stop()

        p = multiprocessing.Process(target=__speak__, args=(text, self.voice_id))
        p.start()
        self.process = p

    def set_voice(self, voice_id):
        self.voice_id = voice_id

    def stop(self):
        if self.process:
            self.process.terminate()


    def get_voice_keys_by_language(self, language=''):
        result = []
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        for voice in voices:
            if language == '':
                result.append(voice.id)
            elif language.lower() in voice.name.lower():
                result.append(voice.id)
        return result