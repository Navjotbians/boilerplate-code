import json
import os
from pathlib import Path


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
print(os.path.join(PROJECT_DIR, "config.json"))


class Config:
    def __init__(self, config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
        self.data_path = Path(config["data_path"]).resolve()
        self.model_path = Path(config["model_path"]).resolve()
        self.num_epochs = config["num_epochs"]
        self.learning_rate = config["learning_rate"]
