class Wife:
    count = 0

    @classmethod
    def mount_of_wife(cls):
        print("一共娶了%d个老婆" % cls.count)

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        Wife.count += 1


w01 = Wife("xiaoj", 55, 158)
w02 = Wife("xiaoh", 50, 162)
w03 = Wife("xiaow", 55, 143)
Wife.mount_of_wife()
