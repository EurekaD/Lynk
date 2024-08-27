import keyboard

# 发送单个按键
# keyboard.press_and_release('shift+a')
#
# # 发送组合键
# keyboard.press_and_release('ctrl+c')

# 模拟输入字符串
keyboard.write('Hello, World!')

# 设置一个热键，比如按下 'esc' 键退出程序
keyboard.add_hotkey('esc', lambda: print('退出程序'))
keyboard.wait('esc')


