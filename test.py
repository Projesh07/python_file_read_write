
from file_read import FileRead


b=FileRead("hello.txt",'r')

contents=b.file_write()

for content in contents:
	print content
b.file_write()

	
