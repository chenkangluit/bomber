import time
import argparse
import pyautogui
import pyperclip
from tqdm import tqdm  # 新增进度条库

seconds = 10


def countdown(second):
    print("请在倒计时时间内，把光标放到输入框")
    for i in range(second, 0, -1):
        print(f"倒计时剩余: {i}秒", end='\r')  # 优化倒计时显示
        time.sleep(1)
    print("\n倒计时结束！")  # 强制换行避免进度条重叠


def content_bomb(content, times):
    countdown(seconds)

    # 使用tqdm进度条包裹外部循环
    with tqdm(total=times, desc="发送进度", ncols=75) as pbar:
        for j in range(times):
            for str1 in content.split("\n"):
                if str1.strip() == "": continue  # 跳过空行
                pyperclip.copy(str1)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
            pbar.update(1)  # 每次完整发送后更新进度
    print("✓ 消息发送完成")  # 添加完成标识


def file_bomb(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    str_list = [s for s in content.split("\n") if s.strip()]  # 过滤空行
    countdown(seconds)

    # 文件发送也添加进度条
    with tqdm(total=len(str_list), desc="文件发送", ncols=75) as pbar:
        for str1 in str_list:
            pyperclip.copy(str1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            pbar.update(1)
            time.sleep(0.1)
    print("✓ 文件发送完成")


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
        content_bomb(args.content, args.times)
    elif args.command == "file":
        file_bomb(args.file_path)
    elif args.command == "setting":
        setting(args.seconds)
    else:
        print("请指定一个有效的命令")


if __name__ == "__main__":
    main()
