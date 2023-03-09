#! /bin/bash

Name=ROS_Automate
Imports=(PyQt6 logging-config)
OneFile=1
Release=1

# ----------------
HiddenImportString=

for Import in ${Imports[@]}
do
	HiddenImportString="$HiddenImportString --hidden-import=$Import"
done

# ----------------

OneFileOut=
if [ $OneFile -eq 1 ]
then
	OneFileOut=--onefile
fi

# ----------------

PyName=$Name.py
pyinstaller $PyName $HiddenImportString $OneFileOut --add-data ./Data:./Data -y 
# ----------------

rm -r ../Output
mkdir ../Output

if [ $OneFile -eq 1 ]
then
	cp ./dist/$Name ../Output/$Name
fi

if [ $OneFile -eq 1 ]
then
	if [ $Release -eq 1 ]
	then
		cp ../Output/$Name ../$Name
	fi
fi

mv dist ../Output/dist
mv build ../Output/build
mv $Name.spec ../Output/$Name.spec
	
