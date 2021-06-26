from sklearn import tree
import csv

x = []
y = []

with open('bama2.csv','r',encoding='utf8') as fi :
    data = csv.reader(fi)
    for line in data:
        x.append(line[1:3])
        y.append([line[3]])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
# print(x)
# print(y)
model = int(input('مدل سمند ؟'))
karkard = int(input('میزان کارکرد ماشین ؟'))
newdata = [[model,karkard]]
anser = clf.predict(newdata)
print("میزان ارزش :" , int(anser))