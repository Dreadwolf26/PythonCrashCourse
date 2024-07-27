import aspose.words as aw

"""This is a free version of the apose words this will not convert an entire document. 
It was used for testing puposes and its simple syntax"""

#Takes input of PDF document
doc = aw.Document("python-crash-course.pdf")
#Saves it as a text document
doc.save("python_crash_course.txt")