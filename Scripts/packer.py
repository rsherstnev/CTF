import base64
import sys

with open(sys.argv[1], "r") as script:
    code = str(base64.b64encode(bytes(script.read(), "utf-8"))).split('\'')[1]
    print("python -c \"exec('{}='.decode('base64'))\"".format(code))
