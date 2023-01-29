def is_anagram(first_string: str, second_string: str):
    first_string = merge_sort_string(first_string.lower())
    second_string = merge_sort_string(second_string.lower())

    is_anagram = first_string == second_string and (
        first_string != "" and second_string != ""
    )
    return (first_string, second_string, is_anagram)


def merge_sort_string(string):
    string = list(string)
    if len(string) > 1:
        mid = len(string) // 2
        left_half = string[:mid]
        right_half = string[mid:]

        left_half = merge_sort_string(left_half)
        right_half = merge_sort_string(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                string[k] = left_half[i]
                i += 1
            else:
                string[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            string[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            string[k] = right_half[j]
            j += 1
            k += 1

    return "".join(string)


print(is_anagram("amor", "roma"))
