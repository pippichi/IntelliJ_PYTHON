import numpy as np

data = np.random.randn(160).reshape(80,2)

fileName = 'testSet.txt'
# with open(fileName,'w+') as f:
#     for i in range(data.shape[0]):
#         joinsFrame = data[i]
#         for j in range(len(joinsFrame)):
#             strNum = str(joinsFrame[j])
#             f.write(strNum)
#             f.write(' ')
#             f.flush()
#
# f.close()

# a = np.loadtxt(fileName)
# data = np.reshape(a,(40,2))
np.savetxt(fileName,data)

# dataMat = []
# fr = open(fileName)
# for line in fr.readlines():
#     curLine = line.strip().split(' ')
#     fltLine = map(float, curLine)
#     dataMat.append(fltLine)
#
# for i in dataMat:
#     print(list(i))









