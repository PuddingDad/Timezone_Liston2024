import streamlit as st  
from datetime import datetime  
import pytz  
import requests  
import pycountry
import pydeck as pdk
import pandas as pd


from constant import * 

### Streamlit Page Config ###
# Configuring the Streamlit page with title, icon, layout, and menu items
st.set_page_config(
    page_title='Time Zone Alterer', 
    page_icon='🌎',
    layout='wide',
    menu_items={
        'About': 
        """
        This is the first Data app project for 2024_Liston.
        This app include different code snippets from different students who received 
        excellent for this assignment.
        """
    }  
)

### Heading ### 
st.title('Time Zone Alterer 😎')

st.divider()

st.sidebar.header("Select Location")

continent_list = list(timezone_dict.keys())
continent_selected = st.sidebar.radio("Select a continent", continent_list)

countries = list(timezone_dict[continent_selected].keys())
country_selected = st.sidebar.selectbox("Select a country", countries)

### Time and timeZone converter ###
timezone = pytz.timezone(timezone_dict[continent_selected][country_selected]['timezone'])
currentDatetime = datetime.now()
currentDatetime_converted = datetime.now(timezone)


### Main Content ###
col1, col2 = st.columns(2)

### Displaying the results in the Streamlit app ###
with col1:
    st.markdown("<h3 style='color:orange;'>Local Time Zone</h3>", unsafe_allow_html=True)
    st.write(currentDatetime.strftime("%Y-%m-%d %H:%M:%S"))

with col2:
    st.markdown("<h3 style='color:green;'>Selected Time Zone</h3>", unsafe_allow_html=True)
    st.write(currentDatetime_converted.strftime("%Y-%m-%d %H:%M:%S"))



st.markdown("---")

### Main 2: Country Information, By Maddison Ewart ###

st.header("Country Information")
st.caption("By Maddison Ewart")

col3, col4 = st.columns([2, 1])

with col3:
    st.write(f"**Capital of {country_selected}:** {country_info[country_selected]['capital']}")
    st.write(f"**About {country_selected}:** {country_info[country_selected]['description']}")

with col4:
    st.image(country_info[country_selected]['image'], caption=country_info[country_selected]['caption'])

st.markdown("---")
### Main 3: Country Geo, By Yohan Vattamkandathil Basil ###

st.header("Country Geo")
st.caption("By Yohan Vattamkandathil Basil")

coordinates = timezone_dict[continent_selected][country_selected]

if coordinates:
    
    #Define a layer to display on the map
    layer = pdk.Layer(
        'ScatterplotLayer',
        data=pd.DataFrame({'lat': [coordinates["lat"]], 'lon': [coordinates["lon"]]}),  #Data to be plotted on the map
        get_position='[lon, lat]',
        get_color='[200, 30, 0, 160]',  #Color of the point marking the location
        get_radius=50000,  #Size of the point marking the location
    )

    # Set the viewport location
    view_state = pdk.ViewState(
        latitude=coordinates["lat"],
        longitude=coordinates["lon"],
        zoom=4.5,  #Zoom level of the map
        pitch=0,  #Pitch angle of the map
    )

        ### Render the map in Streamlit ###
    r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": country_selected})
    st.pydeck_chart(r)  # Display the map in Streamlit

### Fetch Today in History ###

url = tih_wiki + "/" + str(currentDatetime.month) + "/" + str(currentDatetime.day)
r = requests.get(url)
event_list = r.json()['selected']

### Today in History Section ###
st.markdown("---")
st.header("Today in History")

with st.expander("View historical events"):
    # Looping through the list of events and displaying each one
    for i in event_list:
        st.markdown(f"**{i['year']}**: {i['text']}")
        st.markdown("---")

### Sidebar: Event by year, By Vince Sheffield ###

st.sidebar.header("Historical Events by Year")
st.sidebar.subheader("By Vince Sheffield")

unique_years = sorted(set(int(event["year"]) for event in event_list))

selected_year = st.sidebar.select_slider(
    "Select a year:", options=unique_years, value=unique_years[0]
)

selected_events = [event for event in event_list if int(event["year"]) == selected_year]

if selected_events:
    st.sidebar.write(f"Events in {selected_year}:")
    for event in selected_events:
        st.sidebar.markdown(f"**{event['year']}**: {event['text']}")
else:
    st.sidebar.write(f"No events found for {selected_year}.")
