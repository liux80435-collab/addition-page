"""计算两个两位数的和。"""


def read_two_digit_number(prompt: str) -> int:
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("请输入整数。")
            continue

        if 10 <= number <= 99:
            return number

        print("请输入 10 到 99 之间的两位数。")


def main() -> None:
    first = read_two_digit_number("请输入第一个两位数：")
    second = read_two_digit_number("请输入第二个两位数：")
    print(f"{first} + {second} = {first + second}")


if __name__ == "__main__":
    main()
