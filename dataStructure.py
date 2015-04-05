import numpy as np
import cv2
import sys
import random
import threading

class Point():
	def __init__(self,x,y,color):
		self.center = (x,y)
		print self.center
		self.radius = 10
		self.color = color


class Node():
	def __init__(self,data):
		self.data = data
		self.next = None
		color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
		self.point = Point(random.randrange(50,450),random.randrange(50,450),color)

class TNode():
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
		self.point = Point(random.randrange(50,450),random.randrange(50,450),color)

class Tree():
	def __init__(self,root=None):
		self.root = None
		self.initialiseImage()
		self.thread = threading.Thread(target = self.drawImage,args=())
		self.thread.start()

	def insertNode(self,tnode):
		if self.root == None:
			self.root = tnode
		else:
			current = self.root
			parent = None
			while current != None:
				parent = current
				if tnode.data < current.data:
					current = current.left
				else:
					current = current.right

			if tnode.data < parent.data:
				parent.left = tnode
			else:
				parent.right = tnode

	def initialiseImage(self):
		size = (w,h,channels) = (500,500,3)
		self.img = np.zeros(size,np.uint8)
		self.img[::] = (255,255,255)


	def preOrderUtility(self,current):
		if current == None:
			return None

		cv2.circle(self.img,current.point.center,current.point.radius,current.point.color,-1)
		cv2.putText(self.img,str(current.data), current.point.center, cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
		
		if current.left != None:
			cv2.line(self.img, current.point.center, current.left.point.center,(0,0,255),2)
		if current.right != None:
			cv2.line(self.img, current.point.center, current.right.point.center,(0,0,255),2)
		self.preOrderUtility(current.left)
		self.preOrderUtility(current.right)


	def drawImage(self):
		while True:
			self.preOrderUtility(self.root)

			cv2.imshow("Result",self.img)
			key = cv2.waitKey(30)
			if key >= 27:
				break
		cv2.destroyAllWindows()


class LinkList():
	def __init__(self,head=None):
		self.head = head
		self.initialiseImage()
		self.thread = threading.Thread(target = self.drawImage,args=())
		self.thread.start()

	def insertNode(self,node):
		if self.head == None:
			self.head = node

		else:
			node.next = self.head
			self.head = node

		#self.drawImage()

	def display(self):
		current = self.head
		while current != None:
			print current.data,"  ",
			current = current.next
		print ""

	def initialiseImage(self):
		size = (w,h,channels) = (500,500,3)
		self.img = np.zeros(size,np.uint8)
		self.img[::] = (255,255,255)

	def drawImage(self):
		while True:
			current = self.head
			prev = None
			while current != None:
				#print "Circle drawn"
				cv2.circle(self.img,current.point.center,current.point.radius,current.point.color,-1)
				cv2.putText(self.img,str(current.data), current.point.center, cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
			
				if prev != None:
					cv2.line(self.img, current.point.center, prev.point.center,(0,0,255),2)

				prev = current
				current = current.next

			cv2.imshow("Result",self.img)
			key = cv2.waitKey(30)
			if key >= 27:
				break
		cv2.destroyAllWindows()

def userChoice(link):
	choice  = 1
	while choice != 0:
		try:
			choice = int(raw_input("1.Add Node 2.Display 0.Exit "))
		except:
			print "Enter a valid choice"
			continue
		if choice == 1:
			try:
				num = int(raw_input("Enter number : "))
				link.insertNode(Node(num))
			except:
				print "Invalid input! Try again"
				continue
		elif choice == 2:
			try:
				link.display()
			except:
				continue
		else:
			print "To exit: Set focus on window and then press any key"
			sys.exit()

if __name__ == "__main__":
	tree = LinkList()
	userChoice(tree)

	