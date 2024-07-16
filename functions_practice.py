'''Please complete the following functions.

arb_args - Takes in any number of arguments and prints them one at a time.
inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
sum_n_product - Accepts two integers and returns both the sum and the product.
alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
arb_mean - Accepts any number of integers and prints their average.
arb_longest_string - Accepts any number of strings and returns the longest one.'''

def arb_args(args):
    for i in range(len(args)):
        print(args[i])

def inner_func(int1, int2):
    math1 = int1 * int2
    math2 = int1 - int2
    return math1 + math2

def lunch_lady(st_name, st_pref="Mystery Meat"):
    print(f'{st_name} will eat {st_pref}!')

def sum_n_product(int1, int2):
    return int1*int2, int1*int2

alias_arb_args = arb_args(["test1","test2", "test3"])

def alias_arb_args_innerFunc():
    arb_args(["test4","test5","test6"])

def arb_mean(args):
    total = sum(args)
    average = total/len(args)
    print(average)

def arb_longest_string(args):
    longest = args[0]
    for i in range(len(args)):
        if len(args[i]) > len(longest):
            longest = args[i]
    print(f"Longest word is {longest}")


def test_all():
    test_list_strings = ["me","you","brother","cousin"]
    test_list_numbers = [2,4,7,1,0,-1,3]

    arb_args(test_list_strings)
    inner_func(2,6)
    lunch_lady("Sam")
    lunch_lady("Sam", "Hamburgers")
    sum_n_product(3,4)
    alias_arb_args_innerFunc()
    arb_mean(test_list_numbers)
    arb_longest_string(test_list_strings)

test_all()