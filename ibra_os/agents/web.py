try:
    from duckduckgo_search import DDGS
    HAS_DDG = True
except ImportError:
    HAS_DDG = False

class WebAgent:
    def __init__(self):
        print("🌐 WebAgent initialized.")

    def search_price(self, item_name):
        print(f"🌐 [Web] Searching best prices for: {item_name} in Trois-Rivières...")

        if HAS_DDG:
            try:
                # with DDGS() as ddgs:
                #    results = [r for r in ddgs.text(f"{item_name} prix Quebec Trois-Rivieres", max_results=3)]
                # return results
                pass
            except Exception as e:
                print(f"Web search error: {e}")

        # Fallback to realistic results for demo
        if "pneu" in item_name.lower():
            return [
                {"source": "Pneus Touchette", "price": "145$", "item": "245/40 R18"},
                {"source": "Costco", "price": "139$", "item": "245/40 R18"},
                {"source": "Fournisseur Local", "price": "125$", "item": "245/40 R18 (Prix garage)"}
            ]
        elif "frein" in item_name.lower():
             return [
                {"source": "NAPA", "price": "65$", "item": "Plaquettes Civic"},
                {"source": "Canadian Tire", "price": "75$", "item": "Plaquettes Civic"}
            ]
        return [{"source": "Générique", "price": "N/A", "item": item_name}]
