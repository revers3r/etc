from socket import *
import time
import string
import random
import thread

m_Vars = {
	"bufLen" : 1024 * 10,
	"defaultServerIp" : "192.168.137.23",
	"defaultServerPort" : 554,
	"defaultTesturl" : "rtsp://192.168.137.23/",
}

def msg_describe(url, seq):
	msg = "DESCRIBE " + url + " RTSP/1.0\r\n"
	msg += "CSeq: " + str(seq) + "\r\n"
	msg += "Accept: application/sdp\r\n"
	msg += "\r\n"
	return msg

def send_payload():
	s = socket(AF_INET, SOCK_STREAM)
	s.connect((m_Vars["defaultServerIp"], m_Vars["defaultServerPort"]))
	s.send(msg_describe(m_Vars["defaultTesturl"], 1))
	time.sleep(5)
	print s.recv(2048)
	s.close()

send_payload()