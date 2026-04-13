class DocsAgent:
    def __init__(self, manual_path="/content/drive/MyDrive/Manuels_Techniques/"):
        self.manual_path = manual_path

    def query_manual(self, question):
        # Ici, on simule la fouille dans tes PDFs de manuels Honda/Ford sur le Drive
        print(f"📚 Recherche dans {self.manual_path} pour : {question}...")
        return f"Résultat trouvé dans le manuel : 'Le serrage préconisé pour {question} est de 120Nm.'"
