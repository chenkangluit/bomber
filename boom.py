import time
import pyperclip
import keyboard

seconds = 10


# 倒计时
def countdown(second):
    print("请在倒计时时间内，把光标放到输入框\n")
    for i in range(second, 0, -1):
        print(f"{i}秒", end='\r')
        time.sleep(1)
    print("倒计时结束！")


# 发送指定文字
def content_boom():
    strs = input("输入发送内容:\n")
    times = int(input("发送次数:\n"))
    countdown(seconds)

    for j in range(times):
        for str1 in strs.split("。"):
            pyperclip.copy(str1)
            keyboard.press_and_release('ctrl+v')
            keyboard.press_and_release('enter')
            time.sleep(0.1)


# 发送文件内容
def file_boom():
    path = input("请指定文件按路径:\n")
    path = path.replace('"', '')
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    str_list = content.split("\n")
    countdown(seconds)

    for j in range(1):
        for str1 in str_list:
            pyperclip.copy(str1)
            keyboard.press_and_release('ctrl+v')
            keyboard.press_and_release('enter')
            time.sleep(0.1)


# 设置倒计时
def setting():
    global seconds
    print(f"当前倒计时时间为:{seconds}")
    seconds = int(input("请输入倒计时秒数:"))
    print(f"倒计时时间设置为:{seconds}")


def boom():
    while True:
        main()
        nums = int(input("请选择:\n"))
        match nums:
            case 1:
                content_boom()
            case 2:
                file_boom()
            case 3:
                setting()
            case 4:
                break


# 菜单
def main():
    print("---------轰炸---------")
    print("1. 发送指定文字")
    print("2. 发送文件内容")
    print("3. 设置倒计时")
    print("4. 退出")
    print("---------结束---------")


if __name__ == "__main__":
    boom()
