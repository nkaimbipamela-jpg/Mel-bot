# Mel-bot: Double Cash Strategy Bot

A sophisticated betting bot that implements the Double Cash strategy with moving average analysis for the Melbet platform.

## Features

✨ **Core Features**
- Moving average-based trading signals
- Multiple strategy options (Double Cash, Conservative, Aggressive)
- Real-time balance tracking
- Configurable betting parameters
- Comprehensive logging system
- Type hints throughout codebase
- Browser automation support for Melbet

🎯 **Improvements in Latest Version**
- Fixed import issues (case-sensitive file names)
- Proper configuration management
- Enhanced data management with statistics
- Better error handling and logging
- Multiple strategy implementations
- Context manager for browser automation
- Detailed performance summaries

## Project Structure

```
Mel-bot/
├── main.py                 # Main bot execution
├── strategy.py            # Trading strategies
├── data.py               # Data management
├── config.py             # Configuration handling
├── browser.py            # Browser automation
├── logger_config.py      # Logging setup
├── config.json           # Configuration file
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── .gitignore           # Git ignore rules
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nkaimbipamela-jpg/Mel-bot.git
   cd Mel-bot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit `config.json` to customize bot behavior:

```json
{
  "base_bet": 100,              # Base bet amount per play
  "max_loss": 5,                # Max consecutive losses before stopping
  "target_multiplier": 2.0,     # Target multiplier
  "martingale_enabled": false,  # Enable martingale progression
  "initial_balance": 10000,     # Starting balance
  "strategy_threshold": 2.0,    # Average multiplier threshold
  "wait_time_seconds": 3,       # Wait between bets
  "headless_browser": true      # Run browser in headless mode
}
```

## Usage

### Run the Bot

```bash
python main.py
```

The bot will:
1. Load configuration from `config.json`
2. Start the simulation/live trading
3. Log all actions to console and `mel_bot.log`
4. Display performance summary at the end

### Example Output

```
⏸️ Step 1 | Multiplier: x2.34 | Average: 2.34 | Signal: WAIT | Action: WAIT | ➖ Profit: 0 | Balance: 10000
🎯 Step 2 | Multiplier: x2.45 | Average: 2.40 | Signal: PLAY | Action: BET | ✅ Profit: +145 | Balance: 10145
⏸️ Step 3 | Multiplier: x1.89 | Average: 2.23 | Signal: WAIT | Action: WAIT | ➖ Profit: 0 | Balance: 10145
```

## Strategies

### DoubleCashStrategy (Default)
- Uses 5-period moving average
- Plays when average > threshold (2.0)
- Good balance of risk and reward

### ConservativeStrategy
- Uses 10-period moving average
- Higher threshold (2.5)
- Fewer but more confident plays

### AggressiveStrategy
- Uses 3-period moving average
- Lower threshold (1.5)
- More frequent trading signals

### Usage Example

```python
from strategy import ConservativeStrategy
from data import get_last

strategy = ConservativeStrategy(threshold=2.5)
signal = strategy.signal()  # Returns "PLAY" or "WAIT"
```

## API Examples

### Data Management

```python
from data import add_result, get_last, get_manager

# Add a game result
add_result(2.45)

# Get last 10 results
last_results = get_last(10)

# Get statistics
manager = get_manager()
stats = manager.get_stats()
print(f"Average multiplier: {stats['average']}")
```

### Configuration

```python
from config import Config

# Load configuration
config = Config.load_from_file("config.json")

# Access settings
print(config.base_bet)
print(config.initial_balance)

# Create custom configuration
custom_config = Config(base_bet=50, initial_balance=5000)
custom_config.save_to_file("custom_config.json")
```

### Strategy

```python
from strategy import DoubleCashStrategy

strategy = DoubleCashStrategy(threshold=2.0, lookback_period=5)

# Get signal
signal = strategy.signal()  # "PLAY" or "WAIT"

# Get detailed information
info = strategy.get_signal_info()
print(f"Current average: {info['average']}")
print(f"Recent history: {info['history']}")
```

## Browser Automation (Future)

For live Melbet integration:

```python
from browser import MelbetBrowser

with MelbetBrowser(headless=False) as browser:
    browser.navigate_to_melbet()
    # Interact with Melbet
```

## Logging

All activities are logged to both console and `mel_bot.log`:

- **INFO**: General information and progress
- **WARNING**: Warnings (e.g., max losses reached)
- **ERROR**: Errors and exceptions

View logs:
```bash
tail -f mel_bot.log
```

## Performance Metrics

After each run, the bot displays:
- Initial and final balance
- Total profit/loss
- Number of plays and win rate
- Game statistics (min, max, average multiplier)
- Consecutive loss tracking

## Safety Features

⚠️ **Built-in Protections**
- Stops if balance < base bet
- Maximum consecutive losses limit
- Configuration validation
- Error handling and logging
- Keyboard interrupt support (Ctrl+C)

## Troubleshooting

### Import Errors
Ensure you're using the correct file names:
- `strategy.py` (not `Stratégie.py`)
- `data.py` (not `Data.py`)
- `requirements.txt` (not `Requirement.txt`)

### Chrome Driver Issues
```bash
pip install --upgrade webdriver-manager
```

### Configuration Not Loading
- Check `config.json` is valid JSON
- Ensure file is in same directory as `main.py`
- Check file permissions

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is provided as-is for educational purposes.

## Disclaimer

⚠️ **Important**: This bot is for educational purposes. Always:
- Test thoroughly before using with real money
- Use with caution on live trading platforms
- Understand the risks of automated trading
- Never risk more than you can afford to lose

## Support

For issues and questions, please open a GitHub issue.
