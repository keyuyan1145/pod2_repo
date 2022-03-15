from stations_challenge import *

# from stations_challenge import SubwayStation

station_Macy_central = BusStation(station_name="Macy Station", location="14th street and Park Avenue", routes="Downtown, Chicago")
station_Macy_central.show_info()
#our_bus.close_station()
#our_bus.show_info()

station_grand_central = SubwayStation(station_name="14th street", location="14th street and 7th avenue", lines=["Downtown","Near North"])
station_grand_central.show_info()
#our_bus.close_station()
#our_bus.show_info()

station_union_square = BusStation(station_name="Carson Pirie Scott Station", location="24th street and Madison Avenue", routes=["Uptown", "Chicago"])
station_union_square.show_info()
# our_bus.close_station()
# our_bus.show_info()