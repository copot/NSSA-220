import matplotlib.pyplot as plt
import numpy as np

def read_data(filename, data) :

    # Read in data from file line by line
    infile = open(filename, 'r')
    
    line = infile.readline()

    while line :
        line = line.strip()
        data.append(line.split(','))
        line = infile.readline()
    
    infile.close()

    # Convert continuous attributes to float and class labels to integers
    for i in range(0, len(data)) : 
        data[i][0] = float(data[i][0])
        data[i][1] = float(data[i][1])
        data[i][2] = float(data[i][2])

def read_data_better(filename, data) :

    # Read in data from file line by line
    infile = open(filename, 'r')
    
    line = infile.readline()

    while line :
        line = line.strip()
        data.append(line.split(','))
        line = infile.readline()
    
    infile.close()

    # Convert continuous attributes to float and class labels to integers
    for i in range(0, len(data)) : 
        data[i][0] = float(data[i][0])
        data[i][1] = float(data[i][1])
        data[i][2] = float(data[i][2])
        data[i][3] = float(data[i][3])
        data[i][4] = float(data[i][4])

filename1 = 'APM1_metrics.csv'
filename2 = 'APM2_metrics.csv'
filename3 = 'APM3_metrics.csv'
filename4 = 'APM4_metrics.csv'
filename5 = 'APM5_metrics.csv'
filename6 = 'APM6_metrics.csv'
filename7 = 'system_metrics.csv'

# make an empty data List
data = []
APM1 = []
APM2 = []
APM3 = []
APM4 = []
APM5 = []
APM6 = []
system_metrics = []


read_data(filename1, data)
for instance in data :
    APM1.append(instance)
    
APM1_arr = np.array(APM1)
data.clear()

read_data(filename2, data)
for instance in data :
    APM2.append(instance)

APM2_arr = np.array(APM2)
data.clear()

read_data(filename3, data)
for instance in data :
    APM3.append(instance)

APM3_arr = np.array(APM3)
data.clear()

read_data(filename4, data)
for instance in data :
    APM4.append(instance)

APM4_arr = np.array(APM4)
data.clear()

read_data(filename5, data)
for instance in data :
    APM5.append(instance)

APM5_arr = np.array(APM5)
data.clear()

read_data(filename6, data)
for instance in data :
    APM6.append(instance)

APM6_arr = np.array(APM6)
data.clear()

read_data_better(filename7, data)
for instance in data :
    system_metrics.append(instance)

SysMet_arr = np.array(system_metrics)
data.clear()


# CPU plot
plt.plot(APM1_arr[:,0], APM1_arr[:, 1], color='blue', label='APM1')
plt.plot(APM2_arr[:,0], APM2_arr[:, 1], color='black', label='APM2')
plt.plot(APM3_arr[:,0], APM3_arr[:, 1], color='red', label='APM3')
plt.plot(APM4_arr[:,0], APM4_arr[:, 1], color='green', label='APM4')
plt.plot(APM5_arr[:,0], APM5_arr[:, 1], color='yellow', label='APM5')
plt.plot(APM6_arr[:,0], APM6_arr[:, 1], color='cyan', label='APM6')

plt.xlim([0, 910])
plt.legend(loc='upper right')
plt.ylabel('Utilization in percentage')
plt.xlabel('Seconds')
plt.title('CPU Utilization over time')
plt.savefig('cpu.png')
plt.close()


# Memory plot
plt.plot(APM1_arr[:,0], APM1_arr[:, 2], color='blue', label='APM1')
plt.plot(APM2_arr[:,0], APM2_arr[:, 2], color='black', label='APM2')
plt.plot(APM3_arr[:,0], APM3_arr[:, 2], color='red', label='APM3')
plt.plot(APM4_arr[:,0], APM4_arr[:, 2], color='green', label='APM4')
plt.plot(APM5_arr[:,0], APM5_arr[:, 2], color='yellow', label='APM5')
plt.plot(APM6_arr[:,0], APM6_arr[:, 2], color='cyan', label='APM6')

plt.xlim([0, 910])
plt.legend(loc='upper right')
plt.ylabel('Utilization in percentage')
plt.xlabel('Seconds')
plt.title('Memory Utilization over time')
plt.savefig('memory.png')
plt.close()

# bandwidth plot
plt.plot(SysMet_arr[:, 0], SysMet_arr[:, 1], color='red', label='RX')
plt.plot(SysMet_arr[:, 0], SysMet_arr[:, 2], color='black', label='TX')

plt.xlim([0, 910])
plt.legend(loc='upper right')
plt.ylabel('Data rate (kb/sec)')
plt.xlabel('Seconds')
plt.title('Bandwidth Utilization over time')
plt.savefig('bandwidth.png')
plt.close()

# Disk Access rates plot
plt.plot(SysMet_arr[:, 0], SysMet_arr[:, 3], color='black', label='Access Rate')

plt.xlim([0, 910])
plt.legend(loc='upper right')
plt.ylabel('Disk Write (kb/sec)')
plt.xlabel('Seconds')
plt.title('Disk Access Rates Over time')
plt.savefig('disk_access.png')
plt.close()

# Disk Utilization plot
plt.plot(SysMet_arr[:, 0], SysMet_arr[:, 4], color='black', label='Capacity')

plt.xlim([0, 910])
plt.legend(loc='upper right')
plt.ylabel('Data Capacity (mb)')
plt.xlabel('Seconds')
plt.title('Disk Utilization over time')
plt.savefig('disk_util.png')
plt.close()


