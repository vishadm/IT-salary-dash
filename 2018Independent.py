import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import altair as alt


st.set_page_config(layout = 'wide', initial_sidebar_state = 'collapsed')

path = 'D:/DS/Streamlit/IT Salary Survey2018_Cleaned.csv'
df = pd.read_csv(path)

#st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
title_spacer0, title, title_spacer1 = st.columns((3.5,4,3))
title.title('IT Salary Survey Visuals')
subtitle_spacer0, subtitle, subtitle_spacer1 = st.columns((5.5,2,5))
subtitle.subheader('(EU Region)')

yearlist = ['2018','2019','2020']
year = st.sidebar.selectbox('Please Select the year',yearlist)

row0c0, row0c1 = st.columns(2)
row0c0.markdown(""" Hey there! Welcome to IT Salary Survey Visuals App. 
This app curates are represents the IT Jobs Salary data for Europe region with clean and sleek visuals
, If you're on a mobile device, switch over to landscape for viewing ease.""")
row0c1.markdown(""" This app contains the visuals describing the IT Salary Survey Dataset imported from [Kaggle](https://www.kaggle.com/parulpandey/2020-it-salary-survey-for-eu-region) 
and various trends in the data with relevance to The Yearly Salary""")

df_spacer0, dataframe, df_spacer1 = st.columns((3.5,7,3))
dataframe.markdown("""#### First we have a quick look at the data we have with ourselves """)
st.dataframe(df)


note = st.expander('Please Note 👉')
with note:
    st.markdown('This is not the original Dataset. This data was cleaned and prepared [seperately](https://github.com/vishadm/IT-salary-dash/blob/main/IT%20Salary18.ipynb)')

row1_s0,row1,row0_s1 = st.columns((3.5,4,3))
row1.markdown("""### Now into the details of the dataset """)

row2_s0,row2,row2_s1 = st.columns((6.7,4,7))
row2.markdown("""#### <u>The percentage of Genders</u> """,unsafe_allow_html = True)
genpercent = pd.DataFrame({"Gender": ['Male','Female','Not Mentioned'], "value": [84,13,3]}) #765
figGender = alt.Chart(genpercent).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="Gender", type="nominal"), tooltip = ['Gender','value']
).properties(height = 450)
row3_s0,row3,row3_s1 = st.columns((5,6,4))
row3.altair_chart(figGender, use_container_width=True)

row4_s0,row4,row4_s1 = st.columns((3.5,4,3))
row4.markdown("""#### <u>Seniority Levels throughout the dataset</u>""",unsafe_allow_html = True)
row5_s0,row5,row5_s1 = st.columns((5,6,4))

#dfSenior = df.groupby('Seniority Level').sum() (IMPORTANT)

dfSenior = pd.DataFrame({"Level": ['Senior','Middle','Junior','Undefined'], "value": [497,206,40,22]})
#test1 = dfSenior.astype(str)
row6_s0,row6,row6_s1 = st.columns((3.7,6,4))
fig2 = alt.Chart(dfSenior).mark_bar().encode(
    x = 'Level', y = 'value', tooltip = ['Level','value']
).properties(height = 500,width = 800)
row6.altair_chart(fig2, use_container_width=True)

row7_c1, row7_c2 = st.columns(2)
row7_c1.markdown("""#### <u> The designations in the dataset</u> """, unsafe_allow_html = True)
# make positions graph row7_c1

row7_c2.markdown("""##### The experience levels in the dataset vary people with no experience in the tech industry to people with upto 38 documented years of discovery  """)
row7_c2.line_chart(df['Years of experience'],use_container_width  = True)
row7_c2.markdown(""" This schematic shows the variation of the Years of Experience in the dataset """)

row8_s0, row8, row8_s1 = st.columns((2,8,1))
row8.markdown("""### <u> This visual shows the variation of the ** Yearly Salary ** throughout the dataset</u> """, unsafe_allow_html = True) #bolding error
st.area_chart(df['Yearly Salary'], use_container_width=True)
row9_s0, row9, row9_s1 = st.columns((3.5,8,1))
row9.markdown(""" #### As you can see, the salary ranges from €10300 to €200000 """)

note = st.expander('Please Note 👉 ')
with note:
    st.markdown(""" All the displayed Salary and stock values are in Euros(€) """)

row10c1, row10c2 = st.columns(2)
comlang = pd.DataFrame({"Languages":['English','Deutsch','Russian','Not Mentioned','French','Polish','Deutsch/English'],"value":[581,134,29,15,2,2,1]})
row10c1.markdown("""#### Main language of communication in work""")
fig5 = alt.Chart(comlang).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="Languages", type="nominal"), tooltip = ['Languages','value']
).properties(height = 450)
row10c1.altair_chart(fig5, use_container_width = True)
comsize = pd.DataFrame({"Company Sizes":['100-1000','1000+','50-100','10-50','up to 10','Not Mentioned'],"value":[260,219,120,117,34,15]})
fig6 = alt.Chart(comsize).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="Company Sizes", type="nominal"), tooltip = ['Company Sizes','value']
).properties(height = 450)
row10c2.markdown("""#### Size of the companies the employees work in """)
row10c2.altair_chart(fig6, use_container_width = True)

row11_s0,row11,row11_c1 = st.columns((3.5,6,3))
row11.markdown("""### Finally, the company types in the dataset """)
companytypes = pd.DataFrame({"Types":['Product','Startup','Agency','Not mentioned','Consulting','Outsource','E-Commerce','Automotive','Insurance','Others'],"value":[452,145,74,35,15,10,6,2,2,22]})
fig7 = alt.Chart(companytypes).mark_bar().encode(
    y = "Types",x = "value",color = "Types", tooltip = ['Types','value']
)
st.altair_chart(fig7,use_container_width= True)
# if year=='2018':
#     year2018()
