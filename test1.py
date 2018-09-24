#!/usr/bin/env python

import pytest
@pytest.mark.parametrize(("a,b"), [(1,1), (1,1), (1,2)],
                         ids=["basic", None, "advanced"])  
def test_function(a, b):
    assert a == b