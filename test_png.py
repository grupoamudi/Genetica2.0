import genetic_lib

A = genetic_lib.individuo()

A.mutate()

A.save_png("test.png")

# A.load_png("test.png")
# print("==== Original data =====\n")
# print(A.array)
