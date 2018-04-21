from streamparse import Grouping, Topology

from spouts.FileReaderSpout import FileReaderSpout
from bolts.SplitSentenceBolt import SplitSentenceBolt
from bolts.NormalizerBolt import NormalizerBolt
from bolts.WordCountBolt import WordCountBolt
from bolts.TopNFinderBolt import TopNFinderBolt

class TopWordFinderTopologyPartD(Topology):
    config = {'coursera.datafile': 'resources/data.txt'}

    # TODO:
    # Task: wire up the topology
    # Make sure you use the following names for each component
    # FileReaderSpout -> "spout"
    spout = FileReaderSpout.spec()
    # SplitSentenceBolt -> "split"
    split = SplitSentenceBolt.spec(inputs={spout: Grouping.fields('word')})
    # NormalizerBolt -> "normalize"
    normalize = NormalizerBolt.spec(inputs={split: Grouping.fields('word')})
    # WordCountBolt -> "count"
    count = WordCountBolt.spec(inputs={normalize: Grouping.fields('word')})
    # TopNFinderBolt -> "top-n"
    topn = TopNFinderBolt(input={count: Grouping.fields('word', 'count')})


    # NOTE: will have to manually kill Topology after submission
