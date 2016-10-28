import qrtools, os, qrcode

HEADER = '01130dfc'.decode('hex')

def compress(compressedData):
	f = open('in.tmp','w')
	f.write(compressedData);
	f.close()
	assert(os.system('./compress %u < in.tmp > out.tmp'%len(compressedData)) == 0)
	indata = open('out.tmp').read()
	[l, data] = indata.split('\n',1)
	l = int(l)
	assert l == len(data)
	return data

def uncompress(compressedData):
	f = open('in.tmp','w')
	f.write(compressedData);
	f.close()
	assert(os.system('./uncompress %u < in.tmp > out.tmp'%len(compressedData)) == 0)
	indata = open('out.tmp').read()
	[l, data] = indata.split('\n',1)
	l = int(l)
	assert l == len(data)
	return data

def openLevel(imagename):
	qr = qrtools.QR()
	assert(qr.decode(imagename))
	levelData = eval(repr(qr.data)[1:])

	header = levelData[:4]
	#print 'Header:', header.encode('hex')
	assert header == HEADER, repr((header, HEADER))

	compressedData = levelData[4:]
	data = uncompress(compressedData)

	nameLen = ord(data[0])
	name = data[1:1+nameLen]
	authorLen = ord(data[1+nameLen]) + 1
	author = data[2+nameLen:1+nameLen+authorLen]

	levelData = data[1+nameLen+authorLen:]
	return name, author, levelData

def createQR(name, author, levelData):
	rawData = chr(len(name)) + name + chr(len(author)) + author + levelData
	data = HEADER + compress(rawData)
	qrcode.make(data).show()

def printLevel(data):
	# Printing only works if level does not contain multiple byte blocks
	assert len(data) == 0x1000, "level contains multibyte blocks!"

	for i in range(16):
		for j in range(16):
			a = i*16 + j*256
			print data[a:a+16].encode('hex')
		print

def testGeneration():
	A = '\x01'*16
	B = '\x01' + ('\x00'*14) + '\x01'
	b = '\x01' + '\x0f\x04' + ('\x00'*13) + '\x01'
	C = '\x00' * 16
	D = A + B*14 + A
	E = b + C*14 + B
	F = D + E*12 + D + E + D
	createQR('Big Stone Cube', 'LarsH', F)

testGeneration()
