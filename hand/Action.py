"""
所有 动作 的父类
"""


class Action:
    def __init__(self, name):
        self.name = name  # 动作名称
        self.description_en = ""  # 描述
        self.description_zh = ""  # 描述
        self.argument = ""  # 参数

    def action(self):
        """
        具体的动作
        :return:
        """
        pass

    def execute(self):
        """
        动作的执行
        :return:
        """
        pass
