



class ProcessTwo:
    def __init__(self, queue_two, queue_one):
        self.queue_one = queue_one
        self.queue_two = queue_two
        self.count = 0

        self.queue_one.put("Hello World")
        self.loop()

    def loop(self):
        while True:
            if not self.queue_two.empty():
                print(self.queue_two.get())
                self.queue_one.put("two: count: {}".format(self.count))
                self.count += 1