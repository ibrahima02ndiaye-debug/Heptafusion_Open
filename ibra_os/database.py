import sqlite3
import os

DB_PATH = "garage_memory.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Table Clients & Véhicules
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            nom TEXT,
            vehicule TEXT,
            preferences TEXT,
            historique_notes TEXT
        )
    ''')

    # Table des Rendez-vous
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY,
            client_id INTEGER,
            date_heure TEXT,
            service_type TEXT,
            status TEXT DEFAULT 'Prévu',
            FOREIGN KEY(client_id) REFERENCES clients(id)
        )
    ''')

    # Table des Commandes de pièces
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            piece_nom TEXT,
            fournisseur TEXT,
            prix_estime REAL,
            etat TEXT DEFAULT 'En attente'
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print(f"Database initialized at {DB_PATH}")
