import os,sys
import json
import time
import hashlib


def getFileMd5(file_path):
	m = hashlib.md5() 

	with open(file_path,'rb') as f:
		while 1:
			data = f.read(4096)
			if not data:
				break
			m.update(data) 

	return m.hexdigest() 

def getFullExtention(file_name): #'.123.123123'
	if file_name.find('.') != -1:
		extention = file_name[file_name.find('.'):]
	else:
		extention = ''
	return extention

def getLastExtention(file_name): #'.123123'
	if file_name.find('.') != -1:
		extention = '.'+file_name.split('.')[-1]
	else:
		extention = ''
	return extention

if __name__ == '__main__':
	
	folder_path_list = sys.argv[1:]

	for folder_path in folder_path_list:
		if os.path.isdir(folder_path):
			folderName = folder_path.split(os.sep)[-1]
			if not os.path.exists(folder_path+os.sep+folderName+'.json'):
				file_list = os.listdir(folder_path)

				result_dict = {}
				for each in file_list:
					md5 = getFileMd5(folder_path+os.sep+each)

					key = md5
					i = 1
					while key in result_dict:
						key = md5+'_'+str(i)
						i = i+1
					#	print(key)

					#if key in result_dict:
					#	print("ERROR")

					result_dict[key] = each

					newName = key+getLastExtention(each)

					os.rename(folder_path+os.sep+each,folder_path+os.sep+newName)

				with open(folder_path+os.sep+folderName+'.json','w',encoding='utf-8') as f: #json保存中文
					json.dump(result_dict,f,ensure_ascii=False,indent = 4)
