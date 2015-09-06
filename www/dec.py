import functools


def log(text):
	def dec(func):
		@functools.wraps(func)
		def wraper(*arg, **kw):
			print('%s %s()' %(text, func.__name__))
			print('func begin')
			ret=func(*arg,**kw)
			print('func end')
			return ret
		return wraper
	return dec



@log('execute')
def now():
	print('hello world')


now()



