from streamparse import Bolt

class NormalizerBolt(Bolt):
    outputs = ['word']

    def initialize(self, storm_conf, context):
        self.common_words = [
            "the", "be", "a", "an", "and", "of", "to", "in", "am",
            "is", "are", "at", "not", "that", "have", "i", "it",
            "for", "on", "with", "he", "she", "as", "you", "do",
            "this", "but", "his", "by", "from", "they", "we", "her",
            "or", "will", "my", "one", "all", "s", "if", "any", "our",
            "may", "your", "these", "d" , " ", "me" , "so" , "what" , "him"
        ]

    def process(self, tup):
        # TODO:
        # Task 1: make the words all lower case
        word = tup.values[0]
        lowerword = word.lower()
        #lowersentence = tempsentence.lower()
        # Task 2: remove the common words
        # ret = []
        # for word in lowersentence:
        #     if word in self.common_words:
        #         continue
        #     else:
        #         ret.append(word)
        #     sentence = tuple(ret)
        # if word in self.common_words:
        #         return
        # else:
        if lowerword not in self.common_words:
            self.logger.info("- [pid={}] - Processing received message [{}]".format(self.pid, word))
            self.logger.info("- [pid={}] - Emitting: normalize [{}]".format(self.pid, lowerword))


        # Task 3: use the "self.logger.info(...)" function to print 1. the message received and 2. the message emitted
        #self.emit([sentence])
