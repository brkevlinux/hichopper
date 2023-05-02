# Programa HiChopper para Terminal Linux.
# @author: brkevlinux
#----------------------------------------

def chopper():
	print(
		'    _____'
		"\n \_|     |_/ ","-" * len(say),
		"\n  _|  X  |_  '{}'".format(say),
		"\n  |_______| /","-"*len(say),
		"\n    (uO O) /"
		"\n    / -º',"
		"\n   (|___| )"
		"\n    |___|"
		"\n     | | "
		"\n     ^ ^ "
		)
say = input()
if say == 'hello':
	say = 'Oi sou Tony Tony chopper! E esse é o HiChopper.'
	chopper()
else:
	chopper()