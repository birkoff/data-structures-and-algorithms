def get_factorial(number):
    print(number)
    if number == 1:
        return 1

    total =  number * get_factorial(number - 1)
    return total


def permutation_without_repetition(total, baseline):
    factorial_total = get_factorial(total)
    factorial_constrain = get_factorial(total - baseline)
    return factorial_total/factorial_constrain


def permutation_with_repetition(total, baseline):
    return total ** baseline


def permutations(_list):
    if len(_list) == 0:
        return []

    if len(_list) == 1:
        return [_list] # a new list

    permutator_list = []

    for i in range(len(_list)):
        item = _list[i]
        print("{} item {}".format(i, item))
        list_without_item = _list[:i] + _list[i+1:]
        print("{} item {}".format(i, list_without_item))
        permutations_without_item = permutations(list_without_item)
        for _permutation in permutations_without_item:
            permutator_list.append([item] + _permutation)
            print("{} item {}".format(i, permutator_list))

    return permutator_list

data = list('123')
for p in permutations(data):
    print(p)

# total = 5
# baseline = 2
#
# factorial_total = get_factorial(total)
# factorial_constrain = get_factorial(total-baseline)
#
# print("### Results ###")
#
# print("factorial_total: {}".format(factorial_total))
# print("factorial_constrain: {}".format(factorial_constrain))
#
# print("permutation_without_repetition (number of combinations of baseline with unique items in total): {}".format(factorial_total/factorial_constrain))
# print("permutation_with_repetition (number of combinations of baseline with repeted items in total): {}".format(total ** baseline))
