"""
文件相关的操作
"""
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
        for args in kwargs:
            if args == 'file_name':
                file_name = kwargs[args]
            elif args == 'do':
                do = kwargs[args]

        


if __name__ == '__main__':
    a = ActionFile()
    a.action(name=a)