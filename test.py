import matplotlib.pyplot as plt
from matplotlib import rcParams
import networkx as nx

# 設定中文字體
rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
rcParams['axes.unicode_minus'] = False

# 創建有向圖
G = nx.DiGraph()

# 添加節點
nodes = {
    'C': '男（C）',
    'B': '媽媽（B）',
    'A': '女兒（A）',
    'D': '女兒的小孩（D）',
    'E': '媽媽的小孩（E）'
}

for node_id, label in nodes.items():
    G.add_node(node_id, label=label)

# 添加邊（關係）
edges = [
    ('C', 'B', '情侶'),
    ('C', 'A', '老公/女兒的老公'),
    ('B', 'A', '生'),
    ('B', 'E', '生'),
    ('C', 'E', '生'),
    ('A', 'D', '生'),
    ('C', 'D', '生')
]

for source, target, label in edges:
    G.add_edge(source, target, label=label)

# 創建圖表
plt.figure(figsize=(12, 8))
plt.title('血緣關係圖', fontsize=16, fontweight='bold')

# 設定節點位置（手動調整以獲得更好的視覺效果）
pos = {
    'C': (0, 2),    # 男性在上方左側
    'B': (2, 2),    # 媽媽在上方右側
    'A': (1, 1),    # 女兒在中間
    'E': (3, 1),    # 媽媽的小孩在右側
    'D': (1, 0)     # 女兒的小孩在底部
}

# 繪製節點
nx.draw_networkx_nodes(G, pos, node_color='lightblue',
                      node_size=2000, alpha=0.8)

# 繪製節點標籤
node_labels = {node: nodes[node] for node in G.nodes()}
nx.draw_networkx_labels(G, pos, node_labels, font_size=10, font_weight='bold')

# 繪製邊
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True,
                      arrowsize=20, arrowstyle='->', width=1.5)

# 繪製邊的標籤
edge_labels = {(source, target): data['label']
              for source, target, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)

plt.axis('off')  # 隱藏座標軸
plt.tight_layout()

# 儲存圖片
output_file = '血緣關係圖.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()

print(f"血緣關係圖已生成並儲存為：{output_file}")
