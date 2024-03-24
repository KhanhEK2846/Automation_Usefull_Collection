import platform as pf
import multiprocessing as mp
import tensorflow as tf
import psutil

def get_system_info():
    os_name = pf.system()
    pf_name = pf.platform()
    rel_info = pf.release()
    return os_name,pf_name,rel_info 

def Python_Bit_Mode():
    if pf.architecture()[0] == '32bit':
        return "32-bit mode"
    if pf.architecture()[0] == '64bit':
        return "64-bit mode"
    return "Unknow"

def get_num_cpus():
    return mp.cpu_count()

def get_RAM_info():
    mem = psutil.virtual_memory()
    return mem.total, mem.available,mem.used,mem.free
     

if __name__ ==  "__main__":
    os_name,pf_name,rel_info = get_system_info()
    num_cpus = get_num_cpus()
    total_mem,avai_mem,used_mem,free_mem = get_RAM_info()
    print("OS Name:",os_name)
    print("Platform:",pf_name)
    print("Release Information:",rel_info)
    print("Number of CPUs used:",num_cpus)
    print(f'Total Memory: {total_mem} bytes')
    print(f'Available Memory: {avai_mem} bytes')
    print(f'Used Memory: {used_mem} bytes')
    print(f'Free Memory: {free_mem} bytes')
    print("GPU Available:",tf.config.list_physical_devices('GPU'))
    print("Python's running in",Python_Bit_Mode())