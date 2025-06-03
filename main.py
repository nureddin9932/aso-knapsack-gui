import tkinter as tk
from tkinter import messagebox
import numpy as np
import time
import csv
import os

# دالة لتحويل القيم إلى 0 أو 1 باستخدام العتبة
def threshold(x, threshold_value=0.5):
    return np.where(x > threshold_value, 1, 0)

# دالة هدف لمشكلة Knapsack
def knapsack_function(x, weights, profits, capacity):
    x = threshold(np.array(x))
    total_weight = np.sum(x * weights)
    total_profit = np.sum(x * profits)

    if total_weight > capacity:
        return 0

    return total_profit

# خوارزمية ASO
def atom_search_optimization_knapsack(pop_size, dimensions, lower_bound, upper_bound, max_iter, weights, profits, capacity):
    population = np.random.uniform(lower_bound, upper_bound, (pop_size, dimensions))
    best_position = None
    best_score = float('-inf')

    start_time = time.time()

    for iter in range(max_iter):
        for i in range(pop_size):
            score = knapsack_function(population[i], weights, profits, capacity)

            if score > best_score:
                best_score = score
                best_position = population[i]

        population = np.random.uniform(lower_bound, upper_bound, (pop_size, dimensions))

    end_time = time.time()
    time_taken = end_time - start_time
    return best_position, best_score, time_taken

# دالة لقراءة بيانات Knapsack
def read_knapsack_data():
    weights = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
    profits = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
    capacity = 269
    return weights, profits, capacity

# دالة لحفظ النتائج في ملف CSV
def store_results_in_csv(problem, best_position, best_score, time_taken, population_size, max_iterations, weights, profits, capacity):
    if not os.path.exists('results'):
        os.makedirs('results')

    file_path = 'results/test_results.csv'
    file_exists = os.path.exists(file_path)

    if not file_exists:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "المشكلة", "أفضل موضع", "أفضل ربح", "الزمن المستغرق (ثانية)",
                "حجم السكان", "أقصى عدد تكرارات", "الأوزان", "الأرباح", "السعة"
            ])

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        best_position_list = best_position.tolist()
        writer.writerow([
            problem, best_position_list, best_score, time_taken,
            population_size, max_iterations, weights, profits, capacity
        ])

# الدالة عند الضغط على زر البدء
def run_knapsack_algorithm():
    try:
        pop_size = int(pop_size_entry.get())
        max_iter = int(max_iter_entry.get())

        weights, profits, capacity = read_knapsack_data()
        best_position, best_score, time_taken = atom_search_optimization_knapsack(
            pop_size, len(weights), 0, 1, max_iter, weights, profits, capacity
        )

        results_label.config(
            text=f"أفضل موضع: {best_position}\nأفضل ربح: {best_score}\nالزمن المستغرق: {time_taken:.4f} ثانية"
        )

        store_results_in_csv('Kp1', best_position, best_score, time_taken, pop_size, max_iter, weights, profits, capacity)

    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة للمعلمات.")

# واجهة المستخدم
root = tk.Tk()
root.title("تشغيل خوارزمية ASO")

tk.Label(root, text="حجم السكان:").pack()
pop_size_entry = tk.Entry(root)
pop_size_entry.pack()

tk.Label(root, text="أقصى عدد تكرارات:").pack()
max_iter_entry = tk.Entry(root)
max_iter_entry.pack()

run_button = tk.Button(root, text="ابدأ الخوارزمية", command=run_knapsack_algorithm)
run_button.pack()

results_label = tk.Label(root, text="", justify=tk.LEFT)
results_label.pack()

root.mainloop()
