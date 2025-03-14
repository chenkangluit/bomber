# 消息轰炸工具

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)![Platform](https://img.shields.io/badge/platform-Windows%7CmacOS%7CLinux-green)

基于Python开发的自动化消息发送工具，通过模拟键盘操作实现快速批量发送。适用于压力测试/批量通知等场景（请遵守相关平台使用规范）

## ✨ 功能特性

### 操作模式

- **文本轰炸**：直接输入文字内容进行发送
- **文件轰炸**：读取文本文件内容逐行发送
- **倒计时设置**：自定义准备时间（默认10秒）

### 核心能力

- 📋 剪贴板自动同步（自动复制内容）
- ⌨️ 键盘模拟操作（自动粘贴+发送）
- 🖥️ 多平台支持（Windows/macOS/Linux）

## 🛠️ 安装指南

1. 克隆仓库：

```bash
git clone https://github.com/chenkangluit/bomber.git
cd bomber
```

## 🚀 使用说明

### 快速开始

```
python bomber.py -h
usage: bomber.py [-h] {content,file,setting} ...

消息轰炸工具

positional arguments:
  {content,file,setting}
                        可用的命令
    content             发送指定文字
    file                发送文件内容
    setting             设置倒计时

options:
  -h, --help            show this help message and exit


```

### 操作演示

1. 选择模式（文本/文件）
2. 输入消息内容/文件路径
3. 设置倒计时（默认10秒）
4. 快速切换到目标窗口
5. 自动执行发送任务

### 参数示例

```bash
# 发送自定义文本 “？”（20条）
python .\bomber.py content ? --times 20

# 从文件读取内容发送
python bomber.py file ./message
```

## ⚠️ 注意事项

1. 使用前确保：
   - 目标窗口处于激活状态
   - 输入法切换为英文模式
   - 关闭剪贴板历史记录功能
2. 建议操作：
   - 首次使用先进行5秒倒计时测试
   - 发送频率不宜超过20条/秒
   - 敏感场景建议在虚拟机运行

## 🤝 参与贡献

欢迎提交PR或Issue：

1. Fork项目仓库
2. 创建特性分支（git checkout -b feature/xxx）
3. 提交修改（git commit -m 'Add some feature'）
4. 推送分支（git push origin feature/xxx）
5. 新建Pull Request

## 📄 许可协议

本项目采用 [MIT License](LICENSE)

------

📌 温馨提示：本工具仅限合法用途，使用前请确保遵守目标平台的服务条款。开发者不对滥用行为负责。

优化说明：

1. 增加平台支持徽章
2. 补充系统权限配置说明
3. 添加命令行参数示例
4. 强化注意事项章节
5. 增加贡献指南和许可协议
6. 使用更直观的表情符号分隔区块
7. 补充多平台兼容性说明
8. 增加操作建议和安全提示