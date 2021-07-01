#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_y(m, b, x):
    y = m*x + b
    return y
    print(y)

#Functions to find the value of m and b for y = m*x + b 
def calculate_error(m, b, point):
    y = get_y(m, b, point[0])
    error = abs(point[1] - y)
    return error

def calculate_all_error(m, b, points):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error

datapoints =  [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
possible_ms = [m * 0.1 for m in range(-100, 101)]
possible_bs = [b * 0.1 for b in range(-200, 201)]

smallest_error = float("inf")
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error
    
                
print(best_m,best_b,smallest_error)