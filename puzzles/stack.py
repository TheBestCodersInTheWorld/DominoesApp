import time as tt


class Stack():
    def __init__(self):
        self.items = []
    def push(self, thing):
        self.items.append(thing)
    def pop(self):
        if self.items:
            return self.items.pop(-1)
    def peek(self):
        return self.items[-1]

# STACK

"""
Stack is a data structure. 


1. Push: adding something to the TOP of the stack
example: bens_stack.push("something")

bens_stack = (bottom)["harry_potter","artemis_fowl"](top)
bens_stack.push("percy_jackson")
bens_stack = (bottom)["harry_potter","artemis_fowl", "percy_jackson"](top)

2. Pop: taking something off the top of the stack
-returns you the thing that you took off the top

last_book = bens_stack.pop()
last_book -> "percy_jackson"

3. Peek: look at the top element

last_book = bens_stack.peek()
last_book -> "percy_jackson"



"""


# stuff = ([][{{}{}[{{{{{{{[][][])}}}}}}]})

# PROBLEM: Matching Parenthesis

# Given a string that has parenthesis in it, determine if the string is valid, 
# meaning all the parenthesis are matched up. Return True if it is, or false
# if it isnt

# example:


"""
1. input: (ben)[]
-> return True

2.  input: [((ben) dalia)]
-> return True

3.  input:  [(])
-> return False 

4. input: [(()){]
-> return False
"""


# example: input_string = ([hello, ben and dalia]){[]}

def valid_paren(input_string):
    ben_and_Dalia_stack = Stack()
    for character in input_string:
        if character == "(" or character == "[" or  character == "{":
            ben_and_Dalia_stack.push(character)
        elif character == "]":
            last_popped = ben_and_Dalia_stack.pop()
            if last_popped != "[":
                return False
        elif character == ")":
            last_popped = ben_and_Dalia_stack.pop()
            if last_popped != "(":
                return False
        elif character == "}":
            last_popped = ben_and_Dalia_stack.pop()
            if last_popped != "{":
                return False
    if len(ben_and_Dalia_stack.items) != 0:
        return False
    return True


# Test Cases
input_string = "{{{{[[[[]]]]}}}}" # expected: true

start = tt.time()
# time the below stuff
valid_paren(input_string)
end = tt.time()
print("TIME IS:", end-start)

input_string = "(((((((((((((((([{{{{{{{{{{{{{{{{{{{{(((((((((((((((((}}}}}}}}}}}}}}}}}}}]]]]]]]]]]]]]]]]]]]]]]]{{{{{{{{{{}]]]]]]]]]]]]}}{{{{{}}}{}{&O*T BIVBY&BTVIK&TB KOI&OYOBY&P}}}}}}}}}}{{}|{}{{{]" # expected: false
print(valid_paren(input_string))

start = tt.time()
# time the below stuff
valid_paren(input_string)
end = tt.time()
print("TIME IS:", end-start)


input_string = "[[[()(){}{}]]](zoldjflz){{{{{{{{{{((()))}}}}}}}}}}" # expected: true
print(valid_paren(input_string))

start = tt.time()
# time the below stuff
valid_paren(input_string)
end = tt.time()
print("TIME IS:", end-start)


input_string = "(((((asdfghjkl))))" # expected: false
print(valid_paren(input_string))

input_string = "\"\"\"\"\"\"\"\"\"\"\"\"" # expected: true
print(valid_paren(input_string))

input_string = "fasihudidvbasdfijhaosidfjodiuahfu" # expected: true
print(valid_paren(input_string))

input_string = "12345678910123456789101234567891012345678912345678123456" # expected: true
print(valid_paren(input_string))

input_string = "" # expected: true
print(valid_paren(input_string))















































































































