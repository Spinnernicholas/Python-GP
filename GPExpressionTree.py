class GPExpressionTree:
    dna = None
    nodes = []
    head = None

    def __init__(self, dna=None):
        if dna is not None:
            self.dna = dna