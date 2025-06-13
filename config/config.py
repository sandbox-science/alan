import yaml


def load_config():
    """
    Load the configuration file.
    """
    with open("config/config.yaml", "r") as f:
        cfg = yaml.safe_load(f)
    return cfg
