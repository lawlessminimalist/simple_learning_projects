import itertools
def minimumSum(num: int) -> int:
    num = sorted([int(x) for x in str(num)],reverse=True)
    return num[0] + num[1] + num[2]*10 + num[3]*10

print(minimumSum(3421))