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
        flag_dict = dict()
        protection = dict()
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
                for it in prot:
                    if it not in protection.keys():
                        protection[it] = [mem_size,1]
                    else:
                        protection[it][0] += mem_size
                        protection[it][1] += 1
                for it in flags:
                    if it not in flag_dict.keys():
                        flag_dict[it] = [mem_size,1]
                    else:
                        flag_dict[it][0] += mem_size
                        flag_dict[it][1] += 1
        dataframe = pd.DataFrame(data)
        plt.scatter(dataframe["Time"],dataframe["Memory"])
        plt.plot(dataframe["Time"],dataframe["Memory"])
        plt.title("Memory call size for "+filename.split(".")[0])
        plt.xscale("log")
        plt.yscale("log")
        plt.xlabel("Call time since start us")
        plt.ylabel("Used memory bit")
        plt.savefig("graphs/"+filename.split(".")[0]+".png")
        plt.clf()
        label,values = [],[]
        for lab, val in protection.items():
            label.append(lab)
            values.append(val)
        count,size = [],[]
        for value in values:
            count.append(value[1])
            size.append(value[0])
        plt.bar(label,size)
        plt.savefig("graphs/protection/"+filename.split(".")[0]+"prot_size.png")
        plt.clf()
        plt.bar(label,count)
        plt.savefig("graphs/protection/"+filename.split(".")[0]+"prot_count.png")
        plt.clf()
        label,values = [],[]
        for lab, val in flag_dict.items():
            label.append(lab)
            values.append(val)
        count,size = [],[]
        for value in values:
            count.append(value[1])
            size.append(value[0])
        plt.bar(label,size)
        plt.savefig("graphs/flags/"+filename.split(".")[0]+"flag_by_size.png")
        plt.clf()
        plt.bar(label,count)
        plt.savefig("graphs/flags/"+filename.split(".")[0]+"flag_by_count.png")
        plt.clf()
        print(protection)
        print(flag_dict)