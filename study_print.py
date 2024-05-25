import math

RESULT = ">>>"

print("\n### sep end")
print("a", "b", "c", end="|")  # end是結尾符號
print("a", "b", "c", sep=":")  # sep是分隔符號
print("a", "b", "c", sep=":", end="\n")
print("a", "b", "c", end="\n", sep=":")

print("\n### %s %d %f %o %x|%X %e|%E")
s = "python"
i = 13.2
o = 13
x = 13
e = 1234567890
print("|%s|       %", s, RESULT, "|%s|" % i)  # s可以帶入數字
print("|%s|       %", s, RESULT, "|%s|" % s)
print("|%10s|     %", s, RESULT, "|%10s|" % s)
print("|%-10s|    %", s, RESULT, "|%-10s|" % s)
print("|%10.3s|   %", s, RESULT, "|%10.3s|" % s)
print("|%-10.3s|  %", s, RESULT, "|%-10.3s|" % s)
# print("|%d|       %", i, RESULT, "|%d|" % s)  # d不能帶入字串
print("|%d|       %", i, RESULT, "|%d|" % i)
print("|%6d|      %", i, RESULT, "|%6d|" % i)
print("|%-6d|     %", i, RESULT, "|%-6d|" % i)
print("|%06d|     %", i, RESULT, "|%06d|" % i)
print("|%-06d|    %", i, RESULT, "|%-06d|" % i)
print("|%6.2f|    %", i, RESULT, "|%6.2f|" % i)
print("|%-6.2f|   %", i, RESULT, "|%-6.2f|" % i)
print("|%06.2f|   %", i, RESULT, "|%06.2f|" % i)
print("|%-06.2f|  %", i, RESULT, "|%-06.2f|" % i)
# print("|%o|       %", i, RESULT, "|%o|" % i)  # o不能帶入浮點數
print("|%o|       %", o, RESULT, "|%o|" % o)
print("|%6o|      %", o, RESULT, "|%6o|" % o)
print("|%-6o|     %", o, RESULT, "|%-6o|" % o)
print("|%06o|     %", o, RESULT, "|%06o|" % o)
print("|%-06o|    %", o, RESULT, "|%-06o|" % o)
print("|%6.1o|    %", o, RESULT, "|%6.1o|" % o)
print("|%-6.1o|   %", o, RESULT, "|%-6.1o|" % o)
print("|%06.1o|   %", o, RESULT, "|%06.1o|" % o)
print("|%-06.1o|  %", o, RESULT, "|%-06.1o|" % o)
# print("|%x|       %", x, RESULT, "|%x|" % i)  # x不能帶入浮點數
print("|%x|       %", x, RESULT, "|%x|" % x)
print("|%6x|      %", x, RESULT, "|%6x|" % x)
print("|%-6x|     %", x, RESULT, "|%-6x|" % x)
print("|%06x|     %", x, RESULT, "|%06x|" % x)
print("|%-06x|    %", x, RESULT, "|%-06x|" % x)
print("|%6.1x|    %", x, RESULT, "|%6.1x|" % x)
print("|%-6.1x|   %", x, RESULT, "|%-6.1x|" % x)
print("|%06.1x|   %", x, RESULT, "|%06.1x|" % x)
print("|%-06.1x|  %", x, RESULT, "|%-06.1x|" % x)
print("|%e|       %", e, RESULT, "|%e|" % e)  # 使用%E是大寫
print("|%4e|      %", e, RESULT, "|%4e|" % e)
print("|%16e|     %", e, RESULT, "|%16e|" % e)
print("|%-16e|    %", e, RESULT, "|%-16e|" % e)
print("|%016e|    %", e, RESULT, "|%016e|" % e)
print("|%-016e|   %", e, RESULT, "|%-016e|" % e)
print("|%16.4e|   %", e, RESULT, "|%16.4e|" % e)
print("|%-16.4e|  %", e, RESULT, "|%-16.4e|" % e)
print("|%016.4e|  %", e, RESULT, "|%016.4e|" % e)
print("|%-016.4e| %", e, RESULT, "|%-016.4e|" % e)

print("\n### {} format")
var1 = "Aery"
var2 = 55.66
print('"{}|{}|".format("kerker", 9527)                              ', RESULT, "{}|{}|".format("kerker", 9527))
print('"{1}|{0}|".format("kerker", 9527)                            ', RESULT, "{1}|{0}|".format("kerker", 9527))
print('"{0:8s}|{1:8d}|".format("kerker", 9527)                      ', RESULT,
      "{0:8s}|{1:8d}|".format("kerker", 9527))  # 使用格式化時一定要有index, 且不需要%
print('"{0:<8s}|{1:^8d}|{2:>10.3f}|".format("kerker", 9527, math.pi)', RESULT,
      "{0:<8s}|{1:^8d}|{2:>10.3f}|".format("kerker", 9527, math.pi))  # <靠左 ^置中 >靠右
print('"{0:*>7s}|{1:_^7s}|{2:@<7s}".format("好帥", "超帥", "爆帥")    ', RESULT,
      "{0:*>7s}|{1:_^7s}|{2:@<7s}".format("好帥", "超帥", "爆帥"))  # 填充自元
print('f"{var1}|{var2}|"        ', RESULT, f"{var1}|{var2}|")  # f-string, 可以搭配:後面的格式化
print('f"{var1=}|{var2=}|"      ', RESULT, f"{var1=}|{var2=}|")  # f-string, 直接顯示變數
print('f"{var1=:8s}|{var2=:8f}|"', RESULT, f"{var1=:8s}|{var2=:8f}|")
