class AI:
    client = None

    def __init__(self, client):
        self.client = client

    def get_answer(self, model, text):
        response = self.client.chat.completions.create(
            model=model,
            messages=text,
        )
        return response
