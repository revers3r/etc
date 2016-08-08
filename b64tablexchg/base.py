import httplib
import urllib
import base64
import time
import string

encrypt_msg = "Yh9/=-^:86/f87Y?]-@L}<_E|*1/=-Xi!\"Hx865C|-}:|*DL*G_i86/f868FX(@g@-Lh|)=D}_93@_18@g9,*3YC$(@P"
headers = {"Cookie":"PHPSESSID=k710udqu4deo7nth7r1r10n7n5",
				"Content-Type":"application/x-www-form-urlencoded"}
base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
st_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/~`!@#$^&*()_-+}[]{|\"\':;,.<>?"
temp_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
'`', '!', '@', 'X', '$', '%', '^', 'Y', '*', '(', ')', '_', 'U', 
'-', '=', '[', ']', '\\', '{', '}', '|', ';', 'L', ':', '{', ',',
 '.', '/', '<', '{', '?', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 
 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'x']
temp_table = ''.join(temp_table[i] for i in range(0, len(temp_table)))
c = ''
for i in range(0, len(encrypt_msg)):
	idx = temp_table.find(encrypt_msg[i])
	c += base64_table[idx]
print c
raw_input()
for x in range(0, len(st_table)):
	for y in range(0, len(st_table)):
		for z in range(0, len(st_table)):
			conn = httplib.HTTPConnection('xcz.kr')
			conn.request("POST", "/START/prob/prob26.php", urllib.urlencode({"encode":st_table[x] + st_table[y] + st_table[z]}), headers)
			r1 = conn.getresponse()
			data = r1.read().split("ENCODE : ")[1][0:4]
			b64 = base64.b64encode(st_table[x] + st_table[y] + st_table[z])
			for i in range(len(data)):
				idx = base64_table.find(b64[i])
				temp_table[idx] = data[i]
			print st_table[x] + st_table[y] + st_table[z]
			print temp_table
			conn.close()

print temp_table
print len(temp_table)