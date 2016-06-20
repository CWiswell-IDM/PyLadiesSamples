import threading
import time
import datetime

class PrinterThread(threading.Thread):

    def __init__(self, queue, name, append_message_method):
        threading.Thread.__init__(self)
        self.queue = queue
        self.name = name
        self.append_message_method = append_message_method

    def run(self):
        while not self.queue.empty():
            test = self.queue.get()
            rightnow = str(datetime.datetime.now())
            name = test["name"]
            name_chunks = name.split('_')
            test_number = name_chunks[0]
            sleep_length = float(test_number)/3
            time.sleep(sleep_length)
            message = "{me} is handling {it} at {ti} for {wo} seconds.".format(me=self.name,
                                                             it=name,
                                                             ti=rightnow,
                                                             wo=sleep_length)
            self.append_message_method(message)
            self.queue.task_done()
