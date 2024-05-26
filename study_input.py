inputTitleFormat = "{0:6s} : "
outputTitleFormat = "{0:^10s} : "
outputNameFormat = outputTitleFormat + "{1}"
outputScoreFormat = outputTitleFormat + "{1:<3d}"

name = input(inputTitleFormat.format("姓名"))  # always return a string
math = input(inputTitleFormat.format("數學"))
english = input(inputTitleFormat.format("英文"))

math = int(math)
english = int(english)

print("=" * 60)

print(outputNameFormat.format("姓名", name))
print(outputScoreFormat.format("數學成績", math))
print(outputScoreFormat.format("英文成績", english))
print(outputScoreFormat.format("總成績", math + english))
