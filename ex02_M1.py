from parse import *
from calc import *

user = "yossi"
number_of_power_traces = 10
filename = "a.txt"
difficulty = "1"

server_url = "http://aoi.ise.bgu.ac.il/encrypt?user={0}&difficulty={1}".format(user,difficulty)
print(server_url)
download_save_traces(server_url, number_of_power_traces, filename)
file_lines = load_file(filename)
traces = parse_time_stamps(file_lines)
print(traces)

means = []
variances = []
for i in range(len(traces)):
    mean = mean_calculation(traces[i])
    means.append(mean)
    variances.append(variance_calculation(traces[i], mean))

print("Mean\tVariance") # Print once at the start of your program and then
for i in range(len(means)):
    print("{0:.2f}\t{1:.2f}".format(means[i], variances[i]))
