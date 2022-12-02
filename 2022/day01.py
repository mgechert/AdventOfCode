def split_groups(list_str):
    group_strings = list_str.split("\n\n")
    groups = [group_str.split() for group_str in group_strings]
    int_groups = [[int(s) for s in group] for group in groups]

    return int_groups


def sum_groups(group_list):
    sums = [sum(group) for group in group_list]

    return sums


def sum_top_k(nums, k):
    k_sum = sum(sorted(nums)[-k:])

    return k_sum
