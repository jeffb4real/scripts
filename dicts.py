#!/usr/bin/env python
from collections import OrderedDict

# TODO: Figure out why dictionary isn't ordered!
mydict = OrderedDict({
  "this": "succeeded",
  "by": "getting",
  "the": "dweets",
  "with": [
    {
      "thing": "my-thing-name",
      "created": "2014-01-15T18:41:17.166Z",
      "content": {
        "this": "is cool!"
      }
    },
    {
      "thing": "my-thing-name",
      "created": "2014-01-15T18:41:01.583Z",
      "content": {
        "hello": "world",
        "foo": "bar"
      }
    }
  ]
})


for key in mydict:
    print key