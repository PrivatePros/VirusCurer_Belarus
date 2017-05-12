import os, sys


def is_file_infected(filepath):
	try:
		buffer = open(filepath, 'rb').read()		
		vir_maker = 'BELARUS-VIRUS-MAKER'
		cannabis = '~c~a~n~n~a~b~i~s~~i~s~~n~o~t~~a~~d~r~u~g~'
		if buffer[-11:-7]=='.exe':	
			if vir_maker in buffer and cannabis in buffer:
				return True
	except:
		pass
	return False

def cure_file(filepath):
	buffer = open(filepath, 'rb').read()
	buf_len = len(buffer)
	str_len = buffer[-17:-1].split('.exe')[1][1:]
	file_len = int(str_len)
	file_buf = buffer[buf_len-file_len-18:-18]
	with open(filepath, "wb")as f:
		f.write(file_buf)
		f.close()
	print '\t %s is cured' %filepath
	
	
def get_infected_files():
	infected_files = []
	disks = []
	filecount = 0
	infected_dirs = ['C:\\', 'D:\\', 'E:\\temp\\']
	for ld in infected_dirs:
		list_dirs = os.walk(ld) 
		for root, dirs, files in list_dirs: 
			for d in dirs:			
				filepath = os.path.join(root, d)
				if is_file_infected(filepath):
					infected_files.append(filepath)
			for f in files: 
				filepath = os.path.join(root, f) 
				if is_file_infected(filepath):
					infected_files.append(filepath)
	for cf in infected_files:
		print '\t'+cf
	return infected_files

def main():
	print '[*] Finding infected files..'
	infected_files = get_infected_files()
	if infected_files:
		print '[*] Curing infected files..'
		for filepath in infected_files:		
			cure_file(filepath)
	else:
		print '[*] No file infected by virus Belarus'
	

if __name__=='__main__':
	main()



