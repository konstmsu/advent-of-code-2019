# %%
# range 240920-789857


def might_be_password(v):
    sv = str(v)
    non_decreasing = True
    has_duplicate = False
    for c in range(len(sv) - 1):
        if int(sv[c]) > int(sv[c+1]):
            non_decreasing = False
        if sv[c] == sv[c+1]:
            has_duplicate = True

    if has_duplicate and non_decreasing:
        return True

    return False

# 80486 is wrong
# 1610 is wrong
# 121 is wrong


def might_be_password2(v):
    sv = str(v)
    non_decreasing = True
    has_duplicate = False
    for c in range(len(sv) - 1):
        if int(sv[c]) > int(sv[c+1]):
            non_decreasing = False

    c = 0
    while c < len(sv):
        j = c + 1
        matches = 1
        while j < len(sv):
            if sv[j] == sv[c]:
                matches += 1
            else:
                break
            j += 1
        c = j

        if matches == 2:
            has_duplicate = True

        # c += 1

    if has_duplicate and non_decreasing:
        return True

    return False

# 470 is wrong
# 900 is wrong


assert might_be_password2(245999) == False
assert might_be_password2(245899) == True


# %%

possible_password_count = 0
for v in range(240920, 789857+1):
    if might_be_password2(v):
        possible_password_count += 1

print(possible_password_count)
