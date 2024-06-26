"""
使用雙引號多行註解
"""
'''
或者使用單引號多行註解
'''

TITLE = """
========================================================================
{0:^64s}
========================================================================"""
RESULT = ">>>"

print(TITLE.format("計算符號"))
print("True and False =", True and False)
print("True or  False =", True or False)
print("True ^   False =", True ^ False)  # XOR
print("not True       =", not True)
print("5    *  2      =", 5 * 2, type(5 * 2))
print("5.0  *  2      =", 5.0 * 2, type(5.0 * 2))
print("5    *  2.0    =", 5 * 2.0, type(5 * 2.0))
print("10   ** 2      =", 10 ** 2, type(10 ** 2), "# 次方")
print("10.0 ** 2      =", 10.0 ** 2, type(10.0 ** 2))
print("10   ** 2.0    =", 10 ** 2.0, type(10 ** 2.0))
print("10   /  2      =", 10 / 2, type(10 / 2), "# 除法結果一定是float")
print("10   // 4      =", 10 // 4, type(10 // 4), "# 餘數")
print("10.0 // 4      =", 10.0 // 4, type(10.0 // 4))
print("10   // 4.0    =", 10 // 4.0, type(10 // 4.0))
print("10   // 4.5    =", 10 // 4.5, type(10 // 4.5), "# same to math.floor() or int()")
print("10   // 5.1    =", 10 // 5.1, type(10 // 5.1), "# same to math.floor() or int()")

print(TITLE.format("雙引號(\") 單引號(') 互相嵌套可以不需要逃逸字元 (這部分跟js一樣)"))
print("'kerker' " + "9527")
print('"kerker" ' + str(9527))  # 字串與數字不能直接相加, 要透過str()轉換

print(TITLE.format("同時指定"))
a = b = c = 5
print("a = b = c = 5    ", RESULT, a, b, c)
a, b, c = 4, 5, 6
print("a, b, c = 4, 5, 6", RESULT, a, b, c)

print(TITLE.format("交換"))
a, b, c = b, c, a
print("a, b, c = b, c, a", RESULT, a, b, c, "# 交換")

print(TITLE.format("多行接續, 使用繼續符號(\\), 後面不可以接東西, 註解也不行"))
a = 1 \
    + 2 \
    + 3
b = (1  # 使用括弧接續就可以放註解在後面
     + 2
     + 3
     )
print("a", RESULT, a)
print("b", RESULT, b)
print("id(a)", RESULT, id(a), "# 記憶體位置")
print("id(b)", RESULT, id(b), "# 記憶體位置")

print(TITLE.format("匯入模組"))
import math

print("math.pi", RESULT, math.pi)

print(TITLE.format("查型態, python3之後無int/long/float/double限制, 所以基本上就是無限大"))
print("type(10)      ", RESULT, type(10))
print("type(10.0)    ", RESULT, type(10.0))
print("type('kerker')", RESULT, type('kerker'))
print("type(True)    ", RESULT, type(True))
print("type(False)   ", RESULT, type(False))
print("type(None)    ", RESULT, type(None))

print(TITLE.format("進制轉換"))
print("0b1010        ", RESULT, 0b1010, "# 二進制")
print("0o12          ", RESULT, 0o12, "# 八進制")
print("0xA           ", RESULT, 0x0A, "# 十六進制")
print("bin(10)       ", RESULT, bin(10), type(bin(10)), "# 轉二進制")
print("oct(10)       ", RESULT, oct(10), type(oct(10)), "# 轉八進制")
print("hex(10)       ", RESULT, hex(10), type(hex(10)), "# 轉十六進制")
print("int('1010', 2)", RESULT, int('1010', 2), "# 二進制轉十進制")
print("int('12', 8)  ", RESULT, int('12', 8), "# 八進制轉十進制")
print("int('A', 16)  ", RESULT, int('A', 16), "# 十六進制轉十進制")
print("int(10.5)     ", RESULT, int(10.5), "# 轉整數")
print("float(10)     ", RESULT, float(10), "# 轉浮點數")

print(TITLE.format("常用數學方法"))
print("abs(-10)        ", RESULT, abs(-10), "# 絕對值")
print("pow(10, 2)      ", RESULT, pow(10, 2), "# 次方")  # 同 ** 計算子
print("round(10.5)     ", RESULT, round(10.5), "# 四捨五+1入")  # Bankers' Rounding
print("round(10.51)    ", RESULT, round(10.51), "# 四捨五+1入")
print("round(1.055, 2) ", RESULT, round(1.055, 2), "# 四捨五+1入")
print("round(1.0551, 2)", RESULT, round(1.0551, 2), "# 四捨五+1入")

print(TITLE.format("科學記號, 一定是float"))
print("12345e-2", RESULT, 12345e-2)
print("123.45e2", RESULT, 123.45e2)

print(TITLE.format("boolean, 0或空資料為False, 其餘皆為True"))
print("bool(0.0)  ", RESULT, bool(0.0))
print("bool(0)    ", RESULT, bool(0))
print("bool(None) ", RESULT, bool(None))
print("bool('')   ", RESULT, bool(''), "# 空字串")
print("bool([])   ", RESULT, bool([]), "# 空串列")
print("bool(())   ", RESULT, bool(()), "# 空元組")
print("bool({})   ", RESULT, bool({}), "# 空字典")
print("bool(set())", RESULT, bool(set()), "# 空集合")
print("bool(-0.1) ", RESULT, bool(0.1))
print("bool(0.1)  ", RESULT, bool(0.1))
print("bool(1)    ", RESULT, bool(1))
print("int(True)  ", RESULT, int(True))
print("int(False) ", RESULT, int(False))

print(TITLE.format("字串"))
print("'*' * 4", RESULT, "*" * 4)
print("""這邊是\"\"\"多行字串
換行 \
接續非換行""")
print('''這邊是\'\'\'多行字串
換行 \
接續非換行''')
print(r"這邊是原始字串\t不會轉譯逃逸字元\n")

print(TITLE.format("ASCII, ord其實是Unicode"))
print("chr(97)      ", RESULT, chr(97))
print("ord('a')     ", RESULT, ord('a'))
print("ord('帥')     ", RESULT, ord('帥'))  # 10進制
print("hex(ord('帥'))", RESULT, hex(ord('帥')))  # 16進制

print(TITLE.format("exception handle"))
import sys

sys.stdout.flush()  # 先送出上面緩衝的訊息, 下面stderr才會在stdout之後

try:
    print("10 / 0", RESULT, 10 / 0)
except ZeroDivisionError as e:
    print("10 / 0", RESULT, e, file=sys.stderr)
