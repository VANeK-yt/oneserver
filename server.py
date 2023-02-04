# -*- coding: utf-8 -*-

#ONE SERVER
#by m1shkfr3d3

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from mimetypes import init as mimeinit, types_map as getmime
from os.path import join




class WebFiler():
    def gettype(self,path):
        path = path[1:]
        mimeinit()
        filetype = path[path.rfind('.'):path.rfind("?")]
        if filetype == '.oscript' or filetype == '':
            filetype = '.html'
        return getmime[filetype]

    def get(self, path):
        # self.path = path
        path = path[1:]
        arg = path[path.rfind('=') + 1:]
        if path == '':
            path = 'index.html'
        if '.oscript' in path:
            filename = path[path.rfind('/')+1:path.rfind("?")]
            oscript = osm.getosh()
            a = oscript(arg, filename)
            return a.encode()
        try:
            with open(join('html', path),encoding='utf8') as f:
               return f.read().encode()
        except FileNotFoundError:
            notfoundpage()
            
def notfoundpage():
    with open(join('html', 'serverspage', '404.html'),encoding='utf8') as f:
                return f.read().encode()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        filer = WebFiler()
        self.send_response(200)
        self.send_header("Content-type", filer.gettype(self.path))
        self.end_headers()
        self.wfile.write(filer.get(self.path))

class oscriptmanager():
    def setosh(self, oscript) -> None:
        self.oscript = oscript
    def getosh(self):
        return self.oscript

def run(oscript,hostName = "0.0.0.0",serverPort = 8080):
    global osm
    osm = oscriptmanager()
    osm.setosh(oscript)
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("""  _____                 _                                 
 / ___ \               | |                                
| |   | |____   ____    \ \   ____  ____ _   _ ____  ____ 
| |   | |  _ \ / _  )    \ \ / _  )/ ___) | | / _  )/ ___)
| |___| | | | ( (/ / _____) | (/ /| |    \ V ( (/ /| |    
 \_____/|_| |_|\____|______/ \____)_|     \_/ \____)_|    
                                                            by m1shkfr3d3""")
    print("ONEServer started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
if __name__ == "__main__":
    print("""
    Oh no!
    You now trying to start server wihtout runner script!
    (by defalut it is main.py)
    """)
