import time
import random
from strategy import DoubleCashStrategy
from data import add_result

strategy = DoubleCashStrategy()

balance = 10000
base_bet = 100

print("Bot Double Cash démarré...")

while True:
    # Simulation d’un multiplicateur
    multiplier = round(random.uniform(1.0, 5.0), 2)

    add_result(multiplier)

    signal = strategy.signal()

    print(f"Résultat: x{multiplier} | Signal: {signal}")

    if signal == "PLAY":
        gain = base_bet * multiplier
        balance += gain - base_bet
        print(f"Mise gagnée → Balance: {balance}")
    else:
        print("Aucune mise")

    time.sleep(3)