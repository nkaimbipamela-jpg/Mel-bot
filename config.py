"""Configuration management for Mel-bot."""
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Config:
    """Bot configuration settings."""
    base_bet: int = 100
    max_loss: int = 5
    target_multiplier: float = 2.0
    martingale_enabled: bool = False
    initial_balance: int = 10000
    strategy_threshold: float = 2.0
    wait_time_seconds: float = 3
    headless_browser: bool = True

    @classmethod
    def load_from_file(cls, filepath: str = "config.json") -> "Config":
        """Load configuration from JSON file."""
        config_path = Path(filepath)
        
        if not config_path.exists():
            print(f"Config file {filepath} not found. Using defaults.")
            return cls()
        
        try:
            with open(config_path, "r") as f:
                data = json.load(f)
            return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading config: {e}. Using defaults.")
            return cls()

    def save_to_file(self, filepath: str = "config.json") -> None:
        """Save configuration to JSON file."""
        with open(filepath, "w") as f:
            json.dump(self.__dict__, f, indent=2)
