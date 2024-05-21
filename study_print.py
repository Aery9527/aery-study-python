RESULT = ">>>"

print("\n### sep end ###")
print("a", "b", "c", end="|")  # end是結尾符號
print("a", "b", "c", sep=":")  # sep是分隔符號
print("a", "b", "c", sep=":", end="\n")
print("a", "b", "c", end="\n", sep=":")

print("\n### %s %d %f %o %x|%X %e|%E ###")
print("Hello, %s" % "world")
print("%3d + %d = %d" % (10, 0.2, 10 + 0.2))
print("%3d + %f = %f" % (10, 0.2, 10 + 0.2))
print("%03d + %5.2f = %.4f" % (10, 0.2, 10 + 0.2))
print("%o" % 10)  # 8進位
print("%x, %X" % (10, 10))  # 16進位
print("%e, %E" % (1_000_000, 0.000_001))  # 科學記號
