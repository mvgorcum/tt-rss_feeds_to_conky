# Python script to read tt-rss api and conky config to display

A simple python script that can be called from the commandline that displays article tiles for Tiny Tiny RSS.
You'll need to edit the variables for username, password and server (obviously) in the python script.

To call the script run:  
` python /path/to/script/main.py "title of the feed" <maximum number of article titles to display> `

To run this in conky use the execi command, I'd recommend to not set the interval time too low, since you'll just be making useless api calls often. I have it set to 10 minutes (ie. 600 seconds).  
Mine looks like this:  
`${execi 600 python /home/mathijs/Conky/ttrss_api/main.py "Ars Technica" 5 | fmt -s -w 60 -g 60}`

The conky config available in the repo and shown in the screenshot is based on the config made by [/u/RedPacketSecurity](https://www.reddit.com/user/RedPacketSecurity) posted on reddit [here](https://www.reddit.com/r/Conkyporn/comments/5x6gq7/my_conky_config/), available [here](http://pastebin.com/vRiYGWhz).

Screenshot of an example:
![screenshot](https://raw.githubusercontent.com/mvgorcum/tt-rss_feeds_to_conky/master/Screenshot_20170321_013300.png)
