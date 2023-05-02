import os

from src.configurations.config import Config

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_file = os.path.join((parent_dir), "configurations", "config.json")


def load_data():
    config = Config(config_file)
    data_path = config.data_path
    # Load data here
    return data_path
