# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:16:39 2018

@author: Administrator
"""

#'a' and 'b'
# b

#'' and 'b'
#''

#'a' and 'b' and 'c'
#'c'

#'a' or 'b'
#'a'

#'' or 'b'
#'b'

#0 and 'a' or 'b'
#'b'

import requests

def info(object, spacing=10):
    """
     Print methods and doc strings. Take module, class, 
     dictionary, or string.
    """
    # 遍历一遍object对象，把里面的可以被调用的方法提取出来
    methodList = [method for method in dir(object) 
                  if callable(getattr(object, method))]
    
    # 把要提取出来的方法以更好看的,多行变单行
    processFunc = lambda s:" ".join(s.split())
    
    # 让左端打印的是方法名称，右端打印的是方法的doc名称
    print('\n'.join(["%s %s"%(str(method.ljust(spacing)), 
          processFunc(str(getattr(object, method).__doc__)))
          for method in methodList]))
    

info(requests)
                  
    
    
    