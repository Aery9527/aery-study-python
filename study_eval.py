TITLE = """
========================================================================
{0:^64s}
========================================================================"""
RESULT = ">>>"

print(TITLE.format("一般使用"))
x = eval("3 + 5")
print('eval("3 + 5")', RESULT, x)

y = eval("x + 5")
print('eval("x + 5")', RESULT, y)

print(TITLE.format("使用自定義全局命名空間"))
global_namespace = {'x': 1, 'y': 2}
z = eval("x + y", global_namespace)
print('eval("x + y", global_namespace)', RESULT, z)

# 可使用 AST 來過濾危險的 eval
