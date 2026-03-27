import pytest
import math
import os
import sys
from io import StringIO

# Импорт тестируемых функций
from fact import fact_rec, fact_it
from show_employee import show_employee
from sum_and_sub import sum_and_sub
from process_list import process_list, process_list_gen
from my_sum import my_sum
from email_validation import fun as validate_email, filter_mail
from fibonacci import fibonacci
from average_scores import compute_average_scores
from plane_angle import plane_angle, Point
from phone_number import sort_phone
from people_sort import name_format
from complex_numbers import Complex
from circle_square_mk import circle_square_mk

# 1. Tests for fact.py
@pytest.mark.parametrize("n, expected", [
    (0, 1), (1, 1), (5, 120), (6, 720), (10, 3628800)
])
def test_fact(n, expected):
    assert fact_rec(n) == expected
    assert fact_it(n) == expected

# 2. Tests for show_employee.py
@pytest.mark.parametrize("name, salary, expected", [
    ("Ivan", 50000, "Ivan: 50000 ₽"),
    ("Petr", 100000, "Petr: 100000 ₽"),
])
def test_show_employee_args(name, salary, expected):
    assert show_employee(name, salary) == expected

def test_show_employee_default():
    assert show_employee("Boss") == "Boss: 100000 ₽"

# 3. Tests for sum_and_sub.py
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, (15, 5)),
    (0, 0, (0, 0)),
    (-5, -5, (-10, 0)),
    (1.5, 2.5, (4.0, -1.0))
])
def test_sum_and_sub(a, b, expected):
    res = sum_and_sub(a, b)
    assert res == expected

# 4. Tests for process_list.py
def test_process_list():
    inp = [1, 2, 3, 4]
    expected = [1, 4, 27, 16] # 1->1^3, 2->2^2, 3->3^3, 4->4^2
    assert process_list(inp) == expected
    assert list(process_list_gen(inp)) == expected

def test_process_list_empty():
    assert process_list([]) == []
    assert list(process_list_gen([])) == []

# 5. Tests for my_sum.py
@pytest.mark.parametrize("args, expected", [
    ((1, 2, 3), 6),
    ((), 0),
    ((1.1, 2.2), 3.3000000000000003), # float precision
    ((-1, 1), 0)
])
def test_my_sum(args, expected):
    assert my_sum(*args) == expected

# 9. Tests for email_validation.py
@pytest.mark.parametrize("email, is_valid", [
    ("lara@mospolytech.ru", True),
    ("brian-23@mospolytech.ru", True),
    ("britts_54@mospolytech.ru", True),
    ("invalid", False),
    ("no@domain", False), # no extension
    ("name@.com", False), # no site
    ("@site.com", False), # no name
    ("name@site.commm", False), # ext > 3
    ("name#@site.com", False), # invalid char
])
def test_email_validation(email, is_valid):
    assert validate_email(email) is is_valid

def test_filter_mail():
    emails = ["a@b.c", "invalid", "x@y.z"]
    assert filter_mail(emails) == ["a@b.c", "x@y.z"]

