from sklearn.naive_bayes import GaussianNB
import numpy as np
data=np.loadtxt(r"1.txt")
x=data[:,0:-1]
y=data[:,-1]
from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(x, y)
bayes = GaussianNB()
model=bayes.fit(x, y)
pred = model.predict(data_test)
err=pred-target_test
count=[]
for i in err:
    if i==0:
        count.append(i)
rate=len(count)/len(err)*100
print("以自身作为预报的准确率{:.2f}".format(rate),"%")
print()
print()
print("*"*6,"分割线","*"*6)
print("俄罗斯世界杯预测实战，数据集只到2014")
from sklearn.naive_bayes import GaussianNB
import numpy as np
data=np.loadtxt(r"1.txt")
x=data[:,0:-1]
y=data[:,-1]
bayes = GaussianNB()
model=bayes.fit(x, y)
p1=[36,45]#乌拉圭，葡萄牙 1
p2=[13,21]#法国，阿根廷 1
p3=[1,18]#巴西，墨西哥 1
p4=[22,20]#日本，比利时
p5=[34,15]#俄罗斯，西班牙
p6=[28,12]#克罗地亚，丹麦
p7=[38,46]#瑞典，瑞士
p8=[32,24]#哥伦比亚，英格兰
px=[p1,p2,p3,p4,p5,p6,p7,p8]
result=[1,1,1,-1,1,1,1,-1]
preresult=[]
for i in px:
    xNew=np.array([i])
    pred = model.predict(xNew)
    pred=list(pred)
    preresult.append(pred)
preresult=list(np.ravel(preresult))
print(preresult)
print(result)
error=[preresult[i]-result[i] for i in range(len(result))]
count=[]
for i in error:
    if i==0:
        count.append(i)
rate=len(count)/len(error)*100
print(error)  
print("俄罗斯世界杯八强赛正确率{:.2f}".format(rate),"%")
p1=[36,13]#乌拉圭，法国
p2=[1,20]#巴西,比利时
p3=[34,28]#俄罗斯 克罗地亚
p4=[38,24]#瑞典 英格兰
px=[p1,p2,p3,p4]
result=[-1,1,-1,-1]
preresult=[]
for i in px:
    xNew=np.array([i])
    pred = model.predict(xNew)
    pred=list(pred)
    preresult.append(pred)
preresult=list(np.ravel(preresult))
print(preresult)
print(result)
error=[preresult[i]-result[i] for i in range(len(result))]

print(error)  # 误判率怎么求？不为0的就是误判
count=[]
for i in error:
    if i==0:
        count.append(i)
rate=len(count)/len(error)*100
print(error)  # 误判率怎么求？不为0的就是误判
print("俄罗斯世界杯四强赛正确率{:.2f}".format(rate),"%")
p1=[13,20]#法国，比利时
p2=[28,24]#克罗地亚，英格兰
px=[p1,p2]
result=[1,1]
preresult=[]
for i in px:
    xNew=np.array([i])
    pred = model.predict(xNew)
    pred=list(pred)
    preresult.append(pred)
preresult=list(np.ravel(preresult))
print(preresult)
print(result)
error=[preresult[i]-result[i] for i in range(len(result))]

print(error)  
count=[]
for i in error:
    if i==0:
        count.append(i)
rate=len(count)/len(error)*100
print(error)  
print("俄罗斯世界杯半决赛正确率{:.2f}".format(rate),"%")
p1=[13,28]#法国，克罗地亚
px=[p1]
result=[1]
preresult=[]
for i in px:
    xNew=np.array([i])
    pred = model.predict(xNew)
    pred=list(pred)
    preresult.append(pred)
preresult=list(np.ravel(preresult))
print(preresult)
print(result)
error=[preresult[i]-result[i] for i in range(len(result))]


print(error)  
count=[]
for i in error:
    if i==0:
        count.append(i)
rate=len(count)/len(error)*100
print("俄罗斯世界杯决赛正确率{:.2f}".format(rate),"%")
    
