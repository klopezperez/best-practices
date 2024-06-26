"""
Unit and regression test for the measure module."""

import molecool
import numpy as np
import pytest

def test_calculate_distance():
    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])
    
    expected_distance =   0.999999999999999999999 
    calculated_distance = molecool.calculate_distance(r1, r2)
    
    assert pytest.approx(expected_distance) == calculated_distance

def test_calculate_angle():
    r1 = np.array([1,0,0])
    r2 = np.array([0,0,0])
    r3 = np.array([0,1,0])
    
    expected_angle = 90
    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)
    
    assert expected_angle == calculated_angle
