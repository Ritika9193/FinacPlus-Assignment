from special_cipher import specialCipher

def run_tests():
    print("=== BASIC TEST CASES ===")
    result1 = specialCipher("AABCCC", 3)
    print(f'Test 1: {result1} (Expected: D2EF3)')

    result2 = specialCipher("ABCD", 1)
    print(f'Test 2: {result2} (Expected: BCDE)')

    result3 = specialCipher("AAAA", 2)
    print(f'Test 3: {result3} (Expected: C4)')

    print("\n=== EDGE CASES ===")
    result4 = specialCipher("", 5)
    print(f'Test 4: {result4} (Expected: )')

    result5 = specialCipher("A", 10)
    print(f'Test 5: {result5} (Expected: K)')

    result6 = specialCipher("XYZ", 5)
    print(f'Test 6: {result6} (Expected: CDE)')

    result7 = specialCipher("ABC", 52)
    print(f'Test 7: {result7} (Expected: ABC)')

    result8 = specialCipher("DEF", -3)
    print(f'Test 8: {result8} (Expected: ABC)')

    print("\n=== COMPLEX CASES ===")
    result9 = specialCipher("AABBCCDDEE", 1)
    print(f'Test 9: {result9} (Expected: B2C2D2E2F2)')

    result10 = specialCipher("ABABAB", 25)
    print(f'Test 10: {result10} (Expected: ZAZAZA)')

    result11 = specialCipher("AAAAAAAAAA", 7)
    print(f'Test 11: {result11} (Expected: H10)')

    result12 = specialCipher("AABBCC", 0)
    print(f'Test 12: {result12} (Expected: A2B2C2)')

    print("\n=== ADDITIONAL EDGE CASES ===")
    result13 = specialCipher("ABC", -78)
    print(f'Test 13: {result13} (Expected: ABC)')

    result14 = specialCipher("ZZZZZZZZZZZZZZ", 1)
    print(f'Test 14: {result14} (Expected: A14)')

    result15 = specialCipher("ABCABC", 25)
    print(f'Test 15: {result15} (Expected: ZABZAB)')

    print("\n=== SUMMARY ===")
    test_results = [
        (result1, "D2EF3"),
        (result2, "BCDE"),
        (result3, "C4"),
        (result4, ""),
        (result5, "K"),
        (result6, "CDE"),
        (result7, "ABC"),
        (result8, "ABC"),
        (result9, "B2C2D2E2F2"),
        (result10, "ZAZAZA"),
        (result11, "H10"),
        (result12, "A2B2C2"),
        (result13, "ABC"),
        (result14, "A14"),
        (result15, "ZABZAB")
    ]
    passed = sum(1 for actual, expected in test_results if actual == expected)
    total = len(test_results)
    print(f"Tests passed: {passed}/{total}")

    if passed == total:
        print(" All tests passed!")
    else:
        print("Some tests failed. Check the output above.")
        for i, (actual, expected) in enumerate(test_results, 1):
            if actual != expected:
                print(f"  Test {i}: Got '{actual}', Expected '{expected}'")

if __name__ == "__main__":
    run_tests()
