try:
    from flask import Flask, request
    HAS_FLASK = True
except ImportError:
    HAS_FLASK = False

class WebhookServer:
    def __init__(self, phone_agent):
        self.phone_agent = phone_agent
        self.app = None
        if HAS_FLASK:
            self.app = Flask(__name__)
            self._setup_routes()

    def _setup_routes(self):
        @self.app.route("/voice", methods=['POST'])
        def voice_webhook():
            # Simulated Twilio webhook
            transcript = request.values.get("SpeechResult", "Bonjour Ibra Services")
            print(f"🌐 [Webhook] Received voice transcript: {transcript}")
            response_text = self.phone_agent.handle_call(transcript)

            twiml = f"""
<Response>
    <Say language="fr-FR">{response_text}</Say>
</Response>
"""
            return twiml

    def run(self, debug=False):
        if self.app:
            print("🌐 Starting Webhook server on port 5000...")
            # In a real environment, we'd use run_with_ngrok(self.app)
            # self.app.run(port=5000, debug=debug)
        else:
            print("Flask not installed. Webhook server cannot run.")

if __name__ == "__main__":
    # Mock phone agent for testing
    class MockPhoneAgent:
        def handle_call(self, t): return f"Noté: {t}"

    server = WebhookServer(MockPhoneAgent())
    server.run()
