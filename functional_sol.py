# Implement a function that will flatten and sort an array
# of integers in ascending order, and which adheres to a
# functional programming paradigm.

def flat_and_sorted(a):
    new_array = []
    for int in a:
        if type(int) == list:
            for each in int:
                new_array.append(each)
        else:
            new_array.append(int)
    return sorted(new_array)

a = [1, [2, 6], 3, [4, 9, 5]]

print(a)
print(flat_and_sorted(a))

# How does this solution ensure data immutability?
    # The original array(a) does not change and is only used
    # to create a new_array which is seperate from the original.

# Is this solution a pure function? Why or why not?
    # It is pure because the input does not change.

# Is this solution a higher order function? Why or why not?
    # No, there are no nested functions within flat_and_sorted.

# Would it have been easier to solve this problem using a
# different programming style?
    # If the goal is to keep the function pure then it is the
    # best solution. That being said, I'm sure there is a cleaner
    # and more concise way to code it. I'm still learning.

# Why in particular is functional programming a helpful
# paradigm when solving this problem?
    # It does not produce or rely on side effects, the output only
    # relies on the input.




