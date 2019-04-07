# Ask Noah Show Kodi Addon

[![Build Status](https://travis-ci.org/xmetalfanx/plugin.video.asknoahshow.svg?branch=krypton)](https://travis-ci.org/xmetalfanx/plugin.video.asknoahshow)


The [Ask Noah Show](http://www.asknoahshow.com/) is a weekly radio call in show where we take your tech questions or business in tech questions live on the air.

The show airs Tuesdays at 6pm CST on asknoahshow.com and at KEQQ 88.3 FM in Grand Forks ND.
It's a free call 1-855-450-NOAH so join us and start on your way to owning your operating system, your software, and technology.

## Install

1. Visit Video Addons
2. Select Get More...
3. Find and select the Ask Noah Show addon

## Other Ways to Listen 

In addition to this addon, you can also listen to The Ask Noah Show, on these platforms 

- ![Apple Podcasts](/resources/media/apple_podcasts.png) [Apple Podcasts](https://itunes.apple.com/us/podcast/id1221193873)
- ![Google Play](/resources/media/google_play.png) [Google Play](https://play.google.com/music/listen?u=0#/ps/Ijeqmhsoa4nwu6deo5u2taul32a)
- ![Overcast](/resources/media/overcast.png) [Overcast](https://overcast.fm/itunes1221193873/ask-noah-show)
- ![Pocket Casts](/resources/media/pocket_casts.png) [Pocket Casts](http://pca.st/rCSw)
- ![Stitcher](/resources/media/stitcher.png) [Stitcher](http://www.stitcher.com/podcast/jupiter-broadcasting/ask-noah)
- ![Tunein](/resources/media/tunein.png) [Tunein](http://tunein.com/radio/Ask-Noah-p982132/)

Or paste the following URL into your favorite podcast app [https://podcast.asknoahshow.com/rss](https://podcast.asknoahshow.com/rss)

## Development

### Environment
* Requires make, python pip, and virtualenv
```bash
$ sudo apt-get install python-pip
$ pip install virtualenv
```
* Clone plugin into Kodi Addons folder, this is sufficient for use/testing
```bash
$ cd ~/.kodi/addons/
$ git clone git@github.com:JupiterBroadcasting/plugin.video.jupiterbroadcasting.git
```
* Setup development environment
```bash
$ make venv
$ source venv/bin/activate
```
* Run unit tests
```bash
$ make tests
```
* Exit virtual env
```bash
$ deactivate
```


### Tools

* [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) for consistent styles
* [Pylint](http://pylint.org)


## About

* Host: [Noah J. Chelliah](mailto:live@asknoahshow.com)

* This is an addon that has been forked from the [Jupiter Broadcasting Kodi Addon](https://github.com/JupiterBroadcasting/plugin.video.jupiterbroadcasting) by [Rob Loach](http://robloach.net) and others.  
  
* Author: [Rob Loach](http://robloach.net)

* Source: [GitHub](https://github.com/Xmetalfanx/plugin.video.asknoahshow)
