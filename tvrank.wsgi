import sys,logging
logging.basicConfig(stream = sys.stderr)

sys.path.insert(0, '/home/jianan/public_html/tvrank')
from tv_media import app as application
