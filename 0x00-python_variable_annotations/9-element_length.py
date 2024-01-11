#!/usr/bin/env python3
"""Script for function element_length"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Type-annotated function element_length,
    takes an iterable of sequences as argument, returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
