# %%
# range 240920-789857


from itertools import groupby


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
# 1154 is right


def might_be_password2(v):
    sv = str(v)

    non_decreasing = all(int(l) <= int(r) for l, r in zip(sv, sv[1:]))
    has_duplicate = any([len(list(g[1])) == 2 for g in groupby(sv)])

    return has_duplicate and non_decreasing

# 470 is wrong
# 900 is wrong


assert might_be_password2(245999) == False
assert might_be_password2(245899) == True


possible_password_count = 0
for v in range(240920, 789857+1):
    if might_be_password2(v):
        possible_password_count += 1

print(possible_password_count)
assert possible_password_count == 750
