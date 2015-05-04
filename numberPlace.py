# coding: utf-8

# Python2.X encoding wrapper (Windows dedicated processing)
import codecs
import sys
import random
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

cells=[[0 for i in xrange(9)]for j in xrange(9)]

def solve(_row,_col):
	if _row==9:
		return True
	if cells[_row][_col]!=0:
		if solve(_row+1 if _col==8 else _row,(_col+1)%9):
			return True
	else:
		randoms=setRandoms()
		for i in xrange(9):

			if checkRowandCol(_row,_col,randoms[i])==False and check3x3box(_row,_col,randoms[i])==False:
				cells[_row][_col]=randoms[i]
				if solve(_row+1 if _col==8 else _row,(_col+1)%9):
					return True
				else:
					cells[_row][_col]=0;
	return False

def setRandoms():
	randoms=[]
	for i in xrange(9):
		randoms.append(i+1)
		random.shuffle(randoms)
	return randoms

def checkRowandCol(_row,_col,_value):
	for i in xrange(9):
		if i!=_col:
			if cells[_row][i]==_value:
				return True
		if i!=_row:
			if cells[i][_col]==_value:
				return True
	return False

def check3x3box(_row,_col,_value):
	startRow=_row/3*3
	startCol=_col/3*3

	for i in  xrange(startRow,startRow+3):
		for j in xrange(startCol,startCol+3):
			if i==_row and j==_col:
				if cells[i][j]==_value:
					return True
	return False