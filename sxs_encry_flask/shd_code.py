#coding:utf-8
import base64
import binascii
#异或算法

def shd_xor(data,key):
	orstr = ''
	for x,y in zip(data,key*(len(data)//len(key)+1)):
		a=ord(x)^ord(y)
		orstr = orstr + chr(a)
	return orstr

#解密
def dec(value,key):
	#base64 转码
	data = base64.b64decode(value)
	
	#异或算法
	orstr = shd_xor(data,key)
	hex_bstr= binascii.unhexlify(orstr)
	return hex_bstr

#加密
def enc(value,key):
	print key
	enstr=binascii.hexlify(value)
	orstr =shd_xor(enstr,key)
	new_str = base64.b64encode(orstr)
	return new_str
	
if __name__ =='__main__':
		
	s = 'U3VrQwVmRCIBbUcGZ0BXdmpAAGVBVAUaQwFjN1MCbzUBZ0ElBGhDcGdAUgNvQARhRFUFa0JyYDBTdWtDBWxEUAVrQnJnQFcFakIAbUBWBRpDAWJGUg5uRQUWRFEFa0JyZ0BRdG5EAGBBVQRuQgBgMVMCakUFYEFcAWxEcGJHVwFqRAVnQVQCGkYGZkVSAWpEAGRHJwBsQgpmRlIBakcGFkVRBGFCC2ZGUgRsMgRgQVEBa0IGZkpRdG5EAGJEVgFoQgJgMVMCakYFZkRSAWtEcGJHVwBvRAVhRFICGkYGZkRSBWpHAGZHJwBsQgZjRFcHb0cGFkVRBG1HBmZCUgZsMgRgQVMBbEcBY0RRdG5EAGJBUgRhQgdgMVMCakQAZEFSAWpEcGJHVwJqRQBhRFUFa0Z3YDZTcw=='

	
	key = 'd7Yq3Ur'
	key2 = 'Gs18dMSP'
	#print dec(s,key)
	ss = '{"code":100,"num":1,"data":[{"id":"238","title":"\u5173\u4e8e\u65b0\u7f51\u94f6\u884c\u5b58\u7ba1\u7cfb\u7edf\u6b63\u5f0f\u4e0a\u7ebf\u7684\u516c\u544a"}]}'
	print enc(ss,key2)
	
