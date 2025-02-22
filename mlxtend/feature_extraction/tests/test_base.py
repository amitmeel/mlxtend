# Sebastian Raschka 2014-2020
# mlxtend Machine Learning Library Extensions
# Author: Sebastian Raschka <sebastianraschka.com>
#
# License: BSD 3 clause

import numpy as np
import pytest

from mlxtend.feature_extraction.base import _BaseFeatureExtractor

X, y = np.array([[1, 2], [4, 5], [3, 9]]), np.array([1, 2, 3])
base = _BaseFeatureExtractor()


def test_X_array_pass():
    base._check_arrays(X=X)


def test_X_y_array_pass():
    base._check_arrays(X=X, y=y)


def test_1D_X():
    with pytest.raises(ValueError):
        base._check_arrays(X=X[1])


def test_X_int_y():
    with pytest.raises(ValueError):
        base._check_arrays(X=X, y=y[1])


def test_X_short_y():
    print(y[1:].shape)
    print(X.shape)
    with pytest.raises(ValueError):
        base._check_arrays(X=X, y=y[1:])
