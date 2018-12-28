# -*- coding: UTF-8 -*-
from commen.Excel import Reader,Writer
import inspect
from keywords.HTTP import Http


#反射获取关键字
def getfunc(line,http):
    #http = Http()
    func=None
    try:
    # func=getattr(Http,a)
    # print(func)
    # func(http,'http://112.74.191.10:8081/inter/HTTP/auth')
        func = getattr(http, line[3])
    except Exception as e:
        print(e)

    return func
#反射获取参数
def getargs(func):
    args=inspect.getfullargspec(func).__str__()
    args=args[args.find('args=')+5:args.find(',varargs')]
    args=eval(args)
    args.remnove('self')
    #print(len(args))

def run(func,lenargs,line):
    #如果没有这个函数，就不执行
    if func is None:
        return
    if lenargs<1:
        func()
        return
    if lenargs<2:
        func(line[4])
        return
    if lenargs<3:
        func(line[4],line[5])
        return
    if lenargs<4:
        func(line[4],line[5],line[6])
        return
    print('error:目前只支持3个参数的关键字')

def runCase():
    reader = Reader()
    writer=Writer()
    http = Http()
    reader.open_excel('../lib/cases/HTTP接口用例.xls')
    writer.copy_open('../lib/cases/HTTP接口用例.xls', '../lib/results/result-HTTP接口用例.xls')

    sheetname = reader.get_sheets()
    # 遍历所有sheet页
    for sheet in sheetname:
        reader.set_sheet(sheet)
    for i in range(reader.rows):
        line=reader.readline()
        #print(reader.readline())
        #如果第一列，第二列有内容就是分组信息
        if len(line[0])>0 or len(line[1])>0:
            pass
        else:
            func=getfunc(line,http)
            lenargs=getargs(func)
            run(func.lenargs,line)