# -*- coding: UTF-8 -*-
import requests, json
from commen.Excel import Reader,Writer
import inspect
from keywords.HTTP import Http
class Http:
    def __init__(self):
        self.session = requests.session()
        self.jsonres={}
        self.parms={}
        self.url={}
    #设置地址
    def seturl(self,url):
        #url=''
        if url.startswith('http') or url.startswith('https'):
            self.url=url
        else:
            print('error：url地址不合法')
#封装post方法
    def post(self,path,data=None):
        """"
        代码解释
        """
        if not path.startswith('http'):
            path=self.url+'/'+path
        if data is None or data=="":
            result=self.session.post(path)
        else:
            data=self.__saveparms(data)
            data=self.__todic(data)
            result=self.session.post(path,data=data)
        self.jsonres=json.loads(result.text)

#封装断言（判断结果）
    def assertequals(self,key,value):
        res=''
        try:
            res=(self.jsonres[key])
        except Exception as e:
            print(e)
        if res==str(value):
            print('pass')
        else:
            print('fail')

    def addheader(self,key,value):
        value=self.__saveparms(value)
        self.session.headers[key]=value

    def savejson(self,p,key):
        res=''
        try:
            res=self.jsonres[key]
        except Exception as e:
            print(e)
        self.parms[p]=res

    def __saveparms(self,s):
        for key in self.parms:
            s=s.replace('{'+key+'}',self.parms[key])
        return s

    def __todic(self,s):
        httpparms={}

        param=s.split('&')
        for ss in param:
            p=ss.split('=')
            if len(p)>1:
                httpparms[p[0]]=p[1]
            else:
                httpparms[p[0]]=''
        return httpparms
