def calc_item(price, count):
    return price * count


items = [{"price": 100, "count": 3},
         {"price": 200, "count": 2},
         {"price": 300, "count": 1}]
total = 0
for item in items:
    total += calc_item(**item)
print(f"{total:,}")
