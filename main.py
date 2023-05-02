from src.features.build_features import hello_members
import os

from src.configurations.config import (
    Config,
)  # config class is stored in directory src/config.py

config_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "src", "configurations", "config.json"
)

config = Config(config_file)

if __name__ == "__main__":
    hello_members()
    print("Dummy parameters:")
    print("Learning rate : {}".format(config.learning_rate))
    print("Number of epochs : {}".format(config.num_epochs))
