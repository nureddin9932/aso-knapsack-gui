import numpy as np

def update_positions(population, velocities, best_position, w=0.5, c1=1.5, c2=1.5):
    """
    تحديث مواقع وسرعات الذرات (الحلول) في خوارزمية التحسين.
    
    يقوم هذا الدالة بتحديث السرعات بناءً على وزن العزم (w)،
    والمعاملات المعتمدة على أفضل حل تم إيجاده (c1 و c2)،
    ثم تحديث المواقع (الحلول) بناءً على السرعات الجديدة.

    Update positions and velocities of particles (solutions) in the optimization algorithm.
    
    This function updates velocities using inertia weight (w),
    cognitive and social coefficients (c1, c2) based on the best found position,
    and then updates the positions accordingly.
    """
    r1, r2 = np.random.rand(2)  # أعداد عشوائية بين 0 و 1
    velocities = w * velocities + c1 * r1 * (best_position - population) + c2 * r2 * (best_position - population)
    population = population + velocities
    return population, velocities
