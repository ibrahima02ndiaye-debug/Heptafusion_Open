class DocsAgent:
    def __init__(self, manual_path="/content/drive/MyDrive/Manuels_Techniques/"):
        self.manual_path = manual_path
        print(f"📚 DocsAgent initialized with path: {self.manual_path}")

    def query_manual(self, question):
        print(f"📚 [Docs] Querying manuals for: {question}")
        # Simulated RAG response
        if "civic" in question.lower() and "serrage" in question.lower():
            return "Le serrage préconisé pour les boulons de roue Honda Civic 2018 est de 108 Nm (80 lb-pi)."
        elif "focus" in question.lower() and "culasse" in question.lower():
            return "Le serrage préconisé pour la culasse Ford Focus 2018 est de 120 Nm."

        return "Information non trouvée dans les manuels locaux. Veuillez consulter la base de données constructeur."
