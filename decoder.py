import qrtools, os


def openLevel(imagename):
	qr = qrtools.QR()
	assert(qr.decode('cargo.png'))
	levelData = eval(repr(qr.data)[1:])

	header = levelData[:4]
	print 'Header:', header.encode('hex')

	compressedData = levelData[4:]
	f = open('in.tmp','w')
	f.write(compressedData);
	f.close()
	assert(os.system('./uncompress %u < in.tmp > out.tmp'%len(compressedData)) == 0)
	indata = open('out.tmp').read()
	[l, data] = indata.split('\n',1)
	l = int(l)
	assert l == len(data)
	nameLen = ord(data[0])
	name = data[1:1+nameLen]
	print repr(name)
	authorLen = ord(data[1+nameLen]) + 1
	author = data[2+nameLen:1+nameLen+authorLen]
	print repr(author)

	levelData = data[1+nameLen+authorLen:]
	print hex(len(levelData))
	return name, author, levelData

level = openLevel('cargo.png')
print level
