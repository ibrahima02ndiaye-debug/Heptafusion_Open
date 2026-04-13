import os
from typing import List, Dict, Optional
from ibra_os.utils.i18n import I18nManager

class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def process(self, task: str) -> Dict:
        raise NotImplementedError

class SecretaryAgent(BaseAgent):
    """
    The Secretary agent is the orchestrator of Ibra-OS.
    """
    def __init__(self, lang="fr"):
        super().__init__(name="Secretary")
        self.i18n = I18nManager(default_lang=lang)
        self.specialization = "Orchestration & Communication"

        self.intent_map = {
            "vision": ["voir", "regarde", "image", "photo", "diagnostic", "frein", "brake", "view"],
            "memory": ["rendez-vous", "client", "rdv", "horaire", "liste", "appointment", "schedule"],
            "physics": ["moteur", "vibration", "son", "bruit", "engine", "noise"]
        }

    def process(self, query: str) -> Dict:
        print(f"[{self.name}] {self.i18n.get('secretary_analyzing')}: {query}")
        query_lower = query.lower()

        for intent, keywords in self.intent_map.items():
            if any(keyword in query_lower for keyword in keywords):
                return {
                    "target": intent.capitalize(),
                    "action": self._get_action_for_intent(intent),
                    "query": query
                }

        return {"target": "General", "action": "chat", "query": query}

    def _get_action_for_intent(self, intent: str) -> str:
        actions = {
            "vision": "analyze_visuals",
            "memory": "query_database",
            "physics": "analyze_physics"
        }
        return actions.get(intent, "process")

    def confirm_appointment(self, client_name: str, date: str) -> bool:
        msg = self.i18n.get("confirmation_sent", name=client_name, date=date)
        print(f"[{self.name}] {msg} via Twilio/WhatsApp...")
        return True
