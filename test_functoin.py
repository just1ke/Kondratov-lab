from functions import (
    sum_digits,
    average,
    normalize_text,
    select_numbers,
)
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert sum_digits(1000) == 1
assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
assert normalize_text("a\tb\nc") == "a b c"
base = [-5, 0, 2, 5]
assert select_numbers(base, 2) == [-5, 5]
assert select_numbers([], 2) == []
assert select_numbers([-2, 2, 3, -3], 2) == [3, -3]
assert select_numbers([1, 2, 3, -1, -2, -3], 2) == [3, -3]
assert select_numbers([-1, 0, 1], 0) == [-1, 1]
assert select_numbers([0, 0, 0], 0) == []
assert select_numbers([5, 5, 1, 5], 2) == [5, 5, 5]
original = [-5, 0, 2, 5]
copy_before = original.copy()
_ = select_numbers(original, 2)
assert original == copy_before
result = select_numbers(original, 2)
assert result is not original
print("Все проверки пройдены успешно")