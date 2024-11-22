from exchanges.models import Exchange


def buy_from_exchange(symbol, quantity):
    print(f"Buying {quantity} {symbol}(s)")
    return True

def process_exchange(exchanges):
    exchanges.update(status=Exchange.ExchangeStatusChoice.DONE)