#!/usr/bin/python
import sys

from app import serverapp as application


#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/ubuntu/sample-app")

from serverapp import app as application
application.secret_key = 'Add your secret key'