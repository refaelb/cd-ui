import os
import sys
import fileinput
import yaml
from yaml import loader

def configmap(namespace, workdir, imageName , home):
    os.chdir(workdir)
    os.system('pwd')
    os.chdir(workdir+'/'+imageName)
    file=os.listdir()
    os.system ('pwd')
    os.system("ls -l")
    print (file)
    for i in file:
        if '.env' in i:
            os.chdir(workdir+'/'+imageName)
            env = open(i,"r+").read() 
            data = open (workdir+'home_dir/'+imageName+'-test-configmap.yaml',"w+")
            tab = ""
            data.write(tab+ str(env))
    os.chdir(workdir+'home_dir')
    o=os.listdir()
    if imageName+'-test-configmap.yaml' in o:
        for i, line in enumerate(fileinput.input(workdir+'home_dir/'+imageName+'-test-configmap.yaml', inplace=1)):
            sys.stdout.write(line.replace('=', ': '))  

        configmap="""
        apiVersion: v1
        kind: ConfigMap
        metadata:
            name: {}ConfigMap
            namespace: {}
        data:
            master: refael """.format(imageName, namespace, )
        os.chdir(workdir+'/home_dir/')
        with open(imageName+'-configmap.yaml', 'w+' ) as file:
            docs = yaml.load(configmap,  Loader=yaml.BaseLoader)
            yaml.dump(docs, file, sort_keys=False)
        with open(workdir+'home_dir/'+imageName+'-test-configmap.yaml','r+')as file:
            with open(workdir+'home_dir/'+imageName+'-configmap.yaml','a+')as fil:
                a = yaml.load(file , Loader=loader.BaseLoader)
                yaml.dump(a,fil, sort_keys=False)
        imagename=imageName.lower()
        os.system('kubectl delete configmap {} -n {}'.format(imagename, namespace))
        os.system('kubectl create configmap {} --from-file={}-configmap.yaml -n {}'.format(imagename, imageName, namespace))   
    os.system('rm -rf {}/{}'.format(workdir, imageName))    