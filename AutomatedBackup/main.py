import os, pathlib,shutil,datetime,time,schedule

dirPath = pathlib.Path(__file__).parent.absolute()
backupPath = str(dirPath)+"/backup"
scrPath = str(input("Enter path src: "))
timeBackup = str(input("Enter time to backup (hh:mm): "))
def copy_folder_to_directory(src:"str",dst:"str"):
    today = datetime.date.today()
    dst_dir = os.path.join(dst,str(today))
    
    try:
        shutil.copytree(src,dst_dir)
        print(f"Folder copied to {dst_dir}")
    except FileExistsError:
        print(f"Folder already exist in {dst}")

schedule.every().day.at(f"{timeBackup}").do(lambda: copy_folder_to_directory(scrPath.replace('\\','/'),backupPath.replace('\\','/')))

while True:
    schedule.run_pending()
    time.sleep(60)
