import math


def is_prime(n: int) -> bool:
    """判断一个数是否为素数"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_special_primes(start: int = 100000, end: int = 999999) -> list[int]:
    """生成指定范围内第二位和第三位数字相同的素数"""
    primes = []
    for num in range(start, end + 1):
        s = str(num)
        if len(s) >= 3 and s[1] == s[2] and is_prime(num):
            primes.append(num)
    return primes


# 主程序：生成并打印符合条件的素数
if __name__ == "__main__":
    result = generate_special_primes()
    print("生成的素数列表：")
    for p in result:
        print(p)
