class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def __repr__(self):
        return f"{self.value}"