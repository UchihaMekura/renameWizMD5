import os,sys
import json
import time

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
			if os.path.exists(folder_path+os.sep+folderName+'.json'):
				with open(folder_path+os.sep+folderName+'.json','r',encoding='utf-8') as f: #json保存中文
					result_dict = json.load(f)
			
				for each in result_dict:
					if os.path.exists(folder_path+os.sep+each+getLastExtention(result_dict[each])):
						os.rename(folder_path+os.sep+each+getLastExtention(result_dict[each]),folder_path+os.sep+result_dict[each])

				os.remove(folder_path+os.sep+folderName+'.json')
				


