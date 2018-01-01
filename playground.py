#!/usr/bin/env python
from flask import Flask, render_template
from flask_frozen import Freezer
from playground.utils import options
import sys
import os
import SimpleHTTPServer
import SocketServer

app = Flask(__name__)

@app.route('/')
def show_home():
    return render_template('index.html')

@app.route('/about_me.html')
def about_me():
    return render_template('about_me.html')

if __name__ == '__main__':
    opt = options.get_options()

    if opt.test:
        # Self-test section
        sys.exit(0)
    elif opt.export:
        # Freezer
        freezer = Freezer(app)
        freezer.freeze()
        sys.exit(0)
    elif opt.test_static:
        os.chdir('build')
        PORT = 8000
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", PORT), Handler)
        print("serving at port " + str(PORT))
        httpd.serve_forever()
    else:
        # Hosting the page
        app.run(
            host='0.0.0.0', port=5000, debug=True
        )
