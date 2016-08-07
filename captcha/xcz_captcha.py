from fractions import gcd
from captcha_solver import CaptchaSolver
from PIL import Image
from pytesser import *
import httplib

def result_send(lcm):
	headers = {"Cookie":"PHPSESSID=df2o2eum9rfsaj1asi81tt6vq2"}
	conn = httplib.HTTPConnection('xcz.kr')
	conn.request("GET", "/START/prob/prob_files/prob25_ok.php?lcm=" + str(lcm), '', headers)
	r1 = conn.getresponse()
	data = r1.read()
	if "Failed" not in data:
                print data
	conn.close()

def get_captcha():
	headers = {"Cookie":"PHPSESSID=df2o2eum9rfsaj1asi81tt6vq2"}
	conn = httplib.HTTPConnection('xcz.kr')
	conn.request("GET", "/START/prob/prob_files/prob25_img.php", '', headers)
	r1 = conn.getresponse()
	f = open("./captcha.png", "wb")
	f.write(r1.read())
	f.close()
	conn.close()

def lcm(numbers):
    return reduce(lambda x, y: (x*y)/gcd(x,y), numbers, 1)

while True:
	try:
		get_captcha()
		img = Image.open("./captcha.png")
		img = img.convert("RGB")
		pixdata = img.load()
		for y in xrange(img.size[1]):
			for x in xrange(img.size[0]):
				if pixdata[x, y][0] < 255:
					pixdata[x, y] = (0, 0, 0, 0)
		for y in xrange(img.size[1]):
			for x in xrange(img.size[0]):
				if pixdata[x, y][1] < 255:
					pixdata[x, y] = (0, 0, 0, 0)
		img.save("./captcha.tif")
		image = Image.open("./captcha.tif")
		captcha_string = image_to_string(image)
		captcha_string = captcha_string.replace("XCZ . KR Captcha LCPI(", "")
		captcha_string = captcha_string.replace(")", "")
		captcha_string = captcha_string.replace("\n\n", "")
		captcha = captcha_string.split(", ")
		num1 = long(captcha[0])
		num2 = long(captcha[1])
		lcm_result = lcm((num1, num2))
		result_send(str(lcm_result))
	except:
		continue
