import pytest
from core.aso_algorithm import atom_search_optimization
from core.objective_function import sphere_function

def test_knapsack():
    """
    اختبار لوظيفة تحسين Knapsack باستخدام خوارزمية Atom Search Optimization (ASO).
    
    يقوم هذا الاختبار بتشغيل خوارزمية ASO على مشكلة مع معلمات محددة،
    ويتحقق من أن النتيجة (أفضل نتيجة تم الحصول عليها) أقل من قيمة معينة (500).
    
    Test for the Knapsack optimization function using Atom Search Optimization (ASO).
    
    This test runs the ASO algorithm on a problem with specific parameters,
    and asserts that the best score found is less than 500.
    """
    # إعدادات اختبار Knapsack
    best_position, best_score = atom_search_optimization(30, 10, -5, 5, 100)
    
    # التحقق من أن أفضل نتيجة أقل من 500
    assert best_score < 500, f"Expected a score less than 500, but got {best_score}"
