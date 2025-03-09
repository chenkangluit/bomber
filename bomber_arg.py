import time
import argparse
import pyautogui
import pyperclip

seconds = 10

# 倒计时
def countdown(second):
    print("请在倒计时时间内，把光标放到输入框\n")
    for i in range(second, 0, -1):
        print(f"{i}秒", end='\r')
        time.sleep(1)
    print("倒计时结束！")

# 发送指定文字
def content_boom(content, times):
    countdown(seconds)

    for j in range(times):
        for str1 in content.split("\n"):
            # 复制到剪切板
            pyperclip.copy(str1)

            # 粘贴文本并按下回车键
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')

# 发送文件内容
def file_boom(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    str_list = content.split("\n")
    countdown(seconds)

    for j in range(1):
        for str1 in str_list:
            pyperclip.copy(str1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            time.sleep(0.1)

# 设置倒计时
def setting(new_seconds):
    global seconds
    seconds = new_seconds
    print(f"倒计时时间设置为:{seconds}")

def main():
    parser = argparse.ArgumentParser(description="消息轰炸工具")
    subparsers = parser.add_subparsers(dest="command", help="可用的命令")

    # 发送指定文字
    content_parser = subparsers.add_parser("content", help="发送指定文字")
    content_parser.add_argument("content", type=str, help="要发送的内容")
    content_parser.add_argument("--times", type=int, default=1, help="发送次数")

    # 发送文件内容
    file_parser = subparsers.add_parser("file", help="发送文件内容")
    file_parser.add_argument("file_path", type=str, help="文件路径")

    # 设置倒计时
    setting_parser = subparsers.add_parser("setting", help="设置倒计时")
    setting_parser.add_argument("seconds", type=int, help="倒计时秒数")

    args = parser.parse_args()

    if args.command == "content":
        content_boom(args.content, args.times)
    elif args.command == "file":
        file_boom(args.file_path)
    elif args.command == "setting":
        setting(args.seconds)
    else:
        print("请指定一个有效的命令")

if __name__ == "__main__":
    main()