import schedule, requests, sqlite3

def greeting():

    response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    btc_price = f"BTC: {round(data.get('btc_usd').get('last'), 2)}$\n"
    price_btc = {round(data.get('btc_usd').get('last'), 2)}
    print(price_btc)
    print(btc_price)

    createSQL = """CREATE TABLE IF NOT EXISTS btc_price (id INTEGER PRIMARY KEY AUTOINCREMENT, price TEXT, date DATETIME DEFAULT CURRENT_TIMESTAMP)"""

    conn = sqlite3.connect("DB.db")

    cursor = conn.cursor()
    cursor.execute(createSQL)

    cursor.execute("""INSERT INTO btc_price (price) values (?)""", [btc_price])

    conn.commit()


def main():
    # Кожні 3 год дістається інформація з сайту та записується у БД
    # Команда нижче записує кожні 30сек, вона допоможе для перевірки дз, щоб було швидше
    #schedule.every(30).seconds.do(greeting)
    #schedule.every(3).hours.do(greeting)

    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()