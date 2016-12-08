import time
import pychromecast
import mimetypes
import sys
import os
import socket
import signal
import SimpleHTTPServer
import SocketServer
import threading
from optparse import OptionParser

VERBOSE_MODE = False
PORT = 8000
FOLDER = ''

def display_message(message):
    if VERBOSE_MODE:
        print message


def get_internal_ip(): 
    return ([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])


def signal_handler(bla, frame):
    print 'Killing Slidecast (and its subprocesses)!'
    os.kill(os.getpid(), signal.SIGKILL)


def display_pictures(options):
    internal_ip = get_internal_ip()
    display_message("Internal ip found: {}".format(internal_ip))


    display_message("Scanning Chromecasts...")

    chromecasts = pychromecast.get_chromecasts_as_dict().keys()
    if len(chromecasts) > 1 and not options.chromecast:
        print "Chromecasts availables: {}".format(chromecasts)
        print "Specify the Chromecast you're looking for"
        sys.exit(-1)

    chromecast_name = options.chromecast or chromecasts[0]
    cast = pychromecast.get_chromecast(friendly_name=chromecast_name)
    display_message("Using Chromecast {}".format(chromecast_name))

    cast.wait()
    mc = cast.media_controller

    files = (file for file in os.listdir('.')
             if os.path.isfile(os.path.join('.', file)))
    for file in files:
        tmp_file = '{}/{}'.format(options.folder, file)
        mime_type = mimetypes.MimeTypes().guess_type(tmp_file)[0]

        # only images are shown
        if ('image' in mime_type):
            #display_message("{} > {}".format(file, mime_type))
            temp_url = "http://{}:{}/{}".format(internal_ip, options.port, file)
            display_message("temp_url: {}".format(temp_url))
            mc.play_media(temp_url, mime_type)
            mc.pause()
            time.sleep(options.delay)
            mc.play()


def http_server():
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    os.chdir(FOLDER)
    display_message("Serving Web server on port {}".format(PORT))
    httpd.serve_forever()


def main():
    global VERBOSE_MODE, PORT, FOLDER

    parser = OptionParser()
    parser.add_option("-f", "--folder", dest="folder", help="Folder to show", default=None)
    parser.add_option("-c", "--chromecast", dest="chromecast", help="Name of the Chromecast you want to interact with", default=None)
    parser.add_option("-p", "--port", dest="port", help="Port to fire up the web server (default: 8000)", default=8000)
    parser.add_option("-d", "--delay", dest="delay", help="Delay to dispay the pictures (default: 10s)", default=10)
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Verbose mode")

    (options, args) = parser.parse_args()

    if options.verbose:
        VERBOSE_MODE = True


    if not options.folder:
        parser.print_help()
        sys.exit(-1)
    FOLDER = options.folder
    os.chdir(FOLDER)

    # starting web server
    PORT = int(options.port)
    thread = threading.Thread(target=http_server)
    thread.daemon = True
    thread.start()

    signal.signal(signal.SIGINT, signal_handler)
    display_pictures(options)

if __name__ == '__main__':
    main()