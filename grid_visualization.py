# البيانات: (x, char, y)
data = [
    (0, '█', 0),
    (0, '█', 1),
    (0, '█', 2),
    (1, '▀', 1),
    (1, '▀', 2),
    (2, '▀', 1),
    (2, '▀', 2),
    (3, '▀', 2),
]

# نحدد حجم الشبكة
max_x = max(x for x, _, _ in data)
max_y = max(y for _, _, y in data)

# نعمل مصفوفة فارغة
grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

# نحط الحروف في أماكنها
for x, char, y in data:
    grid[y][x] = char

# نطبع الشكل من أعلى لأسفل
for row in reversed(grid):
    print("".join(row))