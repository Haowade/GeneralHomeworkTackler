import numpy as np

def Process(MatrixA):
    ReturnData = []
    if(len(MatrixA.shape) != 2):
        return
    for i in range(MatrixA.shape[0]):
        Abs = MatrixA[i,0] ** 2 + MatrixA[i,1] ** 2
        Arg = np.arctan(MatrixA[i,1] / MatrixA[i,0])
        Data = np.array([Abs,Arg])
        ReturnData.append(Data)
    return ReturnData

InitialData = np.array([[1, 1], [2, 3], [1, 3]])

print(Process(InitialData))