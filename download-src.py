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
def DownloadAll(rootdir_ori, defaultXml, prefix, branchNames, suffix):
	dom = xml.dom.minidom.parse(defaultXml)  
	root = dom.documentElement  
	for node in root.getElementsByTagName("default"):
		AndroidVersion=node.getAttribute("revision").replace("refs/tags/", "")
		break;
	print AndroidVersion
	rootdir=rootdir_ori+"/"+AndroidVersion
	if not os.path.exists(rootdir):  
		os.makedirs(rootdir)  
	os.chdir(rootdir)#Change current work dir

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
#1.git program path  
git = "D:/Software/PortableGit-1.8.4-preview20130916_dinit_rev6/PortableGit-1.8.4-preview20130916/bin/git.exe" 
#2.manifestDir
manifestDir = "E:/Android/SourceCode/manifest";
defaultXml=manifestDir+"/"+"default.xml"
#3.Downloaded source path  
SourceCodeRootDir = "E:/Android/SourceCode/AndroidN"
#4.Download commands
prefix = "git clone https://android.googlesource.com/"  
suffix = ".git"  

#5.Start to download:
branchNames=[
"packages",
"frameworks/base",
"frameworks/opt",
#"frameworks/volley"
]
DownloadAll(SourceCodeRootDir, defaultXml, prefix, branchNames, suffix)
#Notes:1)The python file is only for Windows;2)About detailed info, refer to YinXiang note
