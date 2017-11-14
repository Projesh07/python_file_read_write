

class FileRead(object):
	
	def __init__(self, file_to_read=None,file_open_mode=None,stream_size=100):
		
		super(FileRead, self).__init__()
		self.file_to_read = file_to_read
		self.file_to_write='test.txt'
		self.file_mode=file_open_mode
		self.stream_size=stream_size


	def file_read(self):
		try:
			with open(self.file_to_read,self.file_mode) as file_context:
				contents=file_context.read(self.stream_size)
				while len(contents)>0:
					yield contents
					contents=file_context.read(self.stream_size)

		except Exception as e:

			if type(e).__name__=='IOError':
				output="You have a file input/output error  {}".format(e.args[1])
				raise Exception (output)
			else:
				output="You have a file  error  {} {} ".format(file_context.name,e.args)	 
				raise Exception (output)
	def file_write(self):
		try:
			
			with open(self.file_to_write,'w') as write_file_context:
				contents=self.file_read()
				for content in contents:
					write_file_context.write(content)

		except Exception as e:
			raise e		

										



		


		
		