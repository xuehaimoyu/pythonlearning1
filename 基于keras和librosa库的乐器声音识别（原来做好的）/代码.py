import librosa
import numpy as np
import os
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
from keras.utils import np_utils
from keras import models
from keras.layers import Dense, Dropout
from keras.models import Sequential   # 网络模型
from keras.layers import Dense,Dropout
classes = 'piano guitar violin changdi shoufengqin'.split()
data_set = []
label_set = [] 
label2id = {class1:i for i,class1 in enumerate(classes)}
id2label = {i:class1 for i,class1 in enumerate(classes)}
print(label2id)
for c in classes:
    print(c)
    for filename in os.listdir(f'D:/张斯然文件/musicdate/date/classes/{c}/'):
        songname = f'D:/张斯然文件/musicdate/date/classes/{c}/{filename}'
        y, sr = librosa.load(songname, mono=True, duration=30)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        rmse = librosa.feature.rms(y=y)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
 
        to_append = f'{np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'     
        for e in mfcc:
            to_append += f' {np.mean(e)}' 
        data_set.append([float(i) for i in to_append.split(" ")])
        label_set.append(label2id[c])
scaler = StandardScaler()
X = scaler.fit_transform(np.array(data_set, dtype = float))
y = np_utils.to_categorical(np.array(label_set))
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
print(X_train.shape[1])
def Model_creat():
    model= Sequential()
    model.add(Dense(units=120,activation='relu',input_shape=(X_train.shape[1],)))#构建两个层
    model.add(Dense(units=60,activation='relu'))
    model.add(Dense(units=30, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(units=5,activation='softmax'))#输出节点
    return model
model=Model_creat()
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy','categorical_accuracy'])
model.fit(X_train, y_train, epochs=50, batch_size=64)

#model.save(f'D:/张斯然文件/musicdate/date/modelshow.h5')
import librosa
import numpy as np
import os
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
from keras.utils import np_utils
model_path = f'D:/张斯然文件/musicdate/date/model13.h5'
# 载入模型
model = load_model(model_path)
data_set1=[]
for filename in os.listdir(f'D:/张斯然文件/musicdate/date/classes/test/'):
    songname = f'D:/张斯然文件/musicdate/date/classes/test/{filename}'
    print(songname)
    y, sr = librosa.load(songname, mono=True, duration=30)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    rmse = librosa.feature.rms(y=y)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
 
    to_append = f'{np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'    
 
    for e in mfcc:
        to_append += f' {np.mean(e)}'
 
    data_set1.append([float(i) for i in to_append.split(" ")])
        
scaler = StandardScaler()    
X1= scaler.fit_transform(np.array(data_set1, dtype = float))
result=model.predict(X1)
array=np.argmax(result,axis=1)
print(result)
print(array)
classes=['钢琴','吉他','小提琴','长笛','手风琴']
for j in range(0,len(array)):
    print("第{}个为".format(j+1),classes[array[j]])
