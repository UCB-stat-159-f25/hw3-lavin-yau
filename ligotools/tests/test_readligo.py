from ligotools import readligo as rl
import numpy as np

def test_dq_channel_to_seglist():
    channel = np.array([0, 0, 1, 1, 1], dtype=int)
    segments = rl.dq_channel_to_seglist(channel, fs=1)
    assert len(segments) == 1
    assert isinstance(segments[0], slice)
    assert segments[0].start == 2
    assert segments[0].stop == 5

def test_dq2segs():
    channel_dict = {"DEFAULT": np.ones(4, dtype=int)}
    gps_start = 100
    segment_list = rl.dq2segs(channel_dict, gps_start)
    assert segment_list.seglist == [(100, 104)]