from exercise2.currency import Currency


def main():
    currency = Currency("EUR")

    for d in [1, 5, 2, 10, 0.5]:
        currency.add_denomination(d)
    print(currency.min_denomination())
    print(currency.max_denomination())

    currency.add_change("USD", 1.22)
    print(currency.get_change("USD"))


if __name__ == '__main__':
    main()
