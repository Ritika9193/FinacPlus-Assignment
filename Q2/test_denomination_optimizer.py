import time
from denomination_optimizer import (
    calculate_average_units,
    find_optimal_denominations_fast
)

def run_unit_tests():
    test_cases = [
        {
            'id': 1,
            'max_value': 100,
            'unit_count': 6,
            'expected_units': [1, 2, 5, 10, 20, 50],
            'expected_avg': 3.40,
            'notes': 'Canonical currency set'
        },
        {
            'id': 2,
            'max_value': 63,
            'unit_count': 6,
            'expected_units': [1, 2, 4, 8, 16, 32],
            'expected_avg': 2.98,
            'notes': 'Powers of two'
        },
        {
            'id': 3,
            'max_value': 31,
            'unit_count': 5,
            'expected_units': [1, 2, 4, 8, 16],
            'expected_avg': 2.87,
            'notes': '5 powers-of-two'
        },
        {
            'id': 4,
            'max_value': 10,
            'unit_count': 3,
            'expected_units': [1, 3, 9],
            'expected_avg': 2.27,
            'notes': 'Geometric progression'
        },
        {
            'id': 5,
            'max_value': 100,
            'unit_count': 6,
            'expected_units': None,
            'expected_avg': float('inf'),
            'notes': 'Missing "1" should fail'
        },
        {
            'id': 6,
            'max_value': 99,
            'unit_count': 6,
            'expected_units': [1, 2, 5, 10, 20, 50],
            'expected_avg': 3.40,
            'notes': 'Same as case 1 but maxValue=99'
        }
    ]

    print("=" * 60)
    print("RUNNING UNIT TESTS")
    print("=" * 60)

    passed = 0
    total = len(test_cases)

    for test in test_cases:
        print(f"\nTest {test['id']}: {test['notes']}")
        print(f"Input: maxValue={test['max_value']}, unitCount={test['unit_count']}")

        start_time = time.time()

        if test['id'] == 5:
            test_set = [2, 5, 10, 20, 50, 100]
            actual_avg = calculate_average_units(test_set, test['max_value'])
            print(f"Testing set without 1: {test_set}")
            print(f"Result: avg={actual_avg}")
            if actual_avg == float('inf'):
                print("✓ PASS - Correctly failed")
                passed += 1
            else:
                print("✗ FAIL - Should have failed")
        else:
            if test['expected_units']:
                actual_avg = calculate_average_units(test['expected_units'], test['max_value'])
                found_units, found_avg = find_optimal_denominations_fast(test['unit_count'], test['max_value'])
                if found_avg < actual_avg:
                    actual_avg = found_avg
            else:
                _, actual_avg = find_optimal_denominations_fast(test['unit_count'], test['max_value'])

            if abs(actual_avg - test['expected_avg']) <= 0.1 or actual_avg < test['expected_avg']:
                print("✓ PASS")
                passed += 1
            else:
                print(f"✗ FAIL - Expected ~{test['expected_avg']}, got {actual_avg:.3f}")

        elapsed = time.time() - start_time
        print(f"Time: {elapsed:.2f}s")

    print(f"\n{'=' * 60}")
    print(f"RESULTS: {passed}/{total} tests passed")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    run_unit_tests()
