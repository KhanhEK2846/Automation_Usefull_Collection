import PyPDF2,os,pathlib
import img2pdf
from PIL import Image

dirPath = pathlib.Path(__file__).parent.absolute()
inPath = str(dirPath) + "\input\\"
outPath = str(dirPath) + "\output\\"
tempPath = str(dirPath) + "\\temp\\"

dirs =os.listdir(inPath)

merge = PyPDF2.PdfMerger()

def handler(func, path, exc_info):
    print("Inside handler")
    print(exc_info)

if __name__ == "__main__":
    #os.mkdir("temp")
    for file in dirs:
        image = Image.open(inPath+file)
        f,e = os.path.splitext(file)

        pdf_bytes = img2pdf.convert(image.filename)
        temp_file = open("./temp/"+f+".pdf","wb")
        temp_file.write(pdf_bytes)
        image.close()
        temp_file.close()
        merge.append(tempPath+f+".pdf")



    merge.write(outPath+"Merge.pdf")
    #shutil.rmtree(os.path.join(dirPath,"temp"), onerror=handler)
