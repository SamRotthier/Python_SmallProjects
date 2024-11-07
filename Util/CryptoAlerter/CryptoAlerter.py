import time
try:
    from .CryptoData import get_coins, Coin  # Relative import for package execution
except ImportError:
    from CryptoData import get_coins, Coin   # Direct execution

def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    """Creates an alert for the given price range of a coin"""

    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                # Add the code you want to be executed if a coin reaches
                print(coin, '!!TRIGGERED!!')
            else:
                print(coin)

def main_run_cryptoAlerter():
    coins: list[Coin] = get_coins()

    # A loop for these to create live alerts
    while True:
        time.sleep(5)
        alert('btc', bottom=20_000, top=28_000, coins_list=coins)
        alert('eth', bottom=1800, top=1900, coins_list=coins)
        alert('xrp', bottom=0.47, top=0.48, coins_list=coins)

if __name__ == '__main__':
    main_run_cryptoAlerter()