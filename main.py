import os
import json
import matplotlib.pyplot as plt

# Your code for data processing and calculations

# Example code to save a dictionary as a pickle file
data = {"key1": "value1", "key2": "value2", "key3": "value3"}
pickle_file_path = os.path.join(os.getcwd(), "data.pickle")
with open(pickle_file_path, "wb") as pickle_file:
    pickle.dump(data, pickle_file)
print("Dictionary saved as pickle file.")

# Example code to generate a line graph
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph')
plt.show()

# Example code to generate a bar graph
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 15, 7, 12, 9]
plt.bar(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Graph')
plt.show()

# Example code to generate a pie chart
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [10, 15, 7, 12, 9]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()


json_files_dir = os.path.join(os.getcwd(), 'json')
json_files = [f for f in os.listdir(json_files_dir) if f.endswith('.json')]


# Example json file structure
'''[
    {
        "fw": 5020,
        "mver": "2.2.1",
        "lts": 56292,
        "endtime": 1725411187,
        "dst_name": "betnacional.com",
        "ttr": 33.113119,
        "dst_addr": "104.18.18.131",
        "src_addr": "190.124.192.157",
        "proto": "UDP",
        "af": 4,
        "size": 48,
        "paris_id": 1,
        "result": [
            {
                "hop": 1,
                "result": [
                    {
                        "from": "190.124.192.129",
                        "ttl": 64,
                        "size": 76,
                        "rtt": 0.518
                    },
                    {
                        "from": "190.124.192.129",
                        "ttl": 64,
                        "size": 76,
                        "rtt": 0.452
                    },
                    {
                        "from": "190.124.192.129",
                        "ttl": 64,
                        "size": 76,
                        "rtt": 0.527
                    }
                ]
            },
            {
                "hop": 1,
                "result": [
                    {
                        "from": "190.124.192.129",
                        "ttl": 64,
                        "size": 76,
                        "rtt": 0.518
                    },
                    {
                        "from": "190.124.192.129",
                        "ttl": 64,
                        "size": 76,
                        "rtt": 0.452
                    },
                    {
                        "from": "190.124.192.129",
                        "ttl": 64,
                        "size": 76,
                        "rtt": 0.527
                    }
                ]
            },...
        ],
        "destination_ip_responded": true,
        "msm_id": 78674595,
        "prb_id": 1001398,
        "timestamp": 1725411179,
        "msm_name": "Traceroute",
        "from": "190.124.192.157",
        "type": "traceroute",
        "group_id": 78674595,
        "stored_timestamp": 1725411309
    },...
'''


#PROBE ICMP

# Variables
# Destination, Id probe, timestamp, num-hops, latencia

#Graph1 - De linhas - 3 Destinos 3 Graphs
#Latencia(latencia) / Tempo(timestamp)
## Por Probe - 30 linhas
## Por Pais - 9 linhas (Media de 3 probes)
## Por Continente - 3 linhas (Media de 3 paises/media de 3 probes)

#Graph2 - De linhas - 3 Destinos 3 Graphs
#Hops(num_hops) / Tempo(timestamp)
## Por Probe - 30 linhas
## Por Pais - 9 linhas (Media de 3 probes)
## Por Continente - 3 linhas (Media de 3 paises/media de 3 probes)


#Graph3 - De pontos - 3 Destinos 3 Graphs
#Hops(num_hops) / Latencia(latencia)


if __name__ == '__main__':
    for file in json_files:
        print(f'Processing {file}')
        with open(os.path.join(json_files_dir, file)) as json_file:
            data = json.load(json_file)
            # Access the attributes of the JSON data here
            # For example:
            for key, value in data[0].items():
                print(f"{key}:")
            # Do something with the attributes