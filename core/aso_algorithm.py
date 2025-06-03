import numpy as np
from core.objective_function import knapsack_function

def atom_search_optimization_knapsack(pop_size, dimensions, lower_bound, upper_bound, max_iter, weights, profits, capacity):
    """
    دالة تحسين باستخدام خوارزمية البحث الذري (ASO) لمشكلة الحقيبة (Knapsack Problem)
    """
    # تهيئة السكان (الذرات) بشكل عشوائي ضمن الحدود المحددة
    population = np.random.uniform(low=lower_bound, high=upper_bound, size=(pop_size, dimensions))

    # أفضل موقع (حل) تم إيجاده حتى الآن
    best_position = np.zeros(dimensions)
    best_score = 0

    # تهيئة مصفوفة الدرجات (قيمة الحلول لكل ذرة)
    scores = np.zeros(pop_size)

    # بدء تكرار الخوارزمية حتى الحد الأقصى للتكرارات
    for iter in range(max_iter):
        for i in range(pop_size):
            # تقييم جودة كل ذرة (الحل) باستخدام دالة الهدف
            scores[i] = knapsack_function(population[i], weights, profits, capacity)
            
            # تحديث أفضل حل إذا تم إيجاد حل أفضل
            if scores[i] > best_score:
                best_score = scores[i]
                best_position = population[i]

        # تحديث مواقع الذرات بناءً على قواعد خوارزمية ASO (هنا تحديث مبسط)
        for i in range(pop_size):
            # تحديث موضع الذرة عن طريق إضافة تغير عشوائي موجه بناءً على الفرق بين أفضل حل وحل الحالي
            population[i] += np.random.randn(dimensions) * (best_score - scores[i])

            # التأكد من بقاء قيم الذرات ضمن الحدود المعطاة
            population[i] = np.clip(population[i], lower_bound, upper_bound)

    return best_position, best_score
