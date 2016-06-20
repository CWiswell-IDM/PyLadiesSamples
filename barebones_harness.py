import argparse
import json
import unittest
import Queue
from collections import deque
import time

import harness_config
import harnessed_printer

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--suite", help="JSON test-suite to load - e.g. sanity.json")
args = parser.parse_args()

class SimpleTestQueue():

    def __init__(self):
        self.test_queue = Queue.Queue()
        self.messages = deque([])
        suite_filename = args.suite
        test_json = json.loads(open(suite_filename).read())
        for test in test_json["tests"]:
            test_obj = {}
            test_obj["name"] = test["path"]
            test_obj["url"] = harness_config.endpoint
            test_obj["owner"] = harness_config.username
            self.test_queue.put(test_obj)

    def appendNewMessage(self, message):
        print message
        self.messages.append(message)

    def runThreadedTestPass(self):
        num_threads = harness_config.thread_count
        names = ["Franklin", "Banneker", "Revere", "Gill", "Bradford", "ThatOneGuy"]
        for x in range(num_threads):
            name = names[x % len(names)]
            print name
            t = harnessed_printer.PrinterThread(self.test_queue, name, self.appendNewMessage)
            t.daemon = True
            t.start()
            time.sleep(3)
        self.test_queue.join()
        print self.messages

if __name__ == "__main__":
    if not args.suite:
        print "USAGE: try barebones_harness.py -h for usage"
    else:
        queue = SimpleTestQueue()
        queue.runThreadedTestPass()
