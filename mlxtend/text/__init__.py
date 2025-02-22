# Sebastian Raschka 2014-2020
# mlxtend Machine Learning Library Extensions
# Author: Sebastian Raschka <sebastianraschka.com>
#
# License: BSD 3 clause

import sys

if sys.version_info >= (3, 0):
    from .names import generalize_names
    from .names import generalize_names_duplcheck

from .tokenizer import tokenizer_emoticons, tokenizer_words_and_emoticons

__all__ = [
    "generalize_names",
    "generalize_names_duplcheck",
    "tokenizer_words_and_emoticons",
    "tokenizer_emoticons",
]
