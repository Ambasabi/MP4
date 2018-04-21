import os
from os.path import join
from time import sleep

from streamparse import Spout

class FileReaderSpout(Spout):
    outputs = ['word']

    def initialize(self, stormconf, context):
        datafile = join(os.getcwd(), stormconf['coursera.datafile'])

        # TODO:
        # Task: Initialize the file reader
        with open(datafile) as f:
            lines = f.read().splitlines()
        self.sentences = iter(lines)
        f.close()
        # self.f = datafile #this might need to be something like open(datafile) or something.
        # self._conf = stormconf
        # self._context = context


    def next_tuple(self):
        # TODO:
        # Task 1: read the next line and emit a tuple for it
        # for line in self.f.readlines():
        #     storm.logInfo("Emitting %s" % line)
        #     storm.emit([line])
        sentence = next(self.sentences)
        # Task 2: don't forget to sleep for 1 second when the file is
        #         entirely read to prevent a busy-loop
        sleep(0.1)
        # Task 3: use the "self.logger.info(...)" function to print 1. the message received and 2. the message emitted
        self.emit([sentence])
        self.logger.info("- [pid={}] - Emitting: spout [{}]".format(self.pid,sentence))

        pass

    # NOTE: Streamparse does not have a close() function
    #       Closing the file should be handled in initialize() itself