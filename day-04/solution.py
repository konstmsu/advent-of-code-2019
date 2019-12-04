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


possible_password_count = 0
for v in range(240920, 789857+1):
    if might_be_password(v):
        possible_password_count += 1

print(possible_password_count)
# 80486 is wrong
# 1610 is wrong
# 121 is wrong
