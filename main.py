import os
from ibra_os.database.manager import init_db, upgrade_db_schema
from ibra_os.agents.vision import VisionAgent
from ibra_os.agents.web import WebAgent
from ibra_os.agents.docs import DocsAgent
from ibra_os.agents.memory import MemoryAgent
from ibra_os.agents.physics import PhysicsAgent
from ibra_os.agents.vocal import VocalAgent, SecretaryAgent
from ibra_os.agents.phone import PhoneGemmaAgent

# Configuration
DB_PATH = "garage_memory.db"

def main():
    print("🚀 Démarrage d'Ibra-OS...")

    # 1. Initialisation de la base de données
    init_db(DB_PATH)
    upgrade_db_schema(DB_PATH)

    # 2. Initialisation des Agents
    memory = MemoryAgent(DB_PATH)
    vision = VisionAgent()
    web = WebAgent()
    docs = DocsAgent()
    physics = PhysicsAgent()
    vocal = VocalAgent()
    secretary = SecretaryAgent()
    phone = PhoneGemmaAgent()

    # (Facultatif) Chargement des modèles lourds si possible
    # vision.load_model()
    # physics.load_model()
    # vocal.load_models()

    print("\n--- 🏁 TEST DU SWARM IA Ibra-OS ---")

    # Scénario 1: Un client appelle pour un rendez-vous
    print("\n[Scénario 1: Appel téléphonique]")
    transcript = "Bonjour, je voudrais prendre un rdv pour un changement de pneus sur ma Honda Civic."
    client_phone = "514-555-0199"
    response = phone.handle_call(transcript, client_phone=client_phone)
    print(f"Assistant Téléphonique: {response}")

    # Enregistrement du client s'il est nouveau
    memory.update_client("Jean Dupont", "Honda Civic 2018", "Préfère pièces OEM", "Vibration signalée")
    client = memory.get_client("Jean Dupont")
    if client:
        memory.add_appointment(client['id'], "2026-05-12 09:00", "Changement de pneus")

    # Scénario 2: Analyse visuelle d'une pièce
    print("\n[Scénario 2: Analyse Vision]")
    image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"
    analysis = vision.analyze_image(image_url, query="Identifie cette pièce mécanique.")
    print(f"Analyse Vision: {analysis}")

    # Scénario 3: Recherche de prix pour la pièce identifiée
    print("\n[Scénario 3: Recherche Web]")
    prices = web.search_price("Pneus 245/40 R18")
    for p in prices:
        print(f"- {p['title']}: {p['body']}")

    # Scénario 4: Consultation du manuel technique
    print("\n[Scénario 4: Consultation Docs]")
    manual_info = docs.query_manual("Serrage culasse Honda Civic 2018")
    print(manual_info)

    # Scénario 5: Perception physique (Robotique)
    print("\n[Scénario 5: Perception Physique]")
    latent = physics.get_world_understanding(image_url)
    print(f"Vecteur latent JEPA: {latent if isinstance(latent, str) else latent.shape}")
    check = physics.physics_check(None, None)
    print(f"Physics Check: {check}")

    # Scénario 6: Interaction Vocale / Secrétaire
    print("\n[Scénario 6: Interaction Vocale]")
    vocal_text = "Vérifie l'historique technique du dernier client."
    action = secretary.process_request(vocal_text)
    if action == "history_check":
        hist = memory.get_client("Jean Dupont")
        vocal.speak(f"L'historique de {hist['nom']} indique : {hist['notes']}")

    print("\n✅ Test du Swarm terminé avec succès.")

if __name__ == "__main__":
    main()
