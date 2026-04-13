import re

class SecretaryAgent:
    def __init__(self, memory, web, vision, docs, sms):
        self.name = "Ibra-Assistant"
        self.memory = memory
        self.web = web
        self.vision = vision
        self.docs = docs
        self.sms = sms
        print("👩‍💼 SecretaryAgent (Orchestrator) initialized.")

    def process_request(self, text, client_name=None):
        print(f"👩‍💼 [Secretary] Processing request: '{text}' (Client: {client_name})")
        text_lower = text.lower()

        # Date extraction logic
        date_match = re.search(r"lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche", text_lower)
        extracted_date = date_match.group(0) if date_match else "à définir"

        if "rendez-vous" in text_lower or "rdv" in text_lower:
            if client_name:
                client = self.memory.get_client(client_name)
                if client:
                    self.memory.add_appointment(client['id'], extracted_date, "Entretien Général")
                    # Send WhatsApp confirmation
                    self.sms.send_whatsapp_confirmation(client_name, extracted_date, "Entretien Général")
                    return f"📅 RDV noté pour {extracted_date} ({client_name}). Je l'ai ajouté au calendrier Ibra."
                else:
                    return f"📅 Je n'ai pas trouvé de fiche pour '{client_name}'. Voulez-vous que j'en crée une ?"
            return f"📅 J'ai noté la demande de rendez-vous pour {extracted_date}. Pour quel client est-ce ?"

        elif "commande" in text_lower or "besoin de" in text_lower:
            piece = "Pièce à identifier"
            if "pneu" in text_lower: piece = "Pneus 245/40 R18"
            elif "frein" in text_lower: piece = "Plaquettes de frein"

            self.memory.add_order(piece, "A déterminer", 0.0)
            return f"📦 Commande de {piece} placée en attente pour validation."

        elif "prix" in text_lower or "combien" in text_lower:
            item = "Pneu 245/40 R18" if "pneu" in text_lower else "pièce"
            prices = self.web.search_price(item)
            best_price = min(prices, key=lambda x: x['price'])
            return f"🌐 Le meilleur prix trouvé pour {item} est de {best_price['price']} chez {best_price['source']}."

        elif "analyse" in text_lower or "diagnostic" in text_lower:
            res = self.vision.analyze_image("current_part.jpg", text)
            return f"🔍 Résultat de l'analyse : {res}"

        elif "serrage" in text_lower or "manuel" in text_lower:
            res = self.docs.query_manual(text)
            return f"📚 Selon le manuel : {res}"

        return "Je reste à l'écoute pour gérer vos rendez-vous, commandes ou diagnostics."
