x = True
if x: print("x is True")

y = False
print("y is", "True" if y else "False")

z = 0
if z == 0:
    print(f"z({z}) is 0")
elif z == 1:
    print(f"z({z}) is 1")
else:
    print(f"z({z}) is other")

# if {VAR} := {value} 給值的同時判斷, since python 3.8
if a := 1:
    print(f"a is {a}")
if b := 1 > 0:
    print(f"b is {b}")
