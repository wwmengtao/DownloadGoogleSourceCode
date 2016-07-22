#! /usr/bin/python
import xml.dom.minidom  
import os  
import string  
from subprocess import call  

#Downloads certain branchs
def isSuitableBranch(pathName, branchNameTuple):
	for branch in branchNameTuple:
		if pathName.startswith(branch):
			return True
	return False;
	

#Downloads All Android SourceCode
def DownloadAll(rootdir, defaultXml, prefix, branchNameTuple, suffix):
	dom = xml.dom.minidom.parse(defaultXml)  
	root = dom.documentElement  
	if not os.path.exists(rootdir):  
		os.mkdir(rootdir)  
	  
	for node in root.getElementsByTagName("project"):  
		os.chdir(rootdir)  
		d = node.getAttribute("path") 
		pathName=d
		last = d.rfind("/")
		if last != -1:  
			d = rootdir + "/" + d[:last]  
			if not os.path.exists(d):  
				os.makedirs(d)  
			os.chdir(d)
		branchName = node.getAttribute("name")
		if True==isSuitableBranch(pathName, branchNameTuple):
			print branchName
			cmd = prefix + branchName + suffix  
			call(cmd)

#Following are certain configurations:
#1.git program path  
git = "D:/Software/PortableGit-1.8.4-preview20130916_dinit_rev6/PortableGit-1.8.4-preview20130916/bin/git.exe" 
#2.default.xml
defaultXml = "E:/Android/SourceCode/manifest/default.xml";
#3.Downloaded source path  
rootdir = "E:/Android/SourceCode/Android6.x"  
#4.Download commands
prefix = "git clone https://android.googlesource.com/"  
suffix = ".git"  

#Start to download:
branchNameTuple=[
"packages/apps",
"frameworks/base"
]
DownloadAll(rootdir, defaultXml, prefix, branchNameTuple, suffix)
cf=input()
