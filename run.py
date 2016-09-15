import subprocess,sys

banner = sys.argv[1]
host = sys.argv[2]
port = sys.argv[3]

url = sys.argv[4]
urlPort = sys.argv[5]

argsPot = [banner, host, port]
argsWeb = [url, urlPort]

# TODO
# Add nmap parser
# Send output to Splunk?

subprocess.Popen(["python", "honeypot.py"] + argsPot)
subprocess.Popen(["python", "yahpotweb.py"] + argsWeb)
