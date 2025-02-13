import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split

def ModelMaker(file):
    data= pd.read_csv(file+'.csv')
    if 'volume' in data.columns:
        data= data.drop(columns = ['id','volume','high','low'],axis=1)
    elif 'index' in data.columns:
        data= data.drop(columns = ['id','index','high','low'],axis=1)   
    data["time"] = pd.to_datetime(data.time).dt.strftime('%H%M')
    y = data['close']
    X = data.drop(columns = ['close'])
    x_train,x_test,y_train,y_test = train_test_split(X,y,test_size = 0.25,random_state=355)
    regression = LinearRegression()
    regression.fit(x_train,y_train)
    filename = file+'LinearRegression.pickle'
    pickle.dump(regression, open(filename, 'wb'))
    print(regression.score(x_train,y_train))

## File format for above fn should be 'file.csv' where file is Company Name

## TO get prediction: code below:

import pickle
loaded_model = pickle.load(open(file+'LinearRegression.pickle', 'rb'))
a=loaded_model.predict([[20150703,916,985.00]])
print(a)

## Insert the following in the predict fn
## date : yyyymmdd
## open/or prevois close
## it will then print the close value of stock

## THE BELOW FUNCTION IS FOR TOP 10 COMPANIES
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split

def ModelMaker2(file):
    data= pd.read_csv(file+'.csv')
    data['timestamp'] = pd.to_datetime(data['timestamp'],dayfirst=True)
    data['date'] = data['timestamp'].dt.strftime('%Y%m%d')
    data['time'] = data['timestamp'].dt.strftime('%H%M')
    data['date']=data['date'].astype(int)
    data= data.drop(columns = ['high','low','volume','timestamp'],axis=1)
    data = data[['date','time','open','close']]
    #data["time"]  = pd.to_datetime(data.time).dt.strftime('%H%M')
    y = data['close']
    X = data.drop(columns = ['close'])
    x_train,x_test,y_train,y_test = train_test_split(X,y,test_size = 0.25,random_state=355)
    regression = LinearRegression()
    regression.fit(x_train,y_train)
    filename = file+'LinearRegression.pickle'
    pickle.dump(regression, open(filename, 'wb'))
    print(regression.score(x_train,y_train))

## TO get prediction: code below:

import pickle
loaded_model = pickle.load(open(file+'LinearRegression.pickle', 'rb'))
a=loaded_model.predict([[20150703,916,985.00]])
print(a)

## Insert the following in the predict fn
## date : yyyymmdd
## open/or prevois close
## it will then print the close value of stock

##Return predictions as dataframe
import pickle
import pandas as pd
def TCSpredictor(from_date,to_date):#enter date as yyyymmdd
    file = input("Enter company Logo:")
    loaded_model = pickle.load(open(file+'LinearRegression.pickle', 'rb'))
    time_list=[916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246,1247,1248,1249,1250,1251,1252,1253,1254,1255,1256,1257,1258,1259,1300,1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311,1312,1313,1314,1315,1316,1317,1318,1319,1320,1321,1322,1323,1324,1325,1326,1327,1328,1329,1330,1331,1332,1333,1334,1335,1336,1337,1338,1339,1340,1341,1342,1343,1344,1345,1346,1347,1348,1349,1350,1351,1352,1353,1354,1355,1356,1357,1358,1359,1400,1401,1402,1403,1404,1405,1406,1407,1408,1409,1410,1411,1412,1413,1414,1415,1416,1417,1418,1419,1420,1421,1422,1423,1424,1425,1426,1427,1428,1429,1430,1431,1432,1433,1434,1435,1436,1437,1438,1439,1440,1441,1442,1443,1444,1445,1446,1447,1448,1449,1450,1451,1452,1453,1454,1455,1456,1457,1458,1459,1500,1501,1502,1503,1504,1505,1506,1507,1508,1509,1510,1511,1512,1513,1514,1515,1516,1517,1518,1519,1520,1521,1522,1523,1524,1525,1526,1527,1528,1529,1530,1531,1532,1533,1534,1535,1536,1537,1538,1539,1540,1541,1542,1543,1544,1545,1546,1547,1548,1549,1550,1551,1552,1553,1554,1555,1556,1557,1558,1559,1600]
    last_close = int(input("Enter previous day close value:"))
    cols = ['date','time','close']
    predictions = pd.DataFrame(columns = cols)
    for date in range(from_date,to_date+1):
        for time in time_list:
            last_close=loaded_model.predict([[date ,time,last_close]])
            predictions.loc[len(predictions)] = [date,time,last_close]
    return predictions