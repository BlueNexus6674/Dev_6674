#! /bin/bash

Name=ROS_Automate
Imports=(PyQt6 logging-config)
Datas=(Internal_Data Install_Data)
OneFile=1
Release=1

# ----------------
HiddenImportString=

for Import in ${Imports[@]}
do
	HiddenImportString="$HiddenImportString --hidden-import=$Import"
done

DataString=

# ----------------

for Data in ${Datas[@]}
do
	DataString="$DataString --add-data=./$Data:./$Data"
done

# ----------------

OneFileOut=
if [ $OneFile -eq 1 ]
then
	OneFileOut=--onefile
fi

# ----------------
cd ./src/
PyName=$Name.py
pyinstaller $PyName $HiddenImportString $DataString $OneFileOut  -y 

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
cd ../
	
