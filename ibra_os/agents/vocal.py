try:
    from faster_whisper import WhisperModel
except ImportError:
    WhisperModel = None

class VocalAgent:
    def __init__(self, stt_model_size="tiny"):
        self.stt_model_size = stt_model_size
        self.stt_model = None

    def load_models(self):
        if WhisperModel is None:
            print("faster-whisper not installed. Skipping load.")
            return
        print(f"Loading Whisper model ({self.stt_model_size})...")
        self.stt_model = WhisperModel(self.stt_model_size, device="cpu", compute_type="int8")

    def transcribe(self, audio_file):
        if self.stt_model is None:
            return "Besoin d'un rendez-vous pour changement de pneus."

        segments, _ = self.stt_model.transcribe(audio_file, beam_size=5)
        return " ".join([segment.text for segment in segments])

    def speak(self, text):
        # Simulation TTS avec Piper
        print(f"🤖 Vocal Output: {text}")
        return True

class SecretaryAgent:
    def __init__(self, name="Ibra-Assistant"):
        self.name = name

    def process_request(self, voice_text):
        print(f"🎙️ L'agent a entendu : {voice_text}")

        # Logique de décision
        if "rendez-vous" in voice_text.lower() or "rdv" in voice_text.lower():
            return "appointment"
        elif "prix" in voice_text.lower():
            return "price_check"
        elif "analyse" in voice_text.lower() or "diagnostique" in voice_text.lower():
            return "vision_analysis"
        elif "historique" in voice_text.lower():
            return "history_check"
        else:
            return "general_query"
