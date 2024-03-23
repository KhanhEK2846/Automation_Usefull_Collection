import PyPDF2,os,pathlib

dirPath = pathlib.Path(__file__).parent.absolute()
inPath = str(dirPath) + "\input\\"
outPath = str(dirPath) + "\output\\"

dirs =os.listdir(inPath)

merge = PyPDF2.PdfMerger()

def MergePDF():
    for file in dirs:
        if file.endswith(".pdf"):
            merge.append(inPath+file)
            
    merge.write(outPath+"Merge.pdf")


MergePDF()