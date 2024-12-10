from fair_sharer import fair_sharer as fs

def test_fair_sharer_case_1():
    test_1 = fs([0, 1000, 800, 0], 1)
    print(f"Test 1: {test_1}")
    expected_1 = [100.0, 800.0, 900.0, 0.0]
    assert test_1 == expected_1, f"Test 1 fehlgeschlagen: {test_1}"

def test_fair_sharer_case_2():
    test_2 = fs([0, 1000, 800, 0], 2)
    print(f"Test 2: {test_2}")
    expected_2 = [100.0, 890.0, 720.0, 90.0]
    assert test_2 == expected_2, f"Test 2 fehlgeschlagen: {test_2}"