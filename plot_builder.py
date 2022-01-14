import matplotlib.pyplot as plt

if __name__ == "__main__":
    files = ["cat_mmap_txt","clang_mmap.txt","cp_mmap.txt","df_mmap.txt",\
        "firefox_mmap.txt","g++_mmap.txt","gcc_mmap.txt","ls_mmap.txt",\
            "more_mmap.txt","ps_mmap.txt","rm_mmap.txt","writer_mmap.txt","python_mmap.txt"]
    for file_name in files:

        with open(file_name) as file:
            text = file.readline()