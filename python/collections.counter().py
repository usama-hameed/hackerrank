from collections import Counter


def calculate_price(shoe_count, customer_requirements):
    total_earning = 0
    for shoe, price in customer_requirements:
        if shoe_count[shoe] > 0:
            total_earning += price
            shoe_count[shoe] -= 1
    return total_earning


n = int(input())

numbers = list(map(int, input().split()))

q = int(input())

customer_requirements = []
for _ in range(q):
    key, value = map(int, input().split())
    customer_requirements.append((key, value))


shoe_count = Counter(numbers)

print(calculate_price(shoe_count, customer_requirements))
