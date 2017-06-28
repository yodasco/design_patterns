class ScopeGuard:
    def __init__(self, op, *args):
        self.op = op
        self.args = args

    def __exit__(self, exc_type, exc_value, traceback):
        self.op(*self.args)

