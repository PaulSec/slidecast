Slidecast
=================

Litte utility to do a slideshow of a specific directory on a Chromecast. 

Installation
=================

Clone the repository locally. 

```
git clone <url>
```

Then, install the dependencies (in this case, just one: [pychromecast](https://github.com/balloob/pychromecast))

```
pip install -r requirements.txt
```

Usage
=================

Simply type: 

```
python slidecast.py
```

Then, the usage will come up: 

```
$ python slidecast.py 
Usage: slidecast.py [options]

Options:
  -h, --help            show this help message and exit
  -f FOLDER, --folder=FOLDER
                        Folder to show
  -c CHROMECAST, --chromecast=CHROMECAST
                        Name of the Chromecast you want to interact with
  -p PORT, --port=PORT  Port to fire up the web server (default: 8000)
  -d DELAY, --delay=DELAY
                        Delay to dispay the pictures (default: 10s)
  -v, --verbose         Verbose mode

```

A way to use it: 

```
$ python slidecast.py  -f /media/paul/689C63BQ9C53750B/photos/ -v -p 8088
Internal ip found: 192.168.0.11
Scanning Chromecasts...
Serving Web server on port 8088
Using Chromecast Badaboum
temp_url: http://192.168.0.11:8088/DSCN0281.JPG
192.168.0.17 - - [08/Dec/2016 17:21:51] "GET /DSCN0281.JPG HTTP/1.1" 200 -
temp_url: http://192.168.0.11:8088/DSCN0282.JPG
192.168.0.17 - - [08/Dec/2016 17:22:01] "GET /DSCN0282.JPG HTTP/1.1" 200 -
temp_url: http://192.168.0.11:8088/DSCN0283.JPG
192.168.0.17 - - [08/Dec/2016 17:22:11] "GET /DSCN0283.JPG HTTP/1.1" 200 -
temp_url: http://192.168.0.11:8088/DSCN0284.JPG
192.168.0.17 - - [08/Dec/2016 17:22:21] "GET /DSCN0284.JPG HTTP/1.1" 200 -
temp_url: http://192.168.0.11:8088/DSCN0285.JPG
192.168.0.17 - - [08/Dec/2016 17:22:31] "GET /DSCN0285.JPG HTTP/1.1" 200 -
temp_url: http://192.168.0.11:8088/DSCN0286.JPG
192.168.0.17 - - [08/Dec/2016 17:22:41] "GET /DSCN0286.JPG HTTP/1.1" 200 -
```

The scripts detects the internal private IP, fires up a HTTP server (to serve the pictures to the Chromecast), lists the Chromecasts on the private network and picks the one you chose (or the only one on your network if that's the case) and interacts with it.

License
=================

I released this tool under MIT License. Fork it and have fun with it! Cheers