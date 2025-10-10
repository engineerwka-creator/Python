import os


def incremetal (a):
    b = a + 2
    print (b)


incremetal(5)
incremetal(8)
incremetal(10)

def jabko ():
    print ("gruszka")

jabko ()

print ("gruszka")

def find (destination, extention):
    for name in os.listdir(destination):
        extentionLenght = len (extention)
        if name[-extentionLenght:] == extention:
        #print (name[-extentionLenght:])
            print (name)
    print (os.listdir(destination))
find ("c:\\Users\\engin", "ini")
find ("c:\\Windows", "exe")
find ("C:\\Users\\engin\\PycharmProjects\\PythonPoradnik","4.py")

def find (destination, extention):
    for name in os.listdir(destination):
        extentionLenght = len (extention)
        if name[-extentionLenght:] == extention:
        #print (name[-extentionLenght:])
            print (name)
    print (os.listdir(destination))
find ("c:\\Windows", "dat")
