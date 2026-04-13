class PhoneAgent:
    def __init__(self, secretary):
        self.secretary = secretary
        print("📞 PhoneAgent initialized.")

    def handle_call(self, transcript):
        print(f"📞 [Phone] Incoming call transcript: '{transcript}'")
        response = self.secretary.process_request(transcript)
        return response
