'''a1_fn_sig_checker.py

This program can be used to check whether your Assignment 1 Part A Python file
is using correct function names, parameter types, and return types.

Usage:
python3 a1_fn_sig_checker.py

Your file a1.py must be in the same folder as this checking program.

S. Tanimoto, Sept. 25, 2019.
'''

import a1
import numbers
print("""-----------------------------------------------------------------------
Example longer than website
-----------------------------------------------------------------------
""")
print("input for five_x_cubed_plus_2: "+str(20))
result1 = a1.five_x_cubed_plus_2(20)

print("result: ")
print(result1)

result2 = a1.triple_up([1, 2, 3, 4, 5, 'a', 'b', ['x', 'y'], ['z'], 'second from last', 'last'])
print("input for triple_up: "+str([1, 2, 3, 4, 5, 'a', 'b', ['x', 'y'], ['z'], 'second from last', 'last']))
print("result: ")
print(result2)

result3 = a1.mystery_code("Usadjiasdij are blalbalb 0,w12e0394<>")
print("input for mystery_code: "+"Usadjiasdij are blalbalb 0,w12e0394<>")

print("result: ")
print(result3)

result4 = a1.future_tense(['He','did','it','. ','He', 'ate', 'all', 'the', 'cookies'])
print("input for future_tense: "+str(['He','did','it','. ','He', 'ate', 'all', 'the', 'cookies']))
print("result: ")
print(result4)

print("""-----------------------------------------------------------------------
Example in website
-----------------------------------------------------------------------
""")
print("input for five_x_cubed_plus_2: "+str(3))
result1 = a1.five_x_cubed_plus_2(3)
print("result: ")
print(result1)

result2 = a1.triple_up([1, 2, 3, 4, 5, 'a', 'b', ['x', 'y'], ['z'], 'second from last', 'last'])
print("input for triple_up: "+str([1, 2, 3, 4, 5, 'a', 'b', ['x', 'y'], ['z'], 'second from last', 'last']))
print("result: ")
print(result2)

result3 = a1.mystery_code("abc Iz th1s Secure? n0, no, 9!")
print("input for mystery_code: "+"abc Iz th1s Secure? n0, no, 9!")
print("result: ")
print(result3)

result4 = a1.future_tense(['Yesterday', 'I', 'ate', 'pasta', 'and', 'today', 'I', 'am', 'having', 'soup'])
print("input for future_tense: "+str(['Yesterday', 'I', 'ate', 'pasta', 'and', 'today', 'I', 'am', 'having', 'soup']))
print("result: ")
print(result4)

print("""-----------------------------------------------------------------------
Example shorter than website
-----------------------------------------------------------------------
""")
print("input for five_x_cubed_plus_2: "+str(1))
result1 = a1.five_x_cubed_plus_2(1)
print("result: ")
print(result1)

result2 = a1.triple_up([1, 2, 3 ,'second from last', 'last'])
print("input for triple_up: "+str([1, 2, 3 ,'second from last', 'last']))
print("result: ")
print(result2)

result3 = a1.mystery_code("abcde")
print("input for mystery_code: "+"abcde")
print("result: ")
print(result3)

result4 = a1.future_tense(['Yesterday', 'I', 'ate', 'ice','cream'])
print("input for future_tense: "+str(['Yesterday', 'I', 'ate', 'ice','cream']))
print("result: ")
print(result4)