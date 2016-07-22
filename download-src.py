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
	rootdir=rootdir_ori+AndroidVersion
	if not os.path.exists(rootdir):  
		os.mkdir(rootdir)  
	  
	for node in root.getElementsByTagName("project"):  
		os.chdir(rootdir)#Change current work dir
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
rootdir = "E:/Android/SourceCode/"
#4.Download commands
prefix = "git clone https://android.googlesource.com/"  
suffix = ".git"  

#Start to download:
branchNames=[
"packages",
"frameworks/base"
]
DownloadAll(rootdir, defaultXml, prefix, branchNames, suffix)

"""
#"cd manifest" and execute "git checkout xx"
android-2.1_r2_
android-2.2.1_r1_
android-2.2.1_r2_
android-2.2.2_r1_
android-2.2.3_r1
android-2.2.3_r2
android-2.2.3_r2.1
android-2.2_r1.1_
android-2.2_r1.2_
android-2.2_r1.3_
android-2.2_r1_
android-2.3.1_r1_
android-2.3.2_r1_
android-2.3.3_r1.1
android-2.3.3_r1_
android-2.3.4_r0.9
android-2.3.4_r1_
android-2.3.5_r1_
android-2.3.6_r0.9
android-2.3.6_r1
android-2.3.7_r1
android-2.3_r1_
android-4.0.1_r1
android-4.0.1_r1.1
android-4.0.1_r1.2
android-4.0.2_r1
android-4.0.3_r1
android-4.0.3_r1.1
android-4.0.4_r1
android-4.0.4_r1.1
android-4.0.4_r1.2
android-4.0.4_r2
android-4.0.4_r2.1
android-4.1.1_r1
android-4.1.1_r1.1
android-4.1.1_r1_
android-4.1.1_r2
android-4.1.1_r3
android-4.1.1_r4
android-4.1.1_r5
android-4.1.1_r6
android-4.1.1_r6.1
android-4.1.2_r1
android-4.1.2_r2
android-4.1.2_r2.1
android-4.2.1_r1.1
android-4.2.1_r1.2
android-4.2.1_r1__
android-4.2.2_r1.1
android-4.2.2_r1.2
android-4.2.2_r1_
android-4.2_r1___
android-4.3.1_r1
android-4.3_r0.9
android-4.3_r0.9.1
android-4.3_r0.9.1
android-4.3_r0.9_
android-4.3_r1
android-4.3_r1.1
android-4.3_r1_
android-4.3_r2
android-4.3_r2.1_
android-4.3_r2.1__
android-4.3_r2.2
android-4.3_r2.3
android-4.3_r2_
android-4.3_r3
android-4.3_r3.1
android-4.4.1_r1
android-4.4.1_r1.0
android-4.4.2_r1
android-4.4.2_r1.0
android-4.4.2_r2
android-4.4.2_r2.0
android-4.4.3_r1
android-4.4.3_r1.0
android-4.4.3_r1.1
android-4.4.3_r1.1
android-4.4.4_r1
android-4.4.4_r1.0
android-4.4.4_r2
android-4.4.4_r2.0
android-4.4_r1
android-4.4_r1.0.1
android-4.4_r1.1
android-4.4_r1.1.0
android-4.4_r1.2
android-4.4_r1.2.0
android-4.4w_r1
android-5.0.0_r1
android-5.0.0_r1.0
android-5.0.0_r2
android-5.0.0_r2.0
android-5.0.0_r3
android-5.0.0_r3.0
android-5.0.0_r4
android-5.0.0_r4.0
android-5.0.0_r5
android-5.0.0_r5.0
android-5.0.0_r5.1
android-5.0.0_r5.1
android-5.0.0_r6
android-5.0.0_r6.0
android-5.0.0_r7
android-5.0.0_r7.0
android-5.0.1_r1
android-5.0.2_r1
android-5.0.2_r3
android-5.1.0_r1
android-5.1.0_r3
android-5.1.0_r4
android-5.1.0_r5
android-5.1.1_r1
android-5.1.1_r10
android-5.1.1_r12
android-5.1.1_r13
android-5.1.1_r14
android-5.1.1_r15
android-5.1.1_r16
android-5.1.1_r17
android-5.1.1_r18
android-5.1.1_r19
android-5.1.1_r2
android-5.1.1_r20
android-5.1.1_r22
android-5.1.1_r23
android-5.1.1_r24
android-5.1.1_r25
android-5.1.1_r26
android-5.1.1_r28
android-5.1.1_r29
android-5.1.1_r3
android-5.1.1_r30
android-5.1.1_r33
android-5.1.1_r34
android-5.1.1_r35
android-5.1.1_r36
android-5.1.1_r37
android-5.1.1_r38
android-5.1.1_r4
android-5.1.1_r5
android-5.1.1_r6
android-5.1.1_r7
android-5.1.1_r8
android-5.1.1_r9
android-6.0.0_r1
android-6.0.0_r11
android-6.0.0_r12
android-6.0.0_r13
android-6.0.0_r2
android-6.0.0_r23
android-6.0.0_r24
android-6.0.0_r25
android-6.0.0_r26
android-6.0.0_r3
android-6.0.0_r4
android-6.0.0_r41
android-6.0.0_r5
android-6.0.0_r6
android-6.0.0_r7
android-6.0.1_r1
android-6.0.1_r10
android-6.0.1_r11
android-6.0.1_r12
android-6.0.1_r13
android-6.0.1_r16
android-6.0.1_r17
android-6.0.1_r18
android-6.0.1_r20
android-6.0.1_r21
android-6.0.1_r22
android-6.0.1_r24
android-6.0.1_r25
android-6.0.1_r26
android-6.0.1_r27
android-6.0.1_r28
android-6.0.1_r3
android-6.0.1_r30
android-6.0.1_r31
android-6.0.1_r32
android-6.0.1_r33
android-6.0.1_r4
android-6.0.1_r40
android-6.0.1_r41
android-6.0.1_r42
android-6.0.1_r43
android-6.0.1_r45
android-6.0.1_r46
android-6.0.1_r47
android-6.0.1_r48
android-6.0.1_r49
android-6.0.1_r5
android-6.0.1_r50
android-6.0.1_r51
android-6.0.1_r52
android-6.0.1_r53
android-6.0.1_r54
android-6.0.1_r55
android-6.0.1_r7
android-6.0.1_r8
android-6.0.1_r9
"""