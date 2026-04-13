from ..utils.notifications import send_sms_notification

class PhoneGemmaAgent:
    def __init__(self, memory_agent=None, brain_model="Gemma-Integration"):
        self.memory = memory_agent
        self.brain = brain_model

    def handle_call(self, transcript, client_phone=None, client_name="Client Inconnu"):
        """
        Analyse la transcription d'un appel téléphonique et agit sur le système.
        """
        print(f"📞 Appel entrant - Transcription: {transcript}")

        # Logique simplifiée de routage
        if "rendez-vous" in transcript.lower() or "rdv" in transcript.lower():
            response = self.book_appointment(transcript)

            # Intégration automatique avec la mémoire
            if self.memory:
                client = self.memory.get_client(client_name)
                if not client:
                    self.memory.update_client(client_name, "Inconnu", "A préciser", "Nouveau client via téléphone")
                    client = self.memory.get_client(client_name)

                # Simulation d'extraction de date/service
                self.memory.add_appointment(client['id'], "2026-XX-XX", "Entretien général")

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
