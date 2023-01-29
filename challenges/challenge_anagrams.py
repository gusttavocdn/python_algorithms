def is_anagram(first_string: str, second_string: str):
    first_string = merge_sort_string(list(first_string.lower()))
    second_string = merge_sort_string(list(second_string.lower()))

    is_anagram = first_string == second_string and (
        first_string != "" and second_string != ""
    )
    return (first_string, second_string, is_anagram)


def merge_sort_string(string, start=0, end=None):
    if end is None:
        end = len(string)

    if end - start > 1:
        mid = (start + end) // 2
        merge_sort_string(string, start, mid)
        merge_sort_string(string, mid, end)
        string = merge(string, start, mid, end)

    return "".join(string)


def merge(string, start, mid, end):
    left_half = string[start:mid]
    right_half = string[mid:end]

    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            string[start] = left_half[left_index]
            left_index += 1
        else:
            string[start] = right_half[right_index]
            right_index += 1
        start += 1

    while left_index < len(left_half):
        string[start] = left_half[left_index]
        left_index += 1
        start += 1

    while right_index < len(right_half):
        string[start] = right_half[right_index]
        right_index += 1
        start += 1

    return string


# print(is_anagram("PEDRA", "perda"))
