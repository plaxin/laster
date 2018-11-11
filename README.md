# laster

Use currently playing track as status in VK.com

Fork of [lastrm2vkstatus](https://github.com/DiSonDS/lastfm2vkstatus) repository.

## Requirements
-   pylast
-   vk_api

## Setup

### Last.fm
1.  Allow access to your profile here: <https://vk.cc/8GIIAx>
2.  Complete the **settings.py** with last.fm username, password

### VK.com
1.  Obtain your access token: <https://vk.cc/8GIGDH>
2.  Complete the **settings.py** with token
3.  Optionally, enter custom text for the status. For a track, don't forget `{track}` variable...

## Usage

```console
python3 laster.py
```
![Screenshot](screenshot.png)
