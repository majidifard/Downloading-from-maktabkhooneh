import os

main_paths = [
    'C:\\Users\\TSP5\\Downloads\\maktabkhooneh\\1\\',
    'C:\\Users\\TSP5\\Downloads\\maktabkhooneh\\2\\'
]

def hrefReader() :
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    f = open('hrefs.txt','r')
    m = f.readlines()
    f.close()
    hrefs = []
    for href in m :
        hrefs.append(href.strip())
    return hrefs

def numberFinder(hrefs,file) :
    i = 0
    while i < len(hrefs) :
        if file in hrefs[i] :
            s = i
            while s > 0 :
                if '----' in hrefs[s] :
                    return i-s
                s -= 1
        i += 1

def fileNameGetter(string) :
    sec = string.find(".mp4")
    i = len(string)-1
    while i > 0  :
        if string[i] == "\\" :
            fir = i+1
            break
        i -= 1
    return string[fir:sec]

def main(main_paths) :
    hrefs = hrefReader()
    for PATH in main_paths :
        files = os.listdir(PATH)
        for file in files :
            path = PATH + file
            fileName = fileNameGetter(path)
            number = numberFinder(hrefs,fileName)
            os.chdir(PATH)
            if number is not None :
                print(file)
                os.rename(str(file),str(number)+".mp4")



main(main_paths)
