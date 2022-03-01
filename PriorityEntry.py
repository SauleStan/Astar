# Class to deal with priority queue issues when the f(n) is equal

class PriorityEntry(object):

    def __init__(self, priority, node):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority