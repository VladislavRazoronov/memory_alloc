import sys
import matplotlib.pyplot as plt
import pandas as pd
import re

if __name__ == "__main__":
    files = ["cat_mmap.txt","clang_mmap.txt","cp_mmap.txt","df_mmap.txt",\
        "firefox_mmap.txt","g++_mmap.txt","gcc_mmap.txt","ls_mmap.txt",\
            "more_mmap.txt","ps_mmap.txt","rm_mmap.txt","writer_mmap.txt","python_mmap.txt"]
    for filename in files:
        data = {"Memory":[],"Time":[]}
        begin_time = 0
        with open(filename) as file:
            for call in file:
                time_status = 0
                time = re.split(':| |\.',call)[:4]
                for i in range(4):
                    time[i] = int(time[i])
                if begin_time == 0:
                    begin_time = time
                else:
                    time_status = time[3]-begin_time[3] + (10**6)*(time[2]-begin_time[2]-60*(time[1]-begin_time[1]))
                args = call.split(',')
                if "mmap" not in args[0]:
                    continue
                mem_size = int(args[1])
                data["Memory"].append(mem_size)
                data["Time"].append(time_status)
                prot = args[2].split('|')
                flags = args[3].split('|')
        dataframe = pd.DataFrame(data)
        plt.plot(dataframe["Time"],dataframe["Memory"])
        plt.title("Memory call size for "+filename.split(".")[0])
        plt.xscale("log")
        plt.yscale("log")
        plt.xlabel("Call time since start")
        plt.ylabel("Used memory")
        plt.savefig("graphs/"+filename.split(".")[0]+".png")
        plt.clf()
