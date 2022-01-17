from os import read, write, chdir, system 
from pathlib import Path
import yaml
import os
from configParser import configmap


workdir = "/home/refael/clones/cd-ui/"
Imagename = "supernova"
with open(workdir+'home_dir/'+Imagename+'-test-configmap.yaml','r+')as file:
    for i in file:
        print(i)
        print ('refael')
        
        with open(workdir+'home_dir/'+Imagename+'-test-.yaml','a+')as f:
            yaml.load(i)
            yaml.dump(file,f)
            # print (f)
            
        