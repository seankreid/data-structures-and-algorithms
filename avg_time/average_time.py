#!/usr/bin/env python3

from time import time            # import time function from time module
from dynamic_array import DynamicArray #import dynamic array class
def compute_average(n, version):
  """Perform n appends to an empty list and return average time elapsed."""
  data = DynamicArray()
  start = time()                 # record the start time (in seconds)
  if version == 1:
    for k in range(n):
      data.append(k)
  elif version == 2:
    c = int(input("Enter a value in which to increase array by: "))
    for k in range(n):
      data.append1(k, c)
  end = time()                   # record the end time (in seconds)
  return (end - start) / n       # compute average per operation

def main():
  values = [10, 100, 1000, 10000]
  for i in values:
    print(1000 * compute_average(i, 1))
  for i in values:
    print(1000 * compute_average(i, 2))
  for i in values:
    print(1000 * compute_average(i, 2))  
    
if __name__ == '__main__':
    main()

