import dotenv
import os

dotenv.load_dotenv()


class Config:
    def __init__(self, model: str) -> None:
        self.model = model
        self._config = {
            "phi3": [os.getenv("PHI_ENDPOINT"), os.getenv("PHI_KEY")],
            "mistral": [os.getenv("MISTRAL_ENDPOINT"), os.getenv("MISTRAL_KEY")],
        }

    @property
    def endpoint(self):
        return self._config[self.model][0]

    @property
    def key(self):
        return self._config[self.model][1]
