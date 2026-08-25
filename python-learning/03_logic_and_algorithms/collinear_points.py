# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 15:36:33 2025

@author: gabri
"""

def are_collinear(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    x3: float,
    y3: float,
) -> bool:
    """
    Return True if three points are collinear.
    """
    return (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)

    