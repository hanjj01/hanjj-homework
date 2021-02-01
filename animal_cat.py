from homework.animal import Animal


class Cat(Animal):
    def __init__(self):
        hair = "短毛"
        super().__init__("短耳猫", "黄色", "3", "女")

    def zhuols(self):
        print("会捉老鼠")

    def sing(self):
        super().sing()
        print("喵喵叫")


if __name__ == '__main__':
    eg2 = Cat()
    eg2.sing()
    eg2.runing()
