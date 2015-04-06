#coding=utf-8

"""
1 定义一个函数func(filename) filename:文件的路径，函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。
"""
def func1(filepath):
    try:
        f=open(filepath,"r")
    except IOError:
        print"file coult not be opened"
        #f.close()
    else:
        content=f.readlines()
        return content
        f.close()
    finally:
        print "123"
        #f.close()
        pass 
print func1("class11.py")

"""
2 定义一个函数func(urllist)   urllist:为URL的列表，例如：['http://xx.com','http://www.xx.com','http://www.xxx.com'...] 

函数功能：要求依次打开url，打印url对应的内容，如果有的url打不开，则把url记录到日志文件里，并且跳过继续访问下个url。
"""
import urllib2
def func2(urllist):
    for i in urllist:
        try:
            u=urllib2.urlopen(i)
        except urllib2.URLError:
            print "url could not be opened"
        else:
            content=u.read()
            #u.close()
            print content
        finally:
            u.close()
        print "123"   
urllist=["http://www.baidu.com","http://www.123dxb123.com"]
func2(urllist)
"""
3 定义一个函数func(domainlist)   domainlist:为域名列表，例如：['xx.com','www.xx.com','www.xxx.com'...]
函数功能：要求依次ping 域名，如果ping 域名返回结果为：request time out，则把域名记录到日志文件里，并且跳过继续ping下个域名。（提示用os模块的相关方法）
"""