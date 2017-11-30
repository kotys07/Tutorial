def tag_decorator(tag = 'div'):
	def decorator(func):
		def wrapper(name):
			return '<{tag}>{0}<{tag}>'.format(func(name), tag=tag)
		return wrapper
	return decorator

def  decorator(func):
	def  wrapper(name):
		return '<{tag}>{0}<{tag}>'.(func(name), tag=tag)
	return wrapper


@tag_decorator(tag= 'h1')
def prt_text(name : str)
	return "Hello {}".format(name)

print(prt_text())