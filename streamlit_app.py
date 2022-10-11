import streamlit as st
import mpld3
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from datetime import datetime, timedelta
import plotly.express as px

features_mean = np.load('features_mean.npy')
top50_dongs = pd.read_csv('top50_dongs.csv')
top50_dongs.columns = [['id', 'name']]

date_list = [f'{y:02d}-{m:02d}' for y in range(2014, 2023) for m in range(1, 13)][10:-5]
datetime_list = [datetime.strptime(date_list[i], '%Y-%m') for i in range(len(date_list))]


features_1 = features_mean[:,:,1]
dong_ids = [dong_id[0] for dong_id in top50_dongs['id'].values]
features_flat = np.concatenate([features_1[dong_id] for dong_id in dong_ids])
dong_id_list = [dong_id for dong_id in dong_ids for i in range(features_1.shape[1])]
dong_name_list = [dong_name[0] for dong_name in top50_dongs['name'].values for i in range(features_1.shape[1])]
ym_list = date_list * 50

dong_list = [dong_name[0] for dong_name in top50_dongs['name'].values]

dict = {'id':dong_id_list, 'name':dong_name_list, 'date':ym_list, 'num_property':features_flat}
df = pd.DataFrame(dict)

dong = st.sidebar.selectbox("Select a dong:", dong_list)
st.header("Number of Airbnbs over time")
fig = px.line(df[df['name']==dong], x='date', y='num_property', title=dong)
st.plotly_chart(fig)
