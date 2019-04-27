from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size == 0

    def test_init_with_list(self):
        s = Set(['A', 'B', 'C'])
        assert s.contains('C') == True
        assert s.size == 3

    def test_contains(self):
        s = Set(['A', 'B', 'C'])
        assert s.contains('D') == False
        s = Set([])
        assert s.contains('D') == False

    def test_length(self):
        s = Set()
        assert s.size == 0
        s.add('A')
        assert s.size == 1
        s.add('B')
        assert s.size == 2
        s.remove('A')
        assert s.size == 1
        s.remove('B')
        assert s.size == 0

    def test_add(self):
        s = Set()
        s.add('A')
        assert s.contains('A') == True
        s.add('A')
        assert s.size == 1
        s.add('B')
        s.add('B')
        assert s.size == 2
        assert s.contains('A') == True
        assert s.contains('B') == True

    def test_remove(self):
        s = Set(['A', 'B'])
        assert s.size == 2
        s.remove('A')
        assert s.contains('B')
        assert s.size == 1

    def test_intersection(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A'])
        intersection = s.intersection(other_set)
        assert intersection.contains('A') == True
        other_set = Set(['D'])
        intersection = s.intersection(other_set)
        assert intersection.contains('D') == False
        assert intersection.size == 0

    def test_union(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A'])
        union = s.union(other_set)
        assert union.contains('A') == True
        assert union.contains('B') == True
        assert union.contains('C') == True
        s = Set(['A', 'B', 'C'])
        other_set = Set(['D', 'E'])
        union = s.union(other_set)
        assert union.contains('A') == True
        assert union.contains('B') == True
        assert union.contains('C') == True
        assert union.contains('D') == True
        assert union.contains('E') == True

    def test_difference(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'D'])
        difference = s.difference(other_set)
        assert difference.contains('C') == True
        assert difference.size == 2
        other_set = Set(['A', 'D', 'S'])
        s.add('L') # add new difference
        difference = s.difference(other_set)
        assert difference.contains("B") == True
        assert difference.contains('C') == True
        assert difference.contains('L') == True
        assert difference.size == 3
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'B', 'C'])
        difference = s.difference(other_set)
        assert difference.contains('C') == False
        assert difference.contains('A') == False
        assert difference.size == 0

    def test_symmetric_difference(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'D'])
        difference = s.symmetric_difference(other_set)
        assert difference.contains('D') == True
        assert difference.contains('B') == True
        assert difference.contains('C') == True
        s = Set(['A', 'B', 'C'])
        other_set = Set(['D', 'E', 'F'])
        difference = s.symmetric_difference(other_set)
        assert difference.contains('D') == True
        assert difference.contains('E') == True
        assert difference.contains('F') == True
        assert difference.contains('A') == True
        assert difference.contains('B') == True
        assert difference.contains('C') == True
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'B', 'C'])
        difference = s.symmetric_difference(other_set)
        assert difference.size == 0

    def test_is_subset(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A'])
        assert other_set.is_subset(s) == True
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'B', 'C'])
        assert s.is_subset(other_set) == True
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'B', 'C', 'D'])
        assert s.is_subset(other_set) == True
        s = Set(['A', 'B', 'C'])
        other_set = Set(['D'])
        assert s.is_subset(other_set) == False
       
