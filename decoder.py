import qrtools, os

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

	compressedData = levelData[4:]
	data = uncompress(compressedData)

	nameLen = ord(data[0])
	name = data[1:1+nameLen]
	authorLen = ord(data[1+nameLen]) + 1
	author = data[2+nameLen:1+nameLen+authorLen]

	levelData = data[1+nameLen+authorLen:]
	return name, author, levelData

level = openLevel('big.png')
name, author, data = level
print name, author

# Printing only works if level does not contain multiple byte blocks
assert len(data) == 0x1000, "level contains multibyte blocks!"

for i in range(16):
	for j in range(16):
		a = i*16 + j*256
		print data[a:a+16].encode('hex')
	print
