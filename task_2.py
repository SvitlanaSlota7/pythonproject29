from collections import deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        # Додаємо ребра для неорієнтованого графа
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs_shortest_paths(self, start_node):
        """Найкоротші відстані від start_node до всіх інших вершин."""
        # Ініціалізуємо відстані як -1 ("недосяжно")
        distances = [-1] * self.V
        distances[start_node] = 0

        queue = deque([start_node])

        while queue:
            current = queue.popleft()

            for neighbor in self.adj[current]:
                if distances[neighbor] == -1:  # Якщо вершина ще не відвідана
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)

        return distances

    def all_pairs_shortest_paths(self):
        """Запускає BFS для кожної вершини та будує матрицю відстаней."""
        matrix = []
        for i in range(self.V):
            distances = self.bfs_shortest_paths(i)
            matrix.append(distances)
        return matrix

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(0, 2)

apsp_matrix = g.all_pairs_shortest_paths()

print("Матриця найкоротших шляхів :")
print("    0  1  2  3")
print("")
for idx, row in enumerate(apsp_matrix):
    print(f"{idx} | " + "  ".join(map(str, row)))