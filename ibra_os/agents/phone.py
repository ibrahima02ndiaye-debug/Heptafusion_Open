from ..utils.notifications import send_sms_notification

class PhoneGemmaAgent:
    def __init__(self, brain_model="Gemma-Integration"):
        self.brain = brain_model

    def handle_call(self, transcript, client_phone=None):
        """
        Analyse la transcription d'un appel téléphonique.
        """
        print(f"📞 Appel entrant - Transcription: {transcript}")

        # Logique simplifiée de routage (normalement gérée par le brain_model)
        if "rendez-vous" in transcript.lower() or "rdv" in transcript.lower():
            response = self.book_appointment(transcript)
            if client_phone:
                send_sms_notification(client_phone, "Votre rendez-vous chez Ibra Services Inc est confirmé.")
            return response
        elif "commander" in transcript.lower() or "pièce" in transcript.lower():
            return self.manage_order(transcript)
        return "Je vous transfère à Ibra pour plus de détails."

    def book_appointment(self, data):
        return "📅 Rendez-vous enregistré. Je vous envoie une confirmation par SMS."

    def manage_order(self, data):
        return "📦 Pièce ajoutée à la liste des commandes prioritaires."
