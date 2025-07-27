#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:00:58 2025

@author: Sumanth Reddy Velagala
"""

import pytest

def heapify(arr, n, i):
    
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2  

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)

def heapSort(arr):
    
    n = len(arr) 

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        heapify(arr, i, 0)
        
        
        
# Test case 1: Sorting an already sorted array
def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    heapSort(arr)
    assert arr == [1, 2, 3, 4, 5]


# Test case 2: Sorting a reverse-sorted array
def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    heapSort(arr)
    assert arr == [1, 2, 3, 4, 5]


# Test case 3: Sorting an array with all elements equal
def test_all_equal_elements():
    arr = [3, 3, 3, 3, 3]
    heapSort(arr)
    assert arr == [3, 3, 3, 3, 3]


# Test case 4: Sorting an empty array
def test_empty_array():
    arr = []
    heapSort(arr)
    assert arr == []


# Test case 5: Sorting an array with one element
def test_single_element():
    arr = [42]
    heapSort(arr)
    assert arr == [42]


# Test case 6: Sorting a large array
def test_large_array():
    arr = [i for i in range(1000, 0, -1)]  # reverse order
    heapSort(arr)
    assert arr == list(range(1, 1001))


# Test case 7: Sorting an array with negative numbers
def test_array_with_negative_numbers():
    arr = [-1, -5, 3, 2, 0, -2]
    heapSort(arr)
    assert arr == [-5, -2, -1, 0, 2, 3]


# Test case 8: Sorting an array with floating-point numbers
def test_array_with_floats():
    arr = [3.14, 2.71, 1.41, 4.2, 2.0]
    heapSort(arr)
    assert arr == [1.41, 2.0, 2.71, 3.14, 4.2]


# Test case 9: Sorting a large array with random values
def test_random_values():
    arr = [24, 18, 31, 7, 2, 16, 9, 5]
    heapSort(arr)
    assert arr == [2, 5, 7, 9, 16, 18, 24, 31]


# Test case 10: Sorting a large array with random negative values
def test_random_negative_values():
    arr = [-3, -1, -7, -2, -4, -9]
    heapSort(arr)
    assert arr == [-9, -7, -4, -3, -2, -1]

# New Test Cases
def test_characters():
    arr = ['h','a','d','b','z']
    heapSort(arr)
    assert arr == ['a','b','d','h','z']
    
def test_mixed_data_types():
    arr = [25, -6, 5.5, 0]
    heapSort(arr)
    assert arr == [-6, 0, 5.5, 25]
    
def test_case_sensitivity():
    arr = ['J', 'D', 'z', 'G', 'a']
    heapSort(arr)
    assert arr ==  ['D', 'G', 'J', 'a', 'z']
    
def test_Lexicographical():
    arr = ['strawberry', 'apple', 'orange', 'grapes']
    heapSort(arr)
    assert arr == ['apple', 'grapes', 'orange', 'strawberry']
def test_Special_Char():
    arr = ['%', '@', '!', '<', '(']
    heapSort(arr)
    assert arr == ['!', '%', '(', '<', '@']
    
def fail_test():
    arr = [10, 20, -49, 5.8, "hello", "F", '?']
    
    

if __name__ == '__main__':
    pytest.main()