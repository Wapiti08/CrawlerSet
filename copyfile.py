#大作业
#在某个路径的文件夹下
#将1000多个文件（文件类型不能只有文本类型）
#拷贝到另一个文件夹下；需要有进度条
#注：怎么证明你拷贝的文件是没有错误的？

#在进行工程的创建时，尽量把函数封装的小一点，避免臃肿

from multiprocessing import Pool,Manager
import os
import hashlib

CHUCKSIZE=4096
def hashFile(fileName):
    with open(fileName,'rb') as a:
        #循环读取，这是基础呀
        while True:
            data=a.read(CHUCKSIZE)
            if not data:
                #如果没有数据就跳出循环
                break
            m=hashlib.sha256()
            m.update(data)
    return m.hexdigest()

def innerCopy(fileName,srcpath,despath,q):
     #拼凑出拷贝的源和目标路
    srcfileName=srcpath+'/'+fileName
    desfileName=despath+'/'+fileName
    #开始拷贝文件
    with open(srcfileName,'rb') as fr:
        #这里是写入二进制文件，不是读r呀
        with open(desfileName,'wb') as fw:
            for i in fr:
                fw.write(i)
    q.put(fileName) #向进程池的队列中放入拷贝完的文件，相对于的还有个get操作

    return True

def copyFile(fileName,srcpath,despath,q):
    '''
    拷贝文件的方法
    '''
    #不仅要判断目标文件路径存在与否，还要对源文件夹进行判断
    if not os.path.exists(srcpath):
        #只能放弃了，谈不上在创建啥的
        print("srcPath %s is not existing"%(srcpath))
        return None

    #通过测试以后发现没有目标程序，所以一定要在这之前有个判断
    if not os.path.exists(despath):
        try:
            os.mkdir(despath)
        except:
            print("make %s error"%(despath))
            return None
    
    return innerCopy(fileName,srcpath,despath,q)


if __name__=="__main__":
    srcPath=input("请输入您要拷贝的文件目录")
    desPath=srcPath+'-副本'
    #因为涉及到拷贝的覆盖，所以需要对文件名或者
    # 路径下的文件是否已经存在进行判断
    while os.path.isdir(desPath):
        desPath=desPath+'-副本'

    #遍历源文件夹，获取当前文件夹中所有的文件名
    #及统计其文件个数
    allFiles=os.listdir(srcPath)
    allNum=len(allFiles)
    num=0 #记录当前完成的文件个数

    #进程池
    p=Pool()
    #构造进程池之间的通信队列,无论对于manager中的队列还是大写的队列
    #都不用考虑加锁，因为已经考虑了，属于进程和线程间的队列
    q=Manager().Queue()
    #通过进程池的调度来完成任务的执行
    for i in allFiles:
        p.apply_async(func=copyFile,args=(i,srcPath,desPath,q))
    #通知进程池任务添加结束
    p.close()   
     
    #使用主进程来充当监工的角色，来监控文件的拷贝进程
    while num<allNum:   #判断文件是否已经拷贝完成
        q.get()   #阻塞在这里，直到接受到信号
        num+=1
        rate=num/allNum*100

    #做文件hash值得检测
    srcfileName=srcPath+'/'+fileName
    desfileName=desPath+'/'+desName

    if hashFile(srcfileName)==hashFile(desfileName):
        print("%s copy is OK"%srcfileName)
    else:
        print("%s copy is not OK"%srcfileName)


    print("拷贝进度为%.1f%%"%rate)
    #等待进程池完成所有的拷贝任务
    p.join()
    print("Copy files done")