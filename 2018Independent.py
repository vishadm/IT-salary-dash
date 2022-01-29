from matplotlib import scale
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import altair as alt


st.set_page_config(layout = 'wide', initial_sidebar_state = 'collapsed')

path = 'D:/DS/Streamlit/IT Salary Survey2018_Cleaned.csv'
df = pd.read_csv(path)
imageurl = ('https://keendomains.files.wordpress.com/2021/01/lof36xlnivy9jouwawen.gif')
image_s0, image1, image_s1 = st.columns((1,7,1))
image1.image(imageurl,use_column_width = True)
#st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
title_spacer0, title, title_spacer1 = st.columns((3.5,4,3))
title.title('IT Salary Survey Visuals')
subtitle_spacer0, subtitle, subtitle_spacer1 = st.columns((5.5,2,5))
subtitle.subheader('(EU Region)')

yearlist = ['2018','2019','2020']
year = st.sidebar.selectbox('Please Select the year',yearlist)
note1 = st.sidebar.expander('Please Note 👉')
with note1:
    st.markdown('This is not the original Dataset. This data was cleaned and prepared [seperately](https://github.com/vishadm/IT-salary-dash/blob/main/IT%20Salary18.ipynb)')

row0c0, row0c1 = st.columns(2)
row0c0.markdown(""" Hey there! Welcome to IT Salary Survey Visuals App. 
This app curates ard represents the IT Jobs Salary data for Europe region with clean and sleek visuals
, If you're on a mobile device, switch over to landscape for viewing ease.""")
row0c1.markdown(""" This app contains the visuals describing the IT Salary Survey Dataset imported from [Kaggle](https://www.kaggle.com/parulpandey/2020-it-salary-survey-for-eu-region) 
and various trends in the data with relevance to The Yearly Salary""")

df_spacer0, dataframe, df_spacer1 = st.columns((3.5,7,3))
dataframe.markdown("""#### First we have a quick look at the data we have with ourselves """)
st.dataframe(df)


row1_s0,row1,row0_s1 = st.columns((3.5,4,3))
row1.markdown("""### Now into the details of the dataset """)

row2_c0,row2_c1 = st.columns(2)
row2_c0.markdown("""#### <u>The percentage of Genders</u> """,unsafe_allow_html = True)
genpercent = pd.DataFrame({"Gender": ['Male','Female','Not Mentioned'], "value": [84,13,3]}) #765
figGender = alt.Chart(genpercent).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="Gender", type="nominal"), tooltip = ['Gender','value']
).properties(height = 500)
# row3_s0,row3,row3_s1 = st.columns((5,6,4))
row2_c0.altair_chart(figGender, use_container_width=True)
row2_c0.markdown("""The pie chart pictures the percentage of all the genders in the dataset. There were no mentions of other genders apart from Male and Female.
It is observed parsing through the dataset that the number of the Gender Male had a considerable lead over the Female Gender """)

#row4_s0,row4,row4_s1 = st.columns((3.5,4,3))
row2_c1.markdown("""#### <u>    Seniority Levels throughout the dataset</u>""",unsafe_allow_html = True)

#dfSenior = df.groupby('Seniority Level').sum() (IMPORTANT)

dfSenior = pd.DataFrame({"Level": ['Senior','Middle','Junior','Undefined'], "value": [497,206,40,22]})
#test1 = dfSenior.astype(str)
fig2 = alt.Chart(dfSenior).mark_bar().encode(
    alt.Y('value',
        scale=alt.Scale(domain=(0, 550))),x = 'Level',color = 'Level' ,tooltip = ['Level','value']
)
text = fig2.mark_text(
    align='left',
    baseline='middle',
    dx = -10 ,dy= -5
).encode(
    text='Level'
)

fig2upd = (fig2 + text).properties(height = 500,width = 800)
row2_c1.altair_chart(fig2upd, use_container_width=True)
row2_c1.markdown("""This bar graph shows the number of entries grouped by their seniority levels. A lot of Entries had undefined or Not mentioned
seniority levels but majority were found out to be Seniors in their Job designations wheras a handful of the total were juniors. """)

