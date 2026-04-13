def send_sms_notification(phone_number, message):
    """
    Sends an SMS notification using a placeholder for Twilio or Vonage API.
    """
    print(f"📱 [SMS] To {phone_number}: {message}")
    # Integration code for Twilio/Vonage would go here
    return True

def generate_whatsapp_confirmation(nom_client, service, date, prix_estime):
    """
    Génère un message professionnel prêt à être envoyé via API WhatsApp.
    """
    message = f"""
    🔧 *IBRA SERVICES INC - Confirmation*

    Bonjour {nom_client},
    Votre rendez-vous pour : *{service}* est confirmé pour le : *{date}*.

    📍 Lieu : Trois-Rivières, QC
    💰 Estimation des pièces : {prix_estime} $

    Une question ? Répondez directement à ce message.
    """
    return message.strip()
