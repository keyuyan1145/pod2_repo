from stations_challenge import *

print()

ave11_w36st = BusStation('11th Ave', '11 Av & W 36 ST', ['2', '5', '7', 'A'])

platform_9_34 = SubwayStation(
    'Platform 9 3/4', '175th Street and Fort Washington Avenue',  ['2', '3', '4', 'Hogwarts'])

subway_175st = SubwayStation(
    'Whitehall St', 'South Street and Whitehall Street',  ['1', 'N', 'R', 'W'])


ave11_w36st.show_info()
platform_9_34.show_info()
subway_175st.show_info()
