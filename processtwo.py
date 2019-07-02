



class ProcessTwo:
    def __init__(self, queue_two, queue_one, count):
        self.queue_one = queue_one
        self.queue_two = queue_two
        self.count = count

        self.loop()

    def loop(self):
        while True:
            if not self.queue_two.empty():
                print(self.queue_two.get())
                self.queue_one.put("two: count: {}".format(self.count.one))
                self.count.one += 1