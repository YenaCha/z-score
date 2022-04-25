import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics as st

df = pd.read_csv('C:/Users/yena0/Downloads/Python/project 111/medium_data.csv')
df1 = pd.read_csv('C:/Users/yena0/Downloads/Python/project 111/sample_1.csv')
df2 = pd.read_csv('C:/Users/yena0/Downloads/Python/project 111/sample_2.csv')
df3 = pd.read_csv('C:/Users/yena0/Downloads/Python/project 111/sample_3.csv')
time = df['reading_time'].tolist()
time1 = df1['reading_time'].tolist()
time2 = df2['reading_time'].tolist()
time3 = df3['reading_time'].tolist()
mean1 = st.mean(time1)
mean2 = st.mean(time2)
mean3 = st.mean(time3)

finallist = []
def sampling():
    data = []
    for i in range (0,100):
        rp = random.randint(0,len(time)-1)
        data.append(time[rp])
    finallist.append(st.mean(data))

for i in range (0,1000):
    sampling()

mean = st.mean(finallist)
std = st.stdev(finallist)

fe = mean+std
se = mean+std*2
te = mean+std*3

graphic = ff.create_distplot([finallist],['Reading time'],show_hist=False)
graphic.add_trace(go.Scatter(x=[fe,fe],y=[0,0.17],mode='lines',name='First standard deviation'))
graphic.add_trace(go.Scatter(x=[se,se],y=[0,0.17],mode='lines',name='Second standard deviation'))
graphic.add_trace(go.Scatter(x=[te,te],y=[0,0.17],mode='lines',name='Third standard deviation'))
graphic.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.17],mode='lines',name='Sample1'))
graphic.add_trace(go.Scatter(x=[mean2,mean2],y=[0,0.17],mode='lines',name='Sample2'))
graphic.add_trace(go.Scatter(x=[mean3,mean3],y=[0,0.17],mode='lines',name='Sample3'))
graphic.show()