import os, sys
import pefile


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
	pe = pefile.PE(filepath)
	str_len = buffer[-20:].split('.exe')[1][1:-1]
	file_len = int(str_len)
	sec_num = len(pe.sections)
	last_sec = pe.sections[sec_num-1]
	vir_offset = last_sec.PointerToRawData+last_sec.SizeOfRawData
	file_buf = buffer[vir_offset:vir_offset+file_len]
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



