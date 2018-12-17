import http.server
import os
import datetime
import json
import logging

PORT = 8000
handler_class = http.server.CGIHTTPRequestHandler

starttime_iso = datetime.datetime.now().isoformat()
current = os.path.dirname(os.path.abspath(__file__))
os.chdir(current)

os.chdir("..\\conf")
with open('system.json', 'r') as f:
    sys = json.load(f)
    PORT = sys['port']

os.chdir(current)
logging.basicConfig(filename='..\\tarai.log', level=logging.DEBUG)
print("webserver.py service start.")
logging.info("[web] " + starttime_iso + " webserver.py service start.")
logging.debug(" > PORT:" + str(PORT))

with http.server.HTTPServer(("", PORT), handler_class) as httpd:
    httpd.serve_forever()
