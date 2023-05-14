from sort import *
from every_odd_element import *

unsorted_array = [9, 5, 0, 3, 8, 2]

result_file = open("result.txt", "w+")

sorted_array = bubble_sort(unsorted_array)

odd_numbers = every_odd_element(sorted_array)

result_file.write(''.join(str(num) + ' ' for num in odd_numbers))

result_file.close()