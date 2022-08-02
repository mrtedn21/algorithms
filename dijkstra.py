from typing import Generator
from typing import Optional

INFINITY = 999


class Edge:
    def __init__(self,
                 weight: int,
                 first: Optional["Node"] = None,
                 last: Optional["Node"] = None) -> None:

        self.weight: int = weight
        self.first: Optional[Node] = None
        self.last: Optional[Node] = None

        if first:
            self.set_first(first)
        if last:
            self.set_last(last)

    def set_first(self, node: "Node") -> None:
        self.first = node
        node.add_edge(self)

    def set_last(self, node: "Node") -> None:
        self.last = node
        node.add_edge(self)

    def __repr__(self) -> str:
        return f'Edge, weight={self.weight}, first="{self.first.name}",' + \
               f'last="{self.last.name}"'


class Node:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.parent: Optional[Node] = None
        self.weight: int = INFINITY
        self.edges: list[Edge] = []
        # passed variable needs for iterator to know needs iterate this
        # node of no. Because as iterator walk through the node, iterator
        # mustn't walk through it again
        self.passed: bool = False

    def add_edge(self, edge: Edge) -> None:
        if edge not in self.edges:
            self.edges.append(edge)

    def __repr__(self):
        return f'Node, name="{self.name}", weight={self.weight}.'


class DijkstraAlg:
    def __init__(self, in_node: Node, out_node: Node) -> None:
        self._in_node: Node = in_node
        self._out_node: Node = out_node
        self._all_nodes: list[Node] = []

    def execute(self):
        self._collect()
        self._run_for_nodes()
        self._print_short_path()

    def _print_short_path(self, current_node: Optional[Node] = None) -> None:
        if not current_node:
            print('Short path is:')
            current_node = self._out_node

        print(current_node.name)
        if current_node.parent is None:
            return
        self._print_short_path(current_node.parent)

    def _collect(self, current_node: Optional[Node] = None) -> None:
        if not current_node:
            current_node = self._in_node

        for edge in current_node.edges:
            if edge.first not in self._all_nodes:
                self._all_nodes.append(edge.first)
                self._collect(edge.first)

            if edge.last not in self._all_nodes:
                self._all_nodes.append(edge.last)
                self._collect(edge.last)

    def _node_iterator(self) -> Generator[Node, None, None]:
        while True:
            available_nodes: list[Node] = list(filter(
                lambda element: not element.passed,
                self._all_nodes
            ))

            if not len(available_nodes):
                break

            light_element = sorted(
                available_nodes, key=lambda element: element.weight
            )[0]
            yield light_element

    def _run_for_nodes(self) -> None:
        self._in_node.weight = 0

        for node in self._node_iterator():
            for edge in sorted(node.edges, key=lambda element: element.weight):
                if edge.last is node:
                    brother_node: Node = edge.first
                else:
                    brother_node: Node = edge.last

                new_weight = node.weight + edge.weight
                if brother_node.weight > new_weight:
                    brother_node.weight = new_weight
                    brother_node.parent = node

            node.passed = True


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    ab = Edge(weight=2, first=a, last=b)
    ac = Edge(weight=1, first=a, last=c)
    cb = Edge(weight=3, first=c, last=b)
    ce = Edge(weight=4, first=c, last=e)
    bd = Edge(weight=7, first=b, last=d)
    de = Edge(weight=3, first=d, last=e)
    df = Edge(weight=5, first=d, last=f)

    alg = DijkstraAlg(in_node=a, out_node=f)
    alg.execute()
