from streamparse import Grouping, Topology

from spouts.FileReaderSpout import FileReaderSpout
from bolts.SplitSentenceBolt import SplitSentenceBolt
from bolts.NormalizerBolt import NormalizerBolt
from bolts.WordCountBolt import WordCountBolt

class TopWordFinderTopologyPartC(Topology):
    config = {'coursera.datafile': 'resources/data.txt'}

    # TODO:
    # Task: wire up the topology
    # Make sure you use the following names for each component
    # FileReaderSpout -> "spout"
    spout = FileReaderSpout.spec()
    # SplitSentenceBolt -> "split"
    split = SplitSentenceBolt.spec(inputs={spout: Grouping.fields('word')})
    # WordCountBolt -> "count"
    normalize = NormalizerBolt.spec(inputs={split: Grouping.fields('word')})
    # NormalizerBolt -> "normalize"
    count = WordCountBolt.spec(inputs={normalize: Grouping.fields('word')})


    # NOTE: will have to manually kill Topology after submission
