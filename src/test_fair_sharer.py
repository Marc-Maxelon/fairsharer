from src.fair_sharer import fair_sharer as fs

test_1 = fs([0, 1000, 800, 0], 1)
print(f"{test_1}")

print("\n")

test_2 = fs([0, 1000, 800, 0], 2)
print(f"{test_2}")