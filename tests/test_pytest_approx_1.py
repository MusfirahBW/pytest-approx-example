# Sample code for pytest approx

import pytest


def divide(a, b):
    return a / b


def test_exact_comparison():
    result = divide(1, 3)
    assert result == 0.3333333333333333  # Exact value


def test_approximate_comparison():
    result = divide(1, 3)
    assert result == pytest.approx(0.3333333333333333)  # Approximate value

@pytest.mark.xfail(reason="This test is currently expected to fail")
def test_approximation_failure():
    result = divide(1, 3)
    assert result == pytest.approx(0.333)  # This test will fail due to approximation


# if __name__ == "__main__":
#     pytest.main()
