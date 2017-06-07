#! /usr/bin/python
import xml.dom.minidom  
import os  
import string  
from subprocess import call  

#Downloads certain branchs
def isSuitableBranch(pathName, branchNames):
	for branch in branchNames:
		if pathName.startswith(branch):
			return True
	return False;
	

#Downloads All Android SourceCode
def DownloadAll(rootdir_ori, defaultXml, branchNames):
	dom = xml.dom.minidom.parse(defaultXml)  
	root = dom.documentElement  
	AndroidVersion=""
	for node in root.getElementsByTagName("default"):
		AndroidVersion=node.getAttribute("revision").replace("refs/tags/", "")
		break;
	#print AndroidVersion
	rootdir=rootdir_ori+"/"+AndroidVersion
	if not os.path.exists(rootdir):  
		os.makedirs(rootdir)  
	os.chdir(rootdir)#Change current work dir
	#Download commands
	prefix = "git clone https://android.googlesource.com/"  
	suffix = ".git"  
	for node in root.getElementsByTagName("project"):  
		d = node.getAttribute("path") 
		if True != isSuitableBranch(d, branchNames):	
			continue
		last = d.rfind("/")
		if last != -1:  
			d = rootdir + "/" + d[:last] 
			if not os.path.exists(d):  
				os.makedirs(d)  
			os.chdir(d)
		branchName = node.getAttribute("name")
		cmd = prefix + branchName + suffix  
		call(cmd)

#Following are certain configurations:
#1.Downloaded source path  
SourceCodeRootDir = "D:/Android/SourceCode"
#2.manifestDir
manifestDir = SourceCodeRootDir+"/"+"manifest";
defaultXml=manifestDir+"/"+"default.xml"
#3.branchNames
branchNames=[
"packages",
"frameworks/base",
"frameworks/opt",
#"frameworks/volley"
]
#4.Start to download:
DownloadAll(SourceCodeRootDir, defaultXml, branchNames)
#Notes:1)The python file is only for Windows;2)About detailed info, refer to Weizhi note
