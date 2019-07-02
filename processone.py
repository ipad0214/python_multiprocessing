



class ProcessOne:
    def __init__(self, queue_one, queue_two):
        self.queue_one = queue_one
        self.queue_two = queue_two
        self.count = 0

        self.queue_two.put("Hello World")
        self.loop()

    def loop(self):
        while True:
            if not self.queue_one.empty():
                print(self.queue_one.get())
                self.queue_two.put("one: call: {}".format(self.count))
                self.count += 1