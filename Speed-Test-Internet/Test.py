from speedtest import Speedtest
sp = Speedtest()

try:
    sp.get_best_server()
except:
    sp.get_servers()

sp.upload()
sp.download()
res = sp.results.dict()
def con_MB(n):
    return f"{round(n/(10**6), 2)} MB/s"
print("Upload: ",con_MB(res["upload"]))
print("Download: ",con_MB(res["download"]))
print("Ping: ", res["ping"], "s")
