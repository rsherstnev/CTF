#!/usr/bin/env python3

import base64
import sys

with open(sys.argv[1], "r") as script:
    code = str(base64.b64encode(bytes(script.read(), "utf-8"))).split('\'')[1]
    print("python3 -c \"import base64; exec(compile(base64.b64decode(b'{}'), '<string>', 'exec'))\"".format(code))
