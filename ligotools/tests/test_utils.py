
# utils.py tests


import numpy as np
from ligotools.utils import *

def test_whiten_constant_signal():
    dt = 1/1024
    N = 1024
    strain = np.ones(N)
    interp_psd = lambda f: np.ones_like(f)

    white = whiten(strain, interp_psd, dt)

    white_mean = np.mean(white)
    white_std = np.std(white)

    assert white_mean <= 1
    assert white_std <= 1

def test_reqshift_no_shift():
    fs = 4096
    N = fs
    x = np.random.randn(N)

    shifted = reqshift(x, fshift=0, sample_rate=fs)

    # everything should be the same (with tolerance)
    assert np.allclose(shifted, x, atol=1e-6)

