from urllib import request
import random
from infoForModuleMethods import info
from urllib import error


def downloadHtml(url,headers=[],proxy={},timeout=None,decodeinfo='utf-8',num_retries=5):
    """
      这是一个爬取网页的函数
      它支持设置ua:在headers中加入，以list
      支持代理服务器，参数需要返回一个dict
      返回的状态码不是200
      timeout可以定义超时时间
      decodeInfo指定网页编码
      num_retries 最大尝试次数
    """
    #通过随机的策略去调整使用代理服务器的概率
    if random.randint(1,10)>=6:
        proxy=None
        print("no proxy")
    #创建proxyhandler
    proxy_support=request.ProxyHandler(proxy)

    opener=request.build_opener(proxy_support)

    opener.addheaders=headers

    request.install_opener(opener)

    info(opener.addheaders)

    #因为涉及到可能打不开的情况
    try:
        res=request.urlopen(url,timeout=5)
        html=res.read().decode(decodeinfo)
    except UnicodeDecodeError:
        html=None
        print("UnicodeDecodeError")
    except error.URLError or error.HTTPError as e:
        print("Download Error")
        html=None
        if num_retries>0:
            #如果状态码在[500,600)的范围之内，
            #继续尝试
            time.sleep(random.randint(1,3))
            #hasattr(object, name)
            if hasattr(e,'code') and 500<=e.code<=600:
                #这里是一个递归调用，所以要有变量的变化
                html=downloadHtml(url,headers,proxy,timeout,decodeinfo,num_retries-1)
    return html

if __name__=="__main__":
    headers=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')]
    # proxy={'http':'xxx'}
    print(downloadHtml("http://www.baidu.com",headers=headers))
