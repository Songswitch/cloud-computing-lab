def is_prime(n):
    """判断一个整数是否为素数"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # 只需检查到 sqrt(n)，且跳过偶数
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input("请输入一个正整数: "))
    if is_prime(num):
        print(f"{num} 是素数")
    else:
        print(f"{num} 不是素数")
