
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
assert(size(38) == 'S') #code fails to categorize properly when it tshirt size is exactly 38, it classifies as Large but it is not.
assert(size(40) == 'M')
assert(size(43) == 'L')
print("All is well (maybe!)\n")
