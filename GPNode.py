class GPNode:
    type = None
    name = None
    parent = None
    children = []
    def isRoot(self):
        return self.parent == None
    def isLeaf(self):
        return len(self.children) == 0
