def showHelp():
	print("Boink - A simple issue management system")
	print("Usage: boink <option> <parameter>\n")
	print("--set-name\tSet your name for use with Boink")
	print("--set-email\tSet your email for use with Boink")
	print("--add or -a\tAdd an issue")
	print("--close or -c\tClose an issue")
	print("--show or -s\tShow all issues\n")
	print("Check out the details for commands at https://github.com/sankha93/boink\n")

def setname(name):
	path = os.path.expanduser("~/.boink")
	if not(os.path.exists(path)):
		os.makedirs(path)
	conffile = open(path+"/name",'w')
	conffile.write(name)
	conffile.close()
	print("Ok! Got your name, " + name + ".")

def setemail(email):
	path = os.path.expanduser("~/.boink")
	if not(os.path.exists(path)):
		os.makedirs(path)
	conffile = open(path+"/email",'w')
	conffile.write(email)
	conffile.close()
	print("Ok! Thats your email, " + email + ".")

if __name__ == '__main__':
	import sys, os.path
	if len(sys.argv) < 2:
		showHelp()
	elif sys.argv[1] == "--set-name":
		setname(sys.argv[2])
	elif sys.argv[1] == "--set-email":
		setemail(sys.argv[2])
	elif sys.argv[1] == "--add" or sys.argv[1] == "-a":
		add(sys.argv[2])
	else:
		print("Unknown option.\n")
		showHelp()
