from collections import Counter
import time

from streamparse import Bolt

class TopNFinderBolt(Bolt):
    outputs = ['top-N']

    def initialize(self, storm_conf, context):
        self.top_words = Counter()
        self.N = 10
        self.interval = 0.1 # 100 milliseconds
        self.last_report = time.time()

    def process(self, tup):
        # TODO:
        # Task: keep track of the top N words
        # topwordslist = []
        # word = tup.values[0]
        # # see if there's a way to store these values in some kind of dictionary to later be counted?
        # self.logger.info("- [pid={}] - Processing received message [{}]".format(self.pid,word))
        # topwordslist.append(word)
        # # self.top_words = Counter(topwordslist)
        # self.top_words(topwordslist)
        # self.emit([word, self.counter[word]])
        # self.logger.info("- [pid={}] - Emitting: count [{},{}]".format(self.pid,word,self.counter[word]))
        # word = tup.values[0]
        # self.logger.info("- [pid={}] - Processing received message [{}]".format(self.pid,word))
        # self.counter[word[0]] += word[1]
        #self.emit([word, self.counter[word]])
        # self.logger.info("- [pid={}] - Emitting: count [{},{}]".format(self.pid,word,self.counter[word]))
        word = tup.values[0]
        count = tup.values[1]
        # self.logger.info("- [pid={}] - Processing received tup [{}]".format(self.pid, tup))
        self.logger.info("- [pid={}] - Processing received message [{},{}]".format(self.pid, word,count))
        # self.logger.info("- [pid={}] - Processing received count [{}]".format(self.pid, count))
        self.top_words[word] += count
        self.emit([word, self.top_words[word]])
        # self.emit([word, self.top_words[word]])
        # self.logger.info("- [pid={}] - Emitting: count [{},{}]".format(self.pid,word,self.top_words[word]))
        

        # report the top N words periodically
        if time.time() - self.last_report >= self.interval:
            self.report()

    def report(self):
        self.last_report = time.time()

        common_list = self.top_words.most_common(self.N)
        self.logger.info('- [pid={}] - Emitting: top-n [top-word = {}]'.format(self.pid,str(common_list)))
        self.emit([common_list])