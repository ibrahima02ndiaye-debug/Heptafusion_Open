import sqlite3

def generate_hud_html(db_path, output_path="ibra_os_hud.html"):
    """
    Génère une page HTML interactive (HUD) pour monitorer le garage.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Récupération des rendez-vous
    cursor.execute("SELECT clients.nom, appointments.date_heure, appointments.service_type, appointments.status FROM appointments JOIN clients ON appointments.client_id = clients.id")
    appointments = cursor.fetchall()

    # Récupération des commandes
    cursor.execute("SELECT piece_nom, fournisseur, prix_estime, etat FROM orders")
    orders = cursor.fetchall()

    conn.close()

    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Ibra-OS HUD - Dashboard Garage</title>
        <style>
            body {{ font-family: sans-serif; background: #121212; color: #e0e0e0; padding: 20px; }}
            h1 {{ color: #00e5ff; }}
            .container {{ display: flex; gap: 20px; }}
            .card {{ background: #1e1e1e; padding: 15px; border-radius: 8px; flex: 1; border-left: 5px solid #00e5ff; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
            th, td {{ text-align: left; padding: 8px; border-bottom: 1px solid #333; }}
            th {{ color: #00e5ff; }}
            .status {{ font-weight: bold; color: #ffeb3b; }}
        </style>
    </head>
    <body>
        <h1>🔧 Ibra-OS Dashboard (HUD)</h1>
        <div class="container">
            <div class="card">
                <h2>📅 Rendez-vous</h2>
                <table>
                    <tr><th>Client</th><th>Date/Heure</th><th>Service</th><th>Statut</th></tr>
                    {''.join([f"<tr><td>{a[0]}</td><td>{a[1]}</td><td>{a[2]}</td><td class='status'>{a[3]}</td></tr>" for a in appointments])}
                </table>
            </div>
            <div class="card">
                <h2>📦 Commandes de Pièces</h2>
                <table>
                    <tr><th>Pièce</th><th>Fournisseur</th><th>Prix Est.</th><th>État</th></tr>
                    {''.join([f"<tr><td>{o[0]}</td><td>{o[1]}</td><td>{o[2]} $</td><td class='status'>{o[3]}</td></tr>" for o in orders])}
                </table>
            </div>
        </div>
        <p><i>Dernière mise à jour : automatique via Ibra-OS Agent Swarm</i></p>
    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Dashboard HUD généré avec succès : {output_path}")
    return output_path