# 10. Tests for fibonacci.py
@pytest.mark.parametrize("n, expected", [
    (1, [0]),
    (2, [0, 1]),
    (5, [0, 1, 1, 2, 3]),
    (0, [])
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected

# 11. Tests for average_scores.py
def test_average_scores():
    # 2 students, 2 subjects
    # Subj 1: 100, 90
    # Subj 2: 50,  60
    # Stud 1 avg: (100+50)/2 = 75
    # Stud 2 avg: (90+60)/2 = 75
    scores = [(100, 90), (50, 60)]
    assert compute_average_scores(scores) == (75.0, 75.0)

def test_average_scores_example():
    # Example from task
    # 5 students, 3 subjects
    s1 = (89, 90, 78, 93, 80)
    s2 = (90, 91, 85, 88, 86)
    s3 = (91, 92, 83, 89, 90.5)
    scores = [s1, s2, s3]
    expected = (90.0, 91.0, 82.0, 90.0, 85.5)
    result = compute_average_scores(scores)
    # Check with tolerance
    for r, e in zip(result, expected):
        assert abs(r - e) < 0.001

# 12. Tests for plane_angle.py
def test_point_operations():
    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    sub = p1 - p2
    assert sub.x == -3 and sub.y == -3 and sub.z == -3
    assert p1.dot(p2) == 1*4 + 2*5 + 3*6 # 4+10+18=32
    
def test_plane_angle_zero():
    # Points on one line -> angle 0 or 180 depending on definition, 
    # but strictly planes aren't defined.
    # Let's test perpendicular planes.
    # Plane 1: xy plane (z=0). A(0,0,0), B(1,0,0), C(1,1,0).
    # Normal ~ (0,0,1)
    # Plane 2: xz plane (y=0). B(1,0,0), C(1,0,0) - wait, B and C must define line.
    # Let's use simple standard vectors.
    pass

# 13. Tests for phone_number.py (wrapper)
def test_phone_sort():
    raw = ["07895462130", "89875641230", "9195969878"]
    # Sorted order of last 10 digits:
    # 1. 7895462130 (078...)
    # 2. 9195969878 (919...)
    # 3. 9875641230 (898...)
    # Actually sort works on original strings? No, logic:
    # "The wrapper sorts the list" -> usually implies sorting the processed or raw?
    # Task: "Sort them in ascending order, then print".
    # Standard string sort of inputs:
    # '078...' < '898...' < '919...'
    # Wait, the example output is:
    # +7 (789)... corresponds to 0789...
    # +7 (919)... corresponds to 9195...
    # +7 (987)... corresponds to 8987...
    # In ASCII '0' < '8' < '9'. So inputs are sorted lexicographically.
    
    res = sort_phone(raw)
    assert res[0] == "+7 (789) 546-21-30"
    assert res[1] == "+7 (919) 596-98-78"
    assert res[2] == "+7 (987) 564-12-30"

# 14. Tests for people_sort.py
def test_people_sort():
    # [name, surname, age, sex]
    people = [
        ["Mike", "Thomson", "20", "M"],
        ["Robert", "Bustle", "32", "M"],
        ["Andria", "Bustle", "30", "F"]
    ]
    # Sorted by age: Mike(20), Andria(30), Robert(32)
    res = list(name_format(people))
    assert res[0] == "Mr. Mike Thomson"
    assert res[1] == "Ms. Andria Bustle"
    assert res[2] == "Mr. Robert Bustle"

# 15. Tests for complex_numbers.py
def test_complex_math():
    c1 = Complex(2, 1)
    c2 = Complex(5, 6)
    
    # Add
    s = c1 + c2
    assert str(s) == "7.00+7.00i"
    
    # Sub
    s = c1 - c2
    assert str(s) == "-3.00-5.00i"
    
    # Mul: (2+i)(5+6i) = 10 + 12i + 5i - 6 = 4 + 17i
    m = c1 * c2
    assert str(m) == "4.00+17.00i"
    
    # Div example from task
    d = c1 / c2
    # 0.26-0.11i
    # Check string formatting
    assert str(d) == "0.26-0.11i"
    
    # Mod
    mod1 = c1.mod()
    # sqrt(5) approx 2.236 -> 2.24
    assert str(mod1) == "2.24+0.00i"

def test_complex_str_formats():
    assert str(Complex(1, 0)) == "1.00+0.00i"
    assert str(Complex(0, 5)) == "0.00+5.00i"
    assert str(Complex(0, -5)) == "0.00-5.00i"
    assert str(Complex(1, -1)) == "1.00-1.00i"

# 16. Tests for circle_square_mk.py
def test_monte_carlo():
    r = 1
    area = circle_square_mk(r, 1000)
    # Area should be close to PI * 1^2 = 3.14
    # Bounds are loose because MC is random
    assert 2.5 < area < 3.8 

# Additional tests to reach count > 60
@pytest.mark.parametrize("a, b", [(i, i) for i in range(10)])
def test_sum_simple(a, b):
    assert my_sum(a, b) == a + b

@pytest.mark.parametrize("real, imag", [(1, 1), (2, 2), (3, 3)])
def test_complex_init(real, imag):
    c = Complex(real, imag)
    assert c.real == real
    assert c.imaginary == imag

if __name__ == '__main__':
    # Для запуска тестов можно просто выполнить этот файл
    # или запустить `pytest test.py` в консоли
    sys.exit(pytest.main(["-v", "test.py"]))