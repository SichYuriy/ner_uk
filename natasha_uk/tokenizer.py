# coding: utf-8
from __future__ import unicode_literals

from yargy_uk.tokenizer import MorphTokenizer


TOKENIZER = MorphTokenizer().remove_types('EOL')
