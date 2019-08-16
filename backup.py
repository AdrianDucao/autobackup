import os
import zipfile
import shutil

def	doprocess(sourceFolder, targetZip):
	zipf = zipfile.ZipFile(targetZip, "w")
	for subdir, dirs, files in os.walk(sourceFolder):
		for file in files:
			print (os.path.join(subdir, file))
			zipf.write(os.path.join(subdir, file))
	
	print ("Created ", targetZip)
		
def	docopy(sourceFolder, targetFolder):
	for subdir, dirs, files in os.walk(sourceFolder):
		for file in files:
			print (os.path.join(subdir, file))
			shutil.copy2(os.path.join(subdir, file), targetFolder)
	
if __name__ =='__main__':
	print ('Starting execution')
	
	sourceFolder = 'D:\\Xampp\\htdocs\\repository'
	targetZip = 'F:\\01-Arhive\\01-backup\\2019\\dev-backup\\dev-backup.zip'
	doprocess(sourceFolder, targetZip)	
	sourceFolder = 'F:\\01-Arhive\\01-backup\\2019\\dev-backup'
	targetFolder = 'F:\\01-Arhive\\02-documents\\2019'
	docopy(sourceFolder, targetFolder)

	print ('Ending execution')