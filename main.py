from Stitcher.panorama import Stitcher
import argparse
import imutils
import cv2
import Tkinter
import tkMessageBox
from Tkinter import *
def stitch():
	first = E1.get()
	sec = E2.get()
	vc = cv2.VideoCapture(first + '.mp4')
	c=1

	if vc.isOpened():
    		rval , frame = vc.read()
	else:
    		rval = False

	while rval:
    		rval, frame = vc.read()
    		cv2.imwrite("Test1-" + str(c) + '.jpg',frame)
    		c = c + 1
    		cv2.waitKey(1)
	no_frames1=c
	vc.release()

	vc = cv2.VideoCapture(sec + '.mp4')
	d=1

	if vc.isOpened():
    		rval , frame = vc.read()
	else:
    		rval = False

	while rval:
    		rval, frame = vc.read()
    		cv2.imwrite("Test2-" + str(d) + '.jpg',frame)
   		d = d + 1
   		cv2.waitKey(1)
	no_frames2=d;
	vc.release()
	if no_frames1<no_frames2:
    		min1 = no_frames1
	else:
   		 min1 = no_frames2
	stitcher = Stitcher()
        print "Frames extracted"
	for i in range(1,min1-1):
   		imageA = cv2.imread("Test1-" + str(i) + ".jpg")
		imageB = cv2.imread("Test2-" + str(i) + ".jpg")
		imageA = imutils.resize(imageA, width=400)
		imageB = imutils.resize(imageB, width=400)

# stitch the images together to create a panorama
	
		(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
# show the images
#cv2.imshow("Image A", imageA)
#cv2.imshow("Image B", imageB)
#cv2.imshow("Keypoint Matches", vis)
#cv2.imshow("Result", result)
		cv2.imwrite("result" + str(i) + ".jpg",result)

	cv2.waitKey(0)

	img1 = cv2.imread("result1.jpg")
	height , width , layers =  img1.shape
	fourcc = cv2.cv.CV_FOURCC(*'XVID')
	video = cv2.VideoWriter('output.avi',fourcc,60,(width,height))
	video.write(img1)
	for i in range(2,min1-1):
		img = cv2.imread("result" + str(i) + ".jpg")
		video.write(img)



	cv2.destroyAllWindows()
	video.release()



def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
def printCredits():
   '''
   w = Label(root, text = "Developed by Ansia Inc.\nVersion 1.0", width=50,height=25, background="orange",fg="blue")
   w.config(font=(15))
   root.title("About Us")
   w.pack()
   '''
   filewin1 = Toplevel(root)
   text = Text(filewin1)
   #text.insert("Developed")
   text.insert(INSERT, "\t\t\tDeveloped by Ansia Inc.\n")
   text.insert(END, "\t\t\t\tVersion 1.0")
   text.pack()
'''
def getInput():
   first=E1.get()
   sec=E2.get()
   stitch()
   #execfile("finalstitch.py")
'''
root = Tk()
root.title("Video Stitching")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
'''
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
'''
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Content", command=donothing)
helpmenu.add_command(label="About Us", command=printCredits)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
ext = Label(root, text=".mp4")
ext1 = Label(root, text=".mp4")
L1 = Label(root, text="First Video Name: ")
#L1.pack( side = LEFT)
L1.grid(row=0, column=0)
E1 = Entry(root, bd =5)
E1.grid(row=0, column=1)
ext.grid(row=0, column=2)
#E1.pack(side = RIGHT)

L2 = Label(root, text="Second Video Name: ")
#L2.pack( side = LEFT)
L2.grid(row=1, column=0)
E2 = Entry(root, bd =5)
E2.grid(row=1, column=1)
ext1.grid(row=1, column=2)
#E2.pack(side = LEFT)
but1 = Button(root, text="Process", command=stitch)
but1.grid(row=2, column=1)
root.mainloop()
