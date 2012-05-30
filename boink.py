def showHelp():
	print("Boink - A simple issue management system")
	print("Usage: boink <option> <parameter>\n")
	print("--set-name\tSet your name for use with Boink")
	print("--set-email\tSet your email for use with Boink")
	print("--add or -a\tAdd an issue")
	print("--reply or -r\tReply to an issue")
	print("--close or -c\tClose an issue")
	print("--show or -s\tShow all issues\n")
	print("Check out the details for commands at https://github.com/sankha93/boink\n")

def setname(name):
	if not(os.path.exists(path)):
		os.makedirs(path)
	conffile = open(path+"/name",'w')
	conffile.write(name)
	conffile.close()
	print("Ok! Got your name, " + name + ".")

def setemail(email):
	if not(os.path.exists(path)):
		os.makedirs(path)
	conffile = open(path+"/email",'w')
	conffile.write(email)
	conffile.close()
	print("Ok! Thats your email, " + email + ".")

def add(msg):
	try:
		name = open(path+"/name", 'r').read()
		email = open(path+"/email", 'r').read()
	except IOError:
		print("You have not set your name or email.\n")
		return
	if os.path.exists("issues.boink"):
		issues = pickle.load(open("issues.boink", 'rb'))
	else:
		issues = []
	commit = {'name': name, 'email': email, 'msg': msg}
	issue = [commit]
	issues.append(issue)
	bfile = open("issues.boink", 'wb')
	pickle.dump(issues, bfile)
	bfile.close()
	print("Issue Added: Issue #" + str(len(issues)) + "\n")
	print("From: " + name + " (" + email + ")")
	print("Message: " + msg)

def reply(num, msg):
	try:
		name = open(path+"/name", 'r').read()
		email = open(path+"/email", 'r').read()
	except IOError:
		print("You have not set your name or email.\n")
		return
	if os.path.exists("issues.boink"):
		issues = pickle.load(open("issues.boink", 'rb'))
	else:
		print("There are no issues opened.\n")
		return
	issue = issues [num - 1]
	commit = {'name': name, 'email': email, 'msg': msg}
	issue.append(commit)
	bfile = open("issues.boink", 'wb')
	pickle.dump(issues, bfile)
	bfile.close()
	print("Reply to Issue Added: Issue #" + str(num) + "\n")
	print("From: " + name + " (" + email + ")")
	print("Message: " + msg)

if __name__ == '__main__':
	import sys, os.path, pickle
	path = os.path.expanduser("~/.boink")
	if len(sys.argv) < 2:
		showHelp()
	elif sys.argv[1] == "--set-name":
		setname(sys.argv[2])
	elif sys.argv[1] == "--set-email":
		setemail(sys.argv[2])
	elif sys.argv[1] == "--add" or sys.argv[1] == "-a":
		add(sys.argv[2])
	elif sys.argv[1] == "--reply" or sys.argv[1] == "-r":
		reply(int(sys.argv[2]), sys.argv[3])
	else:
		print("Unknown option.\n")
		showHelp()
