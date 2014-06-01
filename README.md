PictureRanker
=============

To rate a picture collection by selecting between two of them at a time.

Current verion works... minimally:
Select a folder that contains the pictures you want to rank against each other.
Choose between two at a time. Eventually, press 'save'.
Saving the results writes a .csv file into the folder with the pictures.
If you don't want the results file in there, move it manually.
The file contains 3 columns: name-of-file, how-often-displayed, how-many-face-offs-won


TODOs / wish list: (no particular order)
1) settings:
    - read and write settings with gui
    - options for output file
2) evaluation:
    - to have numbers that show how many face offs a certain picture has won is good,
      but what do these numbers mean?
    - button 'evaluate' that issues some histogramms etc., i.e. visuallize.
3) cleverer picture update
    - replace random with method that makes use of gathered information
    - e.g. if picture P has won against picture Q and Q against R, then the probability to
      lk a face off between P and R should be lower (but not zero!) because we intuitively
      expect P to win against R. (In this 3 picture example maybe not. But in a larger
      sample collection... Therefore: choose a sensible probability distribution to work
      with. Poisson of some sort?)
4) implement icon in gui
5) bug when reloading folder?
7) bug with reading .JPG, while no problem with .jpg? (at least on Windows?)
8) correct scaling behavior when rescaling window (instead constant) i.e. make possible to maximize gui
9) write errors to logfile (easier to attack problem when reported... )


To install (at least under linux (at least ubuntu based)):

1st make pictureranker.sh executable
2nd create a symlink so that you can call this PictureRanker from everywhere
from the terminal with $ pictureranker (or whatever name you give the link:)
$ chmod +x pictureranker.sh # make it executable
$ sudo ln -s ..full path to this folder/PictureRanker/pictureranker.sh /usr/local/bin/pictureranker


Cheate sheet:

convert .ui to .py:
pyuic4 qt_designer_name.ui -o my_gui_name.py

Create .exe for (and on) Windows:
pyinstaller -F -w -i gui\pictureranker64.ico -n PictureRanker pictureranker.py
This gives the file PictureRanker.exe
Additionally you need the files settings.stk and about.stk for it to work properly.


