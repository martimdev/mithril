class Scene:
    def __init__(self):
        self.nodes = []
        self.selected_node = None

    def add_node(self, node):
        self.nodes.append(node)
