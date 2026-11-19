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
    while True:
        text = input("请输入一个正整数（输入 q 退出）: ")
        if text.strip().lower() == "q":
            print("程序已退出")
            break
        try:
            num = int(text)
        except ValueError:
            print("输入无效，请输入一个整数")
            continue
        if is_prime(num):
            print(f"{num} 是素数")
        else:
            print(f"{num} 不是素数")
