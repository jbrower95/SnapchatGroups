Snapchat Groups
----------------
(Implemented using a modified version of PySnap)
https://github.com/martinp/pysnap



How to use:


0. Make sure you have gcc installed. If you don't, just type:

    xcode-select --install

1. Make sure you have pip installed. If you don't have pip, download it...
    
    https://pypi.python.org/pypi/pip

        Q: Do I have pip installed? 
        
        A: Open a terminal and type in pip. Did it do something (Y), or did it say
        command not found?


2. If you don't have the following packages installed, use pip to install them
    (sudo pip install <packagename>)
        - docopt                    v0.6.1
        - pycrypto                   v2.6.1
        - requests                  v2.2.1

3. Clone the directory using
    
    git clone http://github.com/jbrower95/snapchatgroups.git

4. Open this directory on your computer, and open up a terminal.
5. At this point, make a snapchat account for your group.
        Ex:
            Username: John
            Password: Doe
6. Run Brunonia

        ./brunonia -u John -p Doe -w 60

    Notice the 60. That means that the script will wait 60 seconds between
    snapchat fetches. Every cycle, the script will download your snaps, parse them,
    and post them to the group story.

    The bigger this number is, the less likely you are to be banned from using
    snapchat. A good time is about 5 minutes (300)

7. Leave Brunonia Running!

8. If it crashes, or if you get locked out of snapchat, just wait a bit and try again.

