# -*- coding: utf-8 -*-

from .context import sample

import pytest

def test_one():
    sample.parseString('display: .size 1');
