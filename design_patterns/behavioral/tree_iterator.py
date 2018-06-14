"""
Intent
------
Provide a way to access the elements of an aggregate object sequentially
without exposing its underlying representations.
"""


depth_first = {
    '1': ['2', '7', '8'],
    '2': ['3', '6'],
    '8': ['9', '12'],
    '3': ['4', '5'],
    '9': ['10', '11'],
}


class ConnectedComponent:

    def __init__(self, adjacency_matrix):
        self.tree = adjacency_matrix

    # Concrete Iterator
    def depth_first(self, node):
        """Depth first search iterator."""
        if node in self.tree:
            for child_node in reversed(self.tree[node]):
                yield from self.depth_first(child_node)
        yield node


def main():
    root = '1'
    component = ConnectedComponent(depth_first)
    print(', '.join(component.depth_first(root)))


if __name__ == '__main__':
    main()
