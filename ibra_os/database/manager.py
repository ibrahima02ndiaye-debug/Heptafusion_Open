import sqlite3
import os

def init_db(db_path):
    """Initializes the database with the clients table."""
    dirname = os.path.dirname(db_path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    conn = sqlite3.connect(db_path)
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
    conn.commit()
    conn.close()
    print(f"Database initialized at {db_path}")

def upgrade_db_schema(db_path):
    """Upgrades the database schema with appointments and orders tables."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Table des Rendez-vous
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY,
            client_id INTEGER,
            date_heure TEXT,
            service_type TEXT,
            status TEXT DEFAULT 'Prévu'
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
    print(f"Database schema upgraded at {db_path}")
