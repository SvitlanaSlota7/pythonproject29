from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _fill_order(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self._fill_order(i, visited, stack)
        stack.append(v)

    def _get_transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def _dfs_util(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self._dfs_util(i, visited, component)

    def find_sccs(self):
        stack = []
        visited = [False] * self.V

        # Заповнюємо стек згідно з часом виходу (DFS)
        for i in range(self.V):
            if not visited[i]:
                self._fill_order(i, visited, stack)

        # Отримуємо транспонований граф
        gr = self._get_transpose()

        # DFS по реверсивному графу в порядку стека
        visited = [False] * self.V
        all_sccs = []

        while stack:
            i = stack.pop()
            if not visited[i]:
                component = []
                gr._dfs_util(i, visited, component)
                all_sccs.append(component)

        return all_sccs

g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

sccs = g.find_sccs()
print("Сильно зв'язні компоненти:")
for component in sccs:
    print(component)