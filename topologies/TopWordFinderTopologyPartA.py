from streamparse import Grouping, Topology

from spouts.RandomSentenceSpout import RandomSentenceSpout
from bolts.SplitSentenceBolt import SplitSentenceBolt
from bolts.WordCountBolt import WordCountBolt

class TopWordFinderTopologyPartA(Topology):
    # TODO:
    # Task: wire up the topology
    # Make sure you use the following names for each component
    # RandomSentenceSpout -> "spout"
    spout = RandomSentenceSpout
    # SplitSentenceBolt -> "split"
    split = SplitSentenceBolt
    # WordCountBolt -> "count"
    count = WordCountBolt

   
    # NOTE: will have to manually kill Topology after submission
