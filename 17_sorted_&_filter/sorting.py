print(1 < 2)
print('A' < 'Z')


def key_func(x):
    return abs(x)

data = [-10, -6, 0 , 3, 6]

print(sorted(data))
print([key_func(n) for n in data])

print(sorted(data, key=key_func))

print(sorted([2, -2, -1, 1], key=key_func))

print(sorted(data, key=lambda x: abs(x)))
print(sorted(data, key=abs))
print(sorted(data, key=abs, reverse=True))

data = [
    {'date': '2020-04-09', 'symbol': 'AAPL', 'open': 268.70, 'high': 270.04, 'low': 264.70, 'close': 267.99},
    {'date': '2020-04-09', 'symbol': 'MSFT', 'open': 166.36, 'high': 167.37, 'low': 163.33, 'close': 165.14},
    {'date': '2020-04-09', 'symbol': 'AMZN', 'open': 2_044.30, 'high': 2_053.00, 'low': 2_017.66, 'close': 2_042.76},
    {'date': '2020-04-09', 'symbol': 'FB', 'open': 175.90, 'high': 177.08, 'low': 171.57, 'close': 175.19}
]

print(sorted(data, key=lambda d: d['symbol'], reverse=True))
print('-----------' * 5)
print(sorted(data, key=lambda d: d['close'] - d['open']/ d['open']))

data = ['A', 'a', 'B', 'b', 'D', 'd','C', 'c']
print(sorted(data))
print(sorted(data, key=lambda x: x.casefold()))