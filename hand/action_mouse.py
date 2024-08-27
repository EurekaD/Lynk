from hand.Action import Action


class ActionFile(Action):
    def __init__(self):
        name = 'FILE'
        super().__init__(name)
        self.description_en = "Create, delete, modify, view files"
        self.description_zh = "新建，删除，修改，查看文件"
        self.argument = "(file_name, do)"

    def execute(self):
        pass

    def action(self, **kwargs):
        pass


if __name__ == '__main__':
    import pyautogui

    # 获取屏幕大小
    screen_width, screen_height = pyautogui.size()
    print(f"屏幕大小: 宽={screen_width}, 高={screen_height}")

    # 移动鼠标到屏幕中心
    pyautogui.moveTo(0, 0, duration=1)

    # 左键点击
    pyautogui.click()

    # 右键点击
    pyautogui.click(button='right')

    # 双击
    pyautogui.doubleClick()

    # 拖动鼠标 (从当前位置向下拖动100像素)
    pyautogui.dragTo(screen_width // 2, screen_height // 2 + 100, duration=1)

    # 获取当前鼠标位置
    current_mouse_x, current_mouse_y = pyautogui.position()
    print(f"当前鼠标位置: x={current_mouse_x}, y={current_mouse_y}")
