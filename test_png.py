import genetic_lib

A = genetic_lib.individuo()

for x in range(10):
    A.mutate()

A.save_png("test.png")

A.array = []

A.load_png("test.png")

A.save_png("test_compare.png")
# print("==== Original data =====\n")
# print(A.array)
