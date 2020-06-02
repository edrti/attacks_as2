import urllib.request
import binascii


def download_save_traces(server_url, number_of_power_traces, filename):
    traces = download_traces(server_url, number_of_power_traces)
    with open(filename, 'w') as file:
        for i in range(len(traces)):
            if i != len(traces) - 1:
                file.write(traces[i] + '\n')
            else:
                file.write(traces[i])


def download_traces(server_url, number_of_power_trace):
    traces = []
    for i in range(number_of_power_trace):
        trace = urllib.request.urlopen(server_url).read()
        traces.append(str(trace)[2:-1])
    return traces


def load_file(filename):
    file_lines = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            file_lines.append(line)
    return file_lines


def parse_time_stamps(file_lines):
    list_of_traces = []
    for line in file_lines:
        idx1 = line.rfind(']')
        idx2 = line.find('[')
        arr = []
        for st in line[idx2 + 1:idx1].split(','):
            arr.append(float(st))
        list_of_traces.append(arr)

    matrix = []
    for i in range(len(list_of_traces)):
        matrix.append(list_of_traces[i])
    return matrix


def parse_plaintexts(file_lines):
    plaintexts = []
    for line in file_lines:
        idx1 = line.find(':')
        idx2 = line.find(',')
        s = bytearray.fromhex(line[idx1 + 2:idx2 - 1])
        # TODO: check correctness
        plaintexts.append(s)
    return plaintexts
