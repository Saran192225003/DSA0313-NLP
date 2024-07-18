def is_match(input_string):
    transitions = {
        0: {'a': 1, 'b': 0},
        1: {'a': 1, 'b': 2},
        2: {'a': 1, 'b': 0}
    }
    current_state = 0
    for char in input_string:
        if char in transitions[current_state]:
            current_state = transitions[current_state][char]
        else:
            current_state = 0
    return current_state == 2
test_strings = ["ab", "aab", "aaaab", "abc", "xyzab", "abab", "ba"]
for test_string in test_strings:
    if is_match(test_string):
        print(f"'{test_string}' matches the pattern.")
    else:
        print(f"'{test_string}' does not match the pattern.")
