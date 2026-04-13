import os
from ibra_os.database.manager import init_db, upgrade_db_schema
from ibra_os.agents.vision import VisionAgent
from ibra_os.agents.web import WebAgent
from ibra_os.agents.docs import DocsAgent
from ibra_os.agents.memory import MemoryAgent
from ibra_os.agents.physics import PhysicsAgent
from ibra_os.agents.vocal import VocalAgent, SecretaryAgent
from ibra_os.agents.phone import PhoneGemmaAgent
from ibra_os.utils.notifications import generate_whatsapp_confirmation
from ibra_os.utils.dashboard import generate_hud_html

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
    phone = PhoneGemmaAgent(memory_agent=memory)

    # (Facultatif) Chargement des modèles lourds si possible
    # vision.load_model()
    # physics.load_model()
    # vocal.load_models()

    print("\n--- 🏁 TEST DU SWARM IA Ibra-OS ---")

    # Scénario 1: Un client appelle pour un rendez-vous (Intégration Automatique)
    print("\n[Scénario 1: Appel téléphonique (Intégration Auto)]")
    transcript = "Bonjour, je voudrais prendre un rdv pour un changement de pneus sur ma Honda Civic."
    client_phone = "514-555-0199"
    client_name = "Jean Dupont"
    response = phone.handle_call(transcript, client_phone=client_phone, client_name=client_name)
    print(f"Assistant Téléphonique: {response}")

    # Mise à jour des détails du client (le client a été créé par l'appel s'il n'existait pas)
    memory.update_client(client_name, "Honda Civic 2018", "Préfère pièces OEM", "Vibration signalée")

    # Scénario 2: Analyse visuelle d'une pièce
    print("\n[Scénario 2: Analyse Vision]")
    image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"
    analysis = vision.analyze_image(image_url, query="Identifie cette pièce mécanique.")
    print(f"Analyse Vision: {analysis}")

    # Scénario 3: Recherche de prix pour la pièce identifiée et notification WhatsApp
    print("\n[Scénario 3: Recherche Web & WhatsApp]")
    prices = web.search_price("Pneus 245/40 R18")
    for p in prices:
        print(f"- {p['title']}: {p['body']}")

    # Simulation de génération de confirmation WhatsApp après avoir trouvé un prix
    prix_estime = "185.00"
    whatsapp_msg = generate_whatsapp_confirmation("Jean Dupont", "Changement de pneus", "Lundi 20 Avril", prix_estime)
    print(f"\n[WhatsApp Mockup]\n{whatsapp_msg}")

    # Enregistrement d'une commande dans la base pour le dashboard
    memory.add_order("Pneus 245/40 R18", "Distributeur Trois-Rivières", 185.00)

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

    # Scénario 7: Génération du Dashboard HUD
    print("\n[Scénario 7: Génération du HUD]")
    generate_hud_html(DB_PATH)

    print("\n✅ Test du Swarm terminé avec succès.")

if __name__ == "__main__":
    main()
