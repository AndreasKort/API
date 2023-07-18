# Importieren Sie das python-binance-Paket
from binance.client import Client

# Richten Sie den Client mit API-Schlüsseln ein
client = Client(API_KEY_1, Secret_Key)

# Holen Sie historische Marktdaten für das BTC/USDT-Paar ab
btc_usdt_klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1. Januar 2020", "25. Juni 2023")

# Holen Sie historische Marktdaten für das BTC/EUR-Paar ab
btc_eur_klines = client.get_historical_klines("BTCEUR", Client.KLINE_INTERVAL_1DAY, "1. Januar 2020", "25. Juni 2023")

# Holen Sie historische Marktdaten für das EUR/USDT-Paar ab
eur_usdt_klines = client.get_historical_klines("EURUSDT", Client.KLINE_INTERVAL_1DAY, "1. Januar 2020", "25. Juni 2023")

# Drucken Sie die abgerufenen Daten
print(btc_usdt_klines)
print(btc_eur_klines)
print(eur_usdt_klines)