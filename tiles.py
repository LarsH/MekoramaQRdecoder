'''
The keys in the dictionary are the tile character used for coding.
The values are tuples of
	description as a string
	the number of extra bytes as an integer
	the representation of the tile for printing, as a single character
'''
tiles = {
	'\x00' : ('Empty',0, ' '),
	'\x01' : ('Stone',0, '#'),
	'\x02' : ('Brick Red',0, 'X'),
	'\x03' : ('Cracked stone*',0, '#'),
	'\x04' : ('Win',0, 'W'),
	'\x05' : ('Stairs',1,'s'),
	'\x06' : ('Trash*', 0, 't'),
	'\x07' : ('Stone Wedge', 1, '/'),
	'\x08' : ('Grass Wedge*', 1, '/'),
	'\x09' : ('Golden ball*', 0, '*'),
	'\x0a' : ('Metal Win*', 1, 'W'),
	'\x0b' : ('Water', 0, '~'),
	'\x0c' : ('Grass',0, '#'),
	'\x0d' : ('Brick Pillar*',0, 'X'),
	'\x0e' : ('Stone corner*',1, '#'),
	'\x0f' : ('Robot Tap to Walk', 1, 'B'),
	'\x10' : ('Zapper',1, 'Z'),
	'\x11' : ('Draggable', 0, 'd'),
	'\x12' : ('Yellow bricks', 0, 'X'),
	'\x13' : ('Wheel*', 1, 'o'),
	'\x14' : ('Metal Stairs*', 1, '/'),
	'\x15' : ('Metal Corner*', 1, '+'),
	'\x16' : ('Motor', 1, 'm'),
	'\x17' : ('Metal box*', 0, '+'),
	'\x18' : ('Alternative stone*', 0, '#'),
	'\x19' : ('Metal', 0, '+'),
	'\x1a' : ('Robot Turns Right', 1, 'R'),
	'\x1b' : ('Eye',0, '0'),
	#'\x1c' : ('Unknown?',0),
	'\x1d' : ('Alterative stone',1, '#'),
	'\x1e' : ('Slider Corner',1, 'j'),
	'\x1f' : ('Alternative stone pillar*',1,'#'),
	'\x20' : ('Metal Half Pillar', 1, '+'),
	'\x21' : ('Slider Rail', 1, '|'),
	'\x22' : ('Shiny Metal Half Pillar*', 1, '+'),
	'\x23' : ('Stone Pillar', 1, '#'),
	'\x24' : ('Draggable Pillar*', 1, 'd'),
	'\x25' : ('Ball', 0, '*'),
	'\x26' : ('Shiny Metal*', 0, '+'),
	'\x27' : ('Metal Pillar', 1, '+'),
	'\x29' : ('Slider', 1, '='),
	'\x2b' : ('Fence', 1, '_')
	}
