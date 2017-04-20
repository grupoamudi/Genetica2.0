import genetic_lib

A = genetic_lib.individuo()

A.mutate()

A.save_bin("test.bin")

A.load_bin("test.bin")

print("==== Original data =====\n")
print(A.array)
