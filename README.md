# YeAHPot: 
Yet Another Honey Pot by jsacco@exploitpack.com

# Description:
Usually HoneyPot projects are made for grabbing malware samples, the purpouse of this project
is to make a honeypot for logging, intercepting and decepting malicious users into sensitive assets
and in order to do that it has a few simple but effective features:

1. Mimic server services by opening the same ports as in the real asset
2. Copy the web server hosted on that asset and serve the content
3. Log all interactions on a pcap file and drop the data into a Syslog server

# How to use:
The following example will open the port 22 for SSH, add the banner, retrieve and serve the login page of Github on port 8080
and bind it to localhost. The process will keep running on the background as a child process.

python run.py "OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.7" localhost 3306 http://github.com 8080

# ToDo List:
1. Nmap + Dynamic copy: As a user of this Honeypot I would like to specify a target and automatically deploy a copy of all the services without the need to specify banners or ports.
2. XML Export: As a user I would like to have the logs in a XML format to be able to import the results into different tools