row7_c1, row7_c2 = st.columns(2)
row7_c1.markdown("""#### <u> The designations in the dataset</u> """, unsafe_allow_html = True)
# make positions graph row7_c1

row7_c2.markdown("""#### <u> The variation of Experience </u>""", unsafe_allow_html = True)
row7_c2.line_chart(df['Years of experience'],use_container_width  = True)
row7_c2.markdown(""" This schematic shows the variation of the Years of Experience in the dataset. 
It was recorded that a lot of people had very low experience in their respective jobs and only a small percentage of people had experience greater than 12 Years.
 The average years of experience was 8 Years while the highest was 38 Years""")

note = st.expander('Please Note 👉 ')
with note:
    st.markdown(""" All the displayed Salary and stock values are in Euros(€) """)

row8_s0, row8, row8_s1 = st.columns((4.5,5,4))
row8.markdown("""### <u> The variation of <b>Yearly Salary</b> </u> """, unsafe_allow_html = True) #bolding error
st.area_chart(df['Yearly Salary'], use_container_width=True)
#row9_s0, row9, row9_s1 = st.columns((3.5,8,1))
st.markdown("""The variation of the Yearly Salary (Without any Stocks and bonuses) is represented by this area chart. 
As you can see, the salary ranges from €10,300 to €200,000 with the average salary going upto €68,300 which is around €5,700 per month,
which can be explained because of the loss of momentum in the growth of [German economy.](https://www.cnbc.com/2019/01/15/germany-2018-gdp-data.html)""")


row10c1, row10c2 = st.columns(2)
comlang = pd.DataFrame({"Languages":['English','Deutsch','Russian','Not Mentioned','French','Polish','Deutsch/English'],"value":[581,134,29,15,2,2,1]})
row10c1.markdown("""#### Main language of communication in work""")
fig5 = alt.Chart(comlang).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="Languages", type="nominal"), tooltip = ['Languages','value']
).properties(height = 450)
row10c1.altair_chart(fig5, use_container_width = True)
row10c1.markdown("""Noted that a majority of the people working communicated in English in their Jobs followed by German as most 
of the data entries are from German cities.""")

comsize = pd.DataFrame({"Company Sizes":['100-1000','1000+','50-100','10-50','up to 10','Not Mentioned'],"value":[260,219,120,117,34,15]})
fig6 = alt.Chart(comsize).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="Company Sizes", type="nominal"), tooltip = ['Company Sizes','value']
).properties(height = 450)
row10c2.markdown("""#### Size of the companies the employees work in """)
row10c2.altair_chart(fig6, use_container_width = True)
row10c2.markdown(""" The pie chart represents that a large number of people worked in Small Organisations
wheras an almost equally large number of people worked for organisaition with 100-1000 employees. A staggering amount of people also worked in very big organisaions accordingly. """)

row11_s0,row11,row11_c1 = st.columns((4,6,3))
row11.markdown("""### The Type of Companies in the dataset """)
companytypes = pd.DataFrame({"Types":['Product','Startup','Agency','Not mentioned','Consulting','Outsource','E-Commerce','Automotive','Insurance','Others'],"value":[452,145,74,35,15,10,6,2,2,22]})
fig7 = alt.Chart(companytypes).mark_bar().encode(
    y = "Types",x = "value",color = "Types", tooltip = ['Types','value']
)
st.altair_chart(fig7,use_container_width= True)
st.markdown("""An astonishing amount of people worked in Product type companies. 
These are companies that produce products of their own and sell them to consumers through the market and provide services for these products.
This number is followed by startups as it was noticed that more than one hundered people were working in startups in the year 2018.
This might be caused by the boom of startups in the [year](https://www.cnbc.com/2018/12/04/state-of-european-tech-2018-record-year-for-start-ups.html) """)
# if year=='2018':
#     year2018()
