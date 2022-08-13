# pyTubeDownloader
Python script to download video or audio from YT.


Hi,

in order for this program to work you must have python installed on your pc.

Take a look at these guides if you don't have it installed.

Windows:
https://realpython.com/installing-python/#how-to-install-python-on-windows

Linux:
https://docs.python-guide.org/starting/install3/linux/

MacOs:
https://docs.python-guide.org/starting/install3/osx/

********************************************************

Next you need to install "pytube" by typing in the command line:

pip3 install pytube

********************************************************

Now open "ytDownloader.py" as a text file and insert the directory 
in which you want the downloaded file to be saved between the single quotes.
And save.

e.g.
stream.download('D:\Download2\YTDownloads')  <-- this won't probably work on your pc

********************************************************

Once this is done all you have to do is go inside the directory 
where the file "ytDownloader" is saved, from the command line, (CMD or other) and type:

python3 ytDownloader.py "#paste here your link" "#insert here "audio" or "video""


e.g.

Video Download:

python3 ytDownloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "video"  

Only-audio Download:

python3 ytDownloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "audio"  


ENJOY.
