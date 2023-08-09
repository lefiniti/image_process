def updateFile(file,old_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        i=0
        for line in f:
            if old_str in line:
                i=i+1
                print(line)
                new_str="2058_"+str(i).zfill(6)+".wav"+'\r'
                print(new_str)
                line = line.replace(line,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

updateFile(r"E:\study\L36\2058_yicangwu\transcriptions.txt", ".wav")#将"D:\zdz\"路径的myfile.txt文件把所有的zdz改为daziran