from enum import Enum

'''Using an ENUM to document the types of relationships between intervals'''
Relations = Enum('RELATIONS', 'LEFT_DISJOINT RIGHT_DISJOINT CONTAINED CONTAINS EQUALS OVERLAP')

class Interval:
    ''' Models the semi-open Interval [a, b).
    Intended to explore Object Orientation, rather than
    the mathematics of such intervals. [0, 0) will be
    used to show error'''

    def __init__(self, lo: int, hi: int):
        self.lo = lo
        self.hi = hi
    
    def __len__(self) -> int:
        return self.hi - self.lo
    
    def __repr__(self) -> str:
        return f'[{self.lo}, {self.hi})'

    def _relation(self, other):
        if self. lo == other.lo and self.hi == other.hi:
            return Relations.EQUALS
        
        elif self.lo < other.lo < other.hi < self.hi:
            return Relations.CONTAINS
        
        elif other.lo < self.lo < self.hi < other.hi:
            return Relations.CONTAINED
        
        elif other.hi < self.lo:
            return Relations.RIGHT_DISJOINT
        
        elif self.hi < other.lo:
            return Relations.LEFT_DISJOINT
        
        else:
            return Relations.OVERLAP
    
    def is_equal(self, other) -> bool:
        return self._relation(other) == Relations.EQUALS

    def is_disjoint(self, other) -> bool:
        return self._relation(other) in {Relations.RIGHT_DISJOINT, Relations.LEFT_DISJOINT}
    
    def is_containing(self, other) -> bool:
        return self._relation(other) == Relations.CONTAINS
    
    def is_contained_in(self, other) -> bool:
        return self._relation(other) == Relations.CONTAINED
    
    def is_overlapping(self, other) -> bool:
        return self._relation(other) == Relations.OVERLAP

    def combine(self, other):
        if self.is_disjoint(other):
            return Interval(0, 0)
        else:
            left = min(self.lo, other.lo)
            right = max(self.hi, other.hi)
            return Interval(left, right)
    
    def pick_common(self, other):
        if self.is_disjoint(other):
            return Interval(0, 0)
        else:
            left = max(self.lo, other.lo)
            right = min(self.hi, other.hi)
            return Interval(left, right)