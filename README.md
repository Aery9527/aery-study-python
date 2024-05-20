- PEP8 (Python Enhancement Proposal 8), 是一種 Python 的程式碼風格指南
- 變數全是reference, x = y = 10, x 和 y 都是指向同一個記憶體位置, 而不是像java原生型別一樣直接占用不同byte表達該數值
- 社群變數命名習慣蛇行命名法(snake_case), 全為小寫字母用底線分隔(my_variable)
- 動態強型別, 非弱型別. 弱型別可以執行"1" + 1, 但強型別不行, 可python宣告變數時不用指定型別, 於是是"動態強型別"
- 支援functional programming
- 使用模組（module）和封裝（package）來組織代碼，類似於Java中的包和類。 \
  但Python的模組系統更加靈活和簡單，並且模組可以在需要時動態加載。
- 多線程在某些情況下可能不如預期效果好，這是因為全局解釋器鎖（Global Interpreter Lock，GIL）的存在。 \
  因此，在Python中，更常見的是使用異步編程庫，如asyncio，來實現非阻塞的並發操作。
- 沒有character, 只有string