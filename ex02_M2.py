from parse import *
from calc import *

filename = 'a.txt'
user = "yossi"
difficulty = "1"
number_of_power_traces = 10
server_url = "http://aoi.ise.bgu.ac.il/encrypt?user={0}&difficulty={1}".format(user,difficulty)

download_save_traces(server_url, number_of_power_traces, filename)
file_lines = load_file(filename)
traces = parse_time_stamps(file_lines)
plaintexts = parse_plaintexts(file_lines)
