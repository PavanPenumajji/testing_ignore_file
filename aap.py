import os
import json

def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

def print_env_vars():
    print("Environment Variables:")
    print(f"DB_HOST: {os.getenv('DB_HOST')}")
    print(f"DB_USER: {os.getenv('DB_USER')}")
    print(f"SECRET_KEY: {os.getenv('SECRET_KEY')}")

if __name__ == "__main__":
    config = load_config()
    print("Config JSON loaded:")
    print(config)
    print_env_vars()
