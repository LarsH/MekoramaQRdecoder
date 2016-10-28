import qrtools, os, qrcode
from tiles import tiles

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

def splitLevelData(data):
	ret = []
	while len(data) > 0:
		t = data[0]
		l = tiles[t][1]+1
		ret += [data[:l]]
		data = data[l:]
	return ret

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
	return name, author, splitLevelData(levelData)

def createQR(name, author, levelData):
	levelData = ''.join(levelData)
	rawData = chr(len(name)) + name + chr(len(author)) + author + levelData
	data = HEADER + compress(rawData)
	qrcode.make(data).show()

def printLevel(data):
	assert len(data) == 0x1000, len(data)
	for i in range(16):
		print '<<<', i, '>>>'
		for j in range(16):
			a = i*16 + j*256
			for b in data[a:a+16]:
				print tiles[b[0]][2],
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


def showTileRotations(t):
	F = ''
	for i in range(8):
		F += '\x00'*3 + t + chr(i)
		F += '\x00'*3 + t + chr(i+8)
		F += '\x00'*3 + t + chr(i+12)
		F += '\x00'*(4 + 15*16)
		F += '\x00' * 16 * 16
	createQR('Twisted Zappers', 'LarsH', F)


def testNewTiles():
	F = '\x00'*14
	a = 200
	for i in range(a, a+16):
		if i == 0x1d:
			F += '\x11' + '\x0f' + '\x00'*(14 + 15*16)
		else:
			F += '\x11' + chr(i) + '\x00'*(14 + 15*16)
	createQR('Eden', 'LarsH', F)


def showAllTiles():
	F = ''
	l = [i for i in tiles]
	l.sort()
	i = 0
	for j in range(16):
		s = l[i]
		i = (i+1)%len(l)
		t = s + '\x00'*(tiles[s][1])
		F += '\x00'*3 + t

		s = l[i]
		i = (i+1)%len(l)
		t = s + '\x00'*(tiles[s][1])
		F += '\x00'*3 + t

		s = l[i]
		i = (i+1)%len(l)
		t = s + '\x00'*(tiles[s][1])
		F += '\x00'*3 + t

		F += '\x00'*(4 + 15*16)

	createQR('Tiles', 'LarsH', splitLevelData(F))


#showAllTiles()

#testNewTiles()
#showTileRotations('\x10')

#testGeneration()

#n,a,d = openLevel('cargo.png')
#printLevel(d)

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 2:
		print "Usage:", ' '.join(sys.argv), 'level.png'
		print "Displays the internals of a Mekorama level"
	else:
		n,a,d = openLevel(sys.argv[-1])
		print 'Level: "%s" by "%s"' % (n,a)
		printLevel(d)

