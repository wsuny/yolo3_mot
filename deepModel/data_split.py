import os
import random
import shutil

def getData(dirPath,destDir):
    subDirs = os.listdir(dirPath)

    for dir in subDirs:
        tempDir = dirPath + '\\' + dir + '\\'
        if not os.path.exists(destDir + '\\' + dir + '\\'):
            os.mkdir(destDir + '\\' + dir + '\\')
        fs = os.listdir(tempDir)
        random.shuffle(fs)
        le = int(len(fs) * 0.8)  
        for f in fs[le:]:
            shutil.move(tempDir + f, destDir + '\\' + dir + '\\')

if __name__ == '__main__':
    parent_path = os.path.dirname(__file__)
    print (os.path.abspath(parent_path))
    train_path = os.path.join(parent_path,'data','Mars','train')
    val_path = os.path.join(parent_path,'data','Mars','validation') # 提前建好
    getData(train_path,val_path)
