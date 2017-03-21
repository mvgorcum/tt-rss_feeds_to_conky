# Python script to read tt-rss api and conky config to display

A simple python script that can be called from the commandline that displays article tiles.
You'll need to edit the variables for username, password and server (obviously) in the python script.

To call the script run:
``` python /path/to/script/main.py "title of the feed" <maximum number of article titles to display> ```

To run this in conky use the execi command, I'd recommend to not set the interval time too low, since you'll just be making useless api calls often. I have it set to 10 minutes (ie. 600 seconds).

The conky config available in the repo is based on the config made by [/u/RedPacketSecurity](https://www.reddit.com/user/RedPacketSecurity), available [here](http://pastebin.com/vRiYGWhz)