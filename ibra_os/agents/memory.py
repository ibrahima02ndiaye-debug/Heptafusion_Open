import sqlite3
import os

class MemoryAgent:
    def __init__(self, db_path="garage_memory.db"):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
             # Try to find it if we are in a subfolder or something,
             # but for main.py it should be in the root.
             pass

    def get_client(self, name):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients WHERE nom LIKE ?", (f"%{name}%",))
        client = cursor.fetchone()
        conn.close()
        if client:
            return {
                "id": client[0],
                "nom": client[1],
                "vehicule": client[2],
                "prefs": client[3],
                "notes": client[4]
            }
        return None

    def update_client(self, nom, vehicule, prefs, notes):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO clients (nom, vehicule, preferences, historique_notes)
            VALUES (?, ?, ?, ?)
        ''', (nom, vehicule, prefs, notes))
        conn.commit()
        conn.close()
        return f"✅ Mémoire mise à jour pour {nom}."

    def add_appointment(self, client_id, date_heure, service_type):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO appointments (client_id, date_heure, service_type)
            VALUES (?, ?, ?)
        ''', (client_id, date_heure, service_type))
        conn.commit()
        conn.close()
        return "📅 Rendez-vous enregistré."

    def add_order(self, piece_nom, fournisseur, prix_estime):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO orders (piece_nom, fournisseur, prix_estime)
            VALUES (?, ?, ?)
        ''', (piece_nom, fournisseur, prix_estime))
        conn.commit()
        conn.close()
        return "📦 Pièce ajoutée à la liste des commandes."
