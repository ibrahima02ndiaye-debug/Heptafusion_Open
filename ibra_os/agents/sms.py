class SMSAgent:
    def __init__(self, api_key="MOCK_API_KEY"):
        self.api_key = api_key
        print("📱 SMSAgent initialized (Twilio/Vonage integration).")

    def send_notification(self, phone_number, message):
        print(f"📱 [SMS] Sending to {phone_number}: {message}")
        return f"SMS sent to {phone_number}"

    def send_whatsapp_confirmation(self, client_name, date, service):
        template = f"""
*IBRA SERVICES INC - Confirmation*
Bonjour {client_name},
Votre rendez-vous pour {service} est confirmé pour le {date}.
Lieu: Trois-Rivières.
À bientôt!
"""
        print(f"📱 [WhatsApp] Sending template to {client_name}:\n{template}")
        return "WhatsApp message sent"

if __name__ == "__main__":
    agent = SMSAgent()
    agent.send_whatsapp_confirmation("Jean Dupont", "lundi", "Changement de pneus")
