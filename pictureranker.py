#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import os

import numpy as np

from PyQt4 import QtCore, QtGui
from gui.mainWindow import Ui_MainWindow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ranker(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(Ranker, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Picture Ranker')
        self._flist = {} # {'filename1': [n1_displayed, n1_selected], 'filename2': [n2_displayed, n2_selected]}
        self._N = len(self._flist)
        self._right_picture = ''
        self._left_picture = ''
        self._dir = '.'
        self._outfilename = self.full_path('pictureranker.csv')
        self._accepted_file_ext = []
        
        self._read_settings()
        
        ########################################
        #         picture platform
        ########################################
        self.canvas_left = QtGui.QGraphicsScene()
#        self.canvas_left.installEventFilter(self) # handels the mouse coords, see def eventFilter
        self.graphic_left.setScene(self.canvas_left)
        self.canvas_right = QtGui.QGraphicsScene()
        self.graphic_right.setScene(self.canvas_right)
        ########################################
        
        ########################################
        #         interaction
        ########################################
        self.connect(self.folderloader, QtCore.SIGNAL("clicked()"), self._open_folder)
        self.connect(self.readbutton, QtCore.SIGNAL("clicked()"), self._open_file)
        self.connect(self.savebutton, QtCore.SIGNAL("clicked()"), self._write_results)
        self.connect(self.selectleft, QtCore.SIGNAL("clicked()"), self._update_pictures_left)
        self.connect(self.selectright, QtCore.SIGNAL("clicked()"), self._update_pictures_right)
        ########################################
        
#        self._load_picture('left', 'left.png')
#        self._load_picture('right', 'right.png')
        
    def full_path(self,path):
        return '{0}/{1}'.format(self._dir,path)
    def only_path_name(self,full_path):
        return full_path.split('/')[-1]
    
    ##############################################
    #                statistics
    ##############################################
    def _count_displayed(self,path):
        self._flist[path][0] +=1
    def _count_selected(self,path):
        self._flist[path][1] +=1

        
    ##############################################
    #                picture handling
    ##############################################
    def _load_picture(self, side, path):
        # path: just filename, internally converted to full_path
        if side == 'left':
            canvas = self.canvas_left
            canvas.clear()
            self._left_picture = path
        elif side == 'right':
            canvas = self.canvas_right
            canvas.clear()
            self._right_picture = path
        pixmap = QtGui.QPixmap(_fromUtf8(self.full_path(path)))
        pixmap = self._scale_pixmap(pixmap)
        canvas.addPixmap(pixmap)
        
    def _scale_pixmap(self, pixmap):
        old_height = pixmap.height()
        old_width = pixmap.width()
        old_ratio = old_width*1.0/old_height
        # QGraphicsView (aka self.graphic_left/right) provides space for 470x500
        # want same scaling for h and w: choose smaller that still fits
        max_height = 500-2
        max_width = 470-2
        max_ratio = max_width*1.0/max_height
        if old_ratio>=max_ratio: # wider than height => fix width
            new_height = int(max_height*1.0/old_ratio)
            new_width = max_width
        else:
            new_height = max_height
            new_width = int(max_width*old_ratio)
        return pixmap.scaled(new_width, new_height)
        
    def _update_pictures_left(self):
        self._update_pictures('left')
    def _update_pictures_right(self):
        self._update_pictures('right')
        
    def _update_pictures(self, which):
        self.statuslabel.setText('pending')
        # handle current display and selection
        path_left = self._left_picture
        path_right = self._right_picture
        if (path_left!='' and path_right!=''):
            self._count_displayed(path_left)
            self._count_displayed(path_right)
            if which=='left': path_selected = path_left
            elif which=='right': path_selected = path_right
            self._count_selected(path_selected)
        # what to display next, select two new:
        #smart selection:
        # as long as not yet all once tested, select these.
        # when all at least once accounted for select at random
        # but: bias random through smart statistical measure...
        rndl, rndr = np.random.randint(self._N), np.random.randint(self._N)
        while (rndl==rndr): rndr = np.random.randint(self._N) # make sure they're different
        self._left_picture = self._flist.keys()[rndl]
        self._right_picture = self._flist.keys()[rndr]
        self._load_picture('left',self._left_picture)
        self._load_picture('right',self._right_picture)
        
        
    ##############################################
    #                open
    ##############################################
    def _open_folder(self):
        _dir = QtGui.QFileDialog.getExistingDirectory(self, directory=self._dir)
        if _dir!='': # i.e. actually something selected
            self._dir = _dir
            self.folderlabel.setText('Folder: ..{0}'.format(self._dir[-min([len(self._dir),100]):]))
            self.folderloader.setText('Folder selected')
            self._outfilename = self.full_path(self.only_path_name(self._outfilename))
            # load filenames / init the list
            elements_in_dir=os.listdir(self._dir)
            for f in elements_in_dir:
                if f.split('.')[-1].lower() in self._accepted_file_ext:
                    self._flist[f]=[0,0]
            self._N = len(self._flist)
            
    def _open_file(self):
        self._outfilename = QtGui.QFileDialog.getOpenFileName(self, directory=self._dir)#, filter='(*.csv *.txt)')
        self._read_results()
            
    ##############################################
    #                result file
    ##############################################
    def _read_results(self):
        with open(self._outfilename, 'rb') as f:
            for r in f:
                rr = r.split(',')
                assert len(rr)==3, 'Input data looks different than expected.'
                rr[1], rr[2] = int(rr[1]), int(rr[2])
                print rr
            
    def _write_results(self):
        with open(self._outfilename, 'wb') as f:
            for entry in self._flist:
                f.write('{0},{1},{2}\n'.format(entry,
                                               self._flist[entry][0],
                                               self._flist[entry][1]))
        self.statuslabel.setText('saved')
        
    ##############################################
    #                Picture Ranker settings
    ##############################################
    def _read_settings(self):
        if os.path.exists('.prsettings'):
            with open('.prsettings', 'rb') as s:
                for r in s:
                    rr = r.split('=')
                    if rr[0]=='home_directory':
                        self._dir = rr[1][:-1]
                    if rr[0]=='output_file':
                        self._outfilename = self.full_path(rr[1][:-1])
                    if rr[0]=='file_types':
                        self._accepted_file_ext = rr[1].split(',')
                        self._accepted_file_ext[-1] = self._accepted_file_ext[-1][:-1] # remove '\n'
#    def _write_settings(self):
#        pass
    

def main():
    app = QtGui.QApplication(sys.argv)
    form = Ranker()
    
    form.showNormal() #showMaximized()
    app.exec_()

if __name__ == "__main__":
    main()