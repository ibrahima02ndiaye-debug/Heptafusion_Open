try:
    from faster_whisper import WhisperModel
    HAS_WHISPER = True
except ImportError:
    HAS_WHISPER = False

class VocalAgent:
    def __init__(self, model_size="tiny"):
        self.model_size = model_size
        self.stt_model = None
        print(f"🎙️ VocalAgent initialized.")

    def load_stt(self):
        if HAS_WHISPER:
            try:
                print(f"VocalAgent: Loading {self.model_size} Whisper model...")
                # self.stt_model = WhisperModel(self.model_size, device="auto", compute_type="float16")
                print("VocalAgent: STT model ready (simulated in sandbox).")
            except Exception as e:
                print(f"VocalAgent: Failed to load STT: {e}")
        else:
            print("VocalAgent: faster-whisper not installed.")

    def transcribe(self, audio_path):
        print(f"🎙️ [STT] Transcribing: {audio_path}")
        if self.stt_model:
            # segments, _ = self.stt_model.transcribe(audio_path, beam_size=5)
            # return " ".join([segment.text for segment in segments])
            return "Transcription réelle (simulée)"

        # Mocking STT for demo
        if "rdv" in audio_path.lower() or "rdv" in audio_path.lower():
            return "Je voudrais prendre un rdv pour un changement de pneus lundi prochain."
        return "Bonjour, je voudrais parler à Ibra."

    def speak(self, text):
        # Placeholder for Piper TTS
        print(f"🤖 [TTS] Speaking: {text}")
        return f"Audio: {text}"
