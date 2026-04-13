from ibra_os.database import init_db
from ibra_os.agents.vision import VisionAgent
from ibra_os.agents.physics import PhysicsAgent
from ibra_os.agents.memory import MemoryAgent
from ibra_os.agents.web import WebAgent
from ibra_os.agents.docs import DocsAgent
from ibra_os.agents.vocal import VocalAgent
from ibra_os.agents.phone import PhoneAgent
from ibra_os.agents.sms import SMSAgent
from ibra_os.agents.secretary import SecretaryAgent
from ibra_os.webhook import WebhookServer

def main():
    print("--- 🚀 Ibra-OS Swarm : Full Automation Mode ---")

    # 1. Setup Database
    init_db()

    # 2. Initialize Agents
    memory = MemoryAgent()
    web = WebAgent()
    vision = VisionAgent()
    physics = PhysicsAgent()
    docs = DocsAgent()
    vocal = VocalAgent()
    sms = SMSAgent()

    # Orchestrator
    secretary = SecretaryAgent(memory, web, vision, docs, sms)
    phone = PhoneAgent(secretary)

    # Webhook (for Telephone calls)
    webhook = WebhookServer(phone)

    print("\n--- 🏁 TEST COMPLET DU SYSTÈME ---")

    # Step 1: Pre-populate client memory
    print("\n[Action] Initialisation de la base client...")
    memory.update_client("Jean Dupont", "Honda Civic 2018", "Préfère pièces OEM", "Vibration signalée")

    # Step 2: Simulate a phone call with intent extraction
    print("\n[Action] Simulation d'un appel téléphonique entrant...")
    # Transcript would come from Faster-Whisper via Webhook
    transcript = "Bonjour, c'est Jean Dupont, je veux un rendez-vous lundi pour mes freins."
    print(f"📞 Client dit : {transcript}")

    # In a real scenario, the Secretary would identify "Jean Dupont" from transcript or Caller ID
    response = secretary.process_request(transcript, client_name="Jean Dupont")
    print(f"🤖 Réponse IA : {response}")

    # Step 3: Simulate a part order
    print("\n[Action] Détection d'un besoin de pièces...")
    order_transcript = "J'ai besoin de nouveaux pneus pour ma Civic."
    order_res = secretary.process_request(order_transcript)
    print(f"🤖 Réponse IA : {order_res}")

    # Step 4: Webhook demonstration (logic only)
    webhook.run()

    print("\n--- ✅ TOUS LES SYSTÈMES SONT OPÉRATIONNELS ---")

if __name__ == "__main__":
    main()
