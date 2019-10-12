from time import perf_counter
l = [i for i in range(10000)]
start = perf_counter()
for _ in range(1000000):
  len(l)
print(perf_counter() - start)
