class GPNode:
    type = None
    parent = None
    children = []
    def isRoot(self):
        return self.parent == None
    def isLeaf(self):
        return len(self.children) == 0
