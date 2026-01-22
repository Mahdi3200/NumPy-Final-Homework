import numpy as np

print("====== 1) Array Creation ======")

# 1-1: آرایه از 1 تا 50
arr1 = np.arange(1, 51)
print("Array 1 to 50:\n", arr1)

# 1-2: مضرب‌های 3 بین 3 تا 60
arr2 = np.arange(3, 61, 3)
print("Multiples of 3 (3 to 60):\n", arr2)

# 1-3: آرایه 6x6 پر از عدد 5
arr3 = np.full((6, 6), 5)
print("6x6 filled with 5:\n", arr3)


print("\n====== 2) Shape & Reshape ======")

# 2-1: آرایه از 1 تا 24
arr4 = np.arange(1, 25)
print("Array 1 to 24:\n", arr4)

# 2-2: shape و size
print("Shape:", arr4.shape)
print("Size:", arr4.size)

# 2-3: reshape به 4x6
arr4_reshaped = arr4.reshape(4, 6)
print("Reshaped 4x6:\n", arr4_reshaped)


print("\n====== 3) Indexing & Boolean Masking ======")

# آرایه 1 تا 40
arr5 = np.arange(1, 41)
print("Array 1 to 40:\n", arr5)

# 3-1: بزرگتر از 20
greater_than_20 = arr5[arr5 > 20]
print("Numbers > 20:\n", greater_than_20)

# 3-2: تقسیم پذیر بر 4
div_by_4 = arr5[arr5 % 4 == 0]
print("Numbers divisible by 4:\n", div_by_4)

# 3-3: جایگزینی اعداد فرد با 0
arr5_updated = arr5.copy()
arr5_updated[arr5_updated % 2 == 1] = 0
print("Odd numbers replaced with 0:\n", arr5_updated)


print("\n====== 4) Broadcasting & Operations ======")

# 4-1: آرایه 3x4 از 1 تا 12
arr6 = np.arange(1, 13).reshape(3, 4)
print("3x4 array (1 to 12):\n", arr6)

# 4-2: اضافه کردن 10 به همه عناصر
add_10 = arr6 + 10
print("Add 10:\n", add_10)

# 4-3: ضرب همه عناصر در 2
mul_2 = arr6 * 2
print("Multiply by 2:\n", mul_2)


print("\n====== 5) NumPy Functions ======")

arr7 = np.array([10, 20, 30, 40, 50])
print("Array:", arr7)

# 5-1: min, max, mean, sum
print("Min:", np.min(arr7))
print("Max:", np.max(arr7))
print("Mean:", np.mean(arr7))
print("Sum:", np.sum(arr7))

# 5-2: where برای جایگزینی > 30 با 999
arr7_where = np.where(arr7 > 30, 999, arr7)
print("Where (>30 -> 999):\n", arr7_where)

# 5-3: clip برای محدود کردن بین 15 تا 45
arr7_clip = np.clip(arr7, 15, 45)
print("Clipped (15 to 45):\n", arr7_clip)


print("\n====== 6) Mini Data Exercise ======")

scores = np.array([45, 60, 75, 90, 30, 85])
print("Scores:", scores)

# 6-1: میانگین
avg_score = np.mean(scores)
print("Average score:", avg_score)

# 6-2: تعداد نمره‌های >= 60
count_ge_60 = np.sum(scores >= 60)
print("Count of scores >= 60:", count_ge_60)

# 6-3: جایگزینی نمره‌های زیر 60 با 60
scores_updated = np.where(scores < 60, 60, scores)
print("Scores below 60 replaced with 60:\n", scores_updated)
