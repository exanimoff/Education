def ways_counter(n):
    results = {}

    def count_ways(n, results):
        if n in results:
            return results[n]
        if n <= 2:
            return 1
        ways = count_ways(n - 1, results) + count_ways(n - 2, results)
        results[n] = ways
        return ways

    return count_ways(n, results)

n = 5
result = ways_counter(n)
print(f"Количество путей к {n} ступеньке: {result}")
