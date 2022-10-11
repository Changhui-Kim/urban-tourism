import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from datetime import datetime, timedelta

features_mean = np.load('./features_mean.npy')
top50_dongs = pd.read_csv('./top50_dongs.csv')
top50_dongs.columns = [['id', 'name']]

date_list = [f'{y:02d}-{m:02d}' for y in range(2014, 2023) for m in range(1, 13)][10:-5]
datetime_list = [datetime.strptime(date_list[i], '%Y-%m') for i in range(len(date_list))]

def draw_graph(features, dong, fidx, start=0, end=93):
    fig, ax = plt.subplots()
    dong_name = dong['name']
    dong_id = int(dong['id'])
    ax.plot(datetime_list,features[dong_id, range(start, end), fidx])
    plt.rc('font', family='NanumGothic')
    
    plt.title(f'dong_{dong_id}_{dong_name}')
    plt.axvline(x=datetime_list[62], color='red')
    myFmt = DateFormatter("%Y-%d")
    ax.xaxis.set_major_formatter(myFmt)

    fig.autofmt_xdate()
    st.pyplot(fig)


for i in range(50):
    draw_graph(features_mean, top50_dongs.iloc[i], 1)
