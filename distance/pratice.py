#此类是读取dat，并分析dat文件中所有的点离（x,y）距离的类
class Distance():
    #初始化函数
    def __init__(self,path,x,y):
        self.a=input('请输入一个距离：')
        self.lines=self.readDat(path)
        self.x = x
        self.y = y
        
    #改造print函数
    def upPrint(self,s):
        print(s)
        print('*************************************************')
        
        
    #读取dat文件，并存入一个数组里面
    def readDat(self,filePath):
        f = open(filePath,'r')
        lines = f.readlines()
        self.upPrint("xyz.dat中共有%s行记录"%len(lines))
        return lines
    
    #*********************************************************************
    
    #读取每行数据，并处理
    def exceLine(self,line):
        name = line.split(',')[0]
        x = line.split(',')[1]
        y = line.split(',')[2]
        xy = ((float(x)-self.x)**2+(float(y)-self.y)**2)*0.5
        return name,x,y,xy
        
    #***********************************************************************
    #判断坐标是否在距离之内
    def isInclude(self,**info):
        if info['distance']>float(self.a):
            self.upPrint('点%s的在距离之外'%info['mingzi'])
        elif info['distance']==float(self.a):
            self.upPrint("")
        else:
            self.upPrint('点%s在距离之内'%info['mingzi'])
            
            
    #****************************************
    def run(self):
        for line in self.lines:
            name,x,y,xy=self.exceLine(line)
            self.upPrint('点名是:%s,x是:%s,y是%s,距离是:%s'%(name,x,y,xy))
            self.isInclude(distance=xy,mingzi=name)
    
        