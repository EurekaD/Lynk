"""
文件相关的操作
"""
from hand.Action import Action


class ActionFile(Action):
    def __init__(self):
        name = 'file'
        super().__init__(name)
        self.description_en = ""
        self.description_zh = ""
        self.argument = ""

    def execute(self):
        pass

    def action(self):
        pass