import pytest
from core.objective_function import sphere_function

def test_sphere_function():
    """
    اختبار دالة sphere_function للتحقق من صحتها.
    
    تقوم الدالة بحساب مجموع مربعات عناصر القائمة.
    المثال: 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
    
    Test for the sphere_function to verify correctness.
    
    The function calculates the sum of squares of the input list elements.
    Example: 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
    """
    x = [1, 2, 3, 4, 5]
    result = sphere_function(x)
    
    # التأكد أن الناتج يساوي 55
    assert result == 55, f"Expected 55, but got {result}"
