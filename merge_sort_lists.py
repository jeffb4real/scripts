#!/usr/bin/python

# Write a function that will merge two lists into a final, sorted list.

def merge_sort_lists(a, b):
    #a = arg[0]
    #b = arg[1]
    a.extend(b)
    a.sort()
    return a

def main():
    a = [5, 3, 1, 2]
    b = [2, 0, 7, 4]
    print merge_sort_lists(a, b)

if __name__ == '__main__':
    main()
