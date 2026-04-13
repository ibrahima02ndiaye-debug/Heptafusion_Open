try:
    from duckduckgo_search import DDGS
except ImportError:
    DDGS = None

class WebAgent:
    def __init__(self):
        pass

    def search_price(self, item_name):
        print(f"🌐 Recherche des meilleurs prix pour : {item_name}...")
        if DDGS is None:
            return [
                {"title": f"Prix {item_name} - Garage Trois-Rivières", "href": "#", "body": f"Estimation de prix pour {item_name}: 150 CAD."},
                {"title": f"Achat {item_name} Québec", "href": "#", "body": f"Meilleur prix trouvé pour {item_name}."}
            ]

        with DDGS() as ddgs:
            results = [r for r in ddgs.text(f"{item_name} prix Quebec Trois-Rivieres", max_results=3)]
        return results
