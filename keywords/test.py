import requests,json
from keywords.HTTP import Http
import inspect

# a='[1,2]'
# b=eval(a)
# print(b)
#反射获取方法
a='post'
http=Http()
# func=getattr(Http,a)
# print(func)
# func(http,'http://112.74.191.10:8081/inter/HTTP/auth')
func=getattr(http,a)
func('http://112.74.191.10:8081/inter/HTTP/auth')
#
# args=inspect.getfullargspec(func).__str__()
# args=args[args.find('args=')+5:args.find(',varargs')]
# args=eval(args)
# args.remnove('self')
# print(len(args))
# print(func.__doc__)
