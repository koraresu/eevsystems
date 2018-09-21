#!/usr/bin/python
import sys
sys.path.insert(0,"/home/ubuntu/sample-app/app")
from server import app as application


if __name__ == '__main__':
	application.run(host="0.0.0.0", port=80)