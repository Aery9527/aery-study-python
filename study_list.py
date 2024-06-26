"""
- list  : `[1, 2, 3]`, 可變且可存放異質物件, 類似 `List<Object>` 概念
"""

TITLE = """
========================================================================
{0:^64s}
========================================================================"""
RESULT = ">>>"

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(TITLE.format("list get"))
print(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9])
print(list[-0], list[-1], list[-2], list[-3], list[-4], list[-5], list[-6], list[-7], list[-8], list[-9])

print(TITLE.format("串列解包, 數量要相同, 否則會報錯"))
a, b, c, d, e, f, g, h, i, j = list
print(a, b, c, d, e, f, g, h, i, j)

print(TITLE.format("slice, [start:stop:step]"))
showFormat = "{0:<16s} {1} {2}"
print(showFormat.format("list[1:]", RESULT, list[1:]))  # 從 1 開始 到最後一個
print(showFormat.format("list[2:]", RESULT, list[2:]))  # 從 2 開始 到最後一個
print(showFormat.format("list[2:-1]", RESULT, list[2:-1]))  # 從 2 開始 到倒數第2個
print(showFormat.format("list[2:-0]", RESULT, list[2:-0]))  # 從 2 開始 0, index 錯誤會回復空list
print(showFormat.format("list[2:0]", RESULT, list[2:0]))  # 從 2 開始 0, index 錯誤會回復空list
print(showFormat.format("list[2:2]", RESULT, list[2:2]))  # 從 2 開始 到 2, index 錯誤會回復空list
print(showFormat.format("list[2:4]", RESULT, list[2:5]))  # 從 2 開始 到 4
print(showFormat.format("list[:4]", RESULT, list[:4]))  # 從 0 開始 到 4
print(showFormat.format("list[:-4]", RESULT, list[:-4]))  # 從 0 開始 到 -4
print(showFormat.format("list[-4:]", RESULT, list[-4:]))  # 從 -4 開始 到最後一個
print(showFormat.format("list[::2]", RESULT, list[::2]))  # 間隔 2
print(showFormat.format("list[::-1]", RESULT, list[::-1]))  # 反轉
print(showFormat.format("list[-2:-6:-1]", RESULT, list[-2:-6:-1]))  # 從 -2 開始 到 -6
print(showFormat.format("list[2:6:-1]", RESULT, list[2:6:-1]))  # index 錯誤會回復空list
print(showFormat.format("list[2:6][::-1]", RESULT, list[2:6][::-1]))  # 因為回傳是一個list, 因此可以直接[]再操作

print(TITLE.format("複製串列, 每個透過slice回傳的的list都是新的"))
list1 = list[:]  # 複製串列
list2 = list1[:]  # 複製串列
list2[0] = 9
print(showFormat.format("list1", RESULT, list1))
print(showFormat.format("list2", RESULT, list2))

print(TITLE.format("list 包含的方法"))
list1Dir = dir(list)
public_attributes = [attr for attr in list1Dir if not attr.startswith('_')]
print(public_attributes)
