import numpy as np

def threshold(x, threshold_value=0.5):
    """
    دالة لتحويل القيم المستمرة إلى 0 أو 1 باستخدام العتبة.
    This function converts continuous values to binary (0 or 1) based on a threshold.
    """
    x = np.asarray(x)  # تأكد من أن x هي مصفوفة NumPy
    return np.where(x > threshold_value, 1, 0)

def knapsack_function(x, weights, profits, capacity):
    """
    دالة الهدف لمشكلة Knapsack التي تحسب الربح الإجمالي بناءً على الاختيارات
    وتحسب الوزن والربح الإجمالي، مع فرض عقوبة إذا تجاوز الوزن السعة.
    
    Objective function for the Knapsack problem that calculates total profit based on selections,
    checks total weight, and applies a penalty if the capacity is exceeded.
    """
    # تأكد من أن x و weights و profits جميعها مصفوفات بنفس الحجم
    x = np.asarray(x)  # تأكد من أن x هي مصفوفة NumPy
    weights = np.asarray(weights)
    profits = np.asarray(profits)

    # تحقق من أن جميع المصفوفات بنفس الحجم
    if x.shape != weights.shape or x.shape != profits.shape:
        raise ValueError("أحجام المصفوفات غير متوافقة! Sizes of input arrays do not match!")

    # تحويل القيم المستمرة إلى 0 أو 1 باستخدام العتبة
    x = threshold(x)  
    
    # حساب إجمالي الوزن والربح باستخدام الضرب الداخلي لتحسين الأداء
    total_weight = np.dot(x, weights)
    total_profit = np.dot(x, profits)
    
    # إذا تجاوز الوزن السعة المحددة، نقوم بفرض عقوبة (0 ربح)
    if total_weight > capacity:
        return 0  # Penalty if capacity exceeded
    
    return total_profit  # العودة بالربح الإجمالي إذا لم يتجاوز الوزن السعة
