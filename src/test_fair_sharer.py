from fair_sharer import fair_sharer as fs

def run_fair_sharer_tests():
    test_1 = fs([0, 1000, 800, 0], 1)
    print(f"Test 1: {test_1}")

    print("\n")

    test_2 = fs([0, 1000, 800, 0], 2)
    print(f"Test 2: {test_2}")

    return test_1, test_2

def test_fair_sharer():
    test_1, test_2 = run_fair_sharer_tests()

    assert test_1 == [100, 1000, 800, 0], f"Test 1 fehlgeschlagen: {test_1}"
    assert test_2 == [100, 1000, 800, 0], f"Test 2 fehlgeschlagen: {test_2}"