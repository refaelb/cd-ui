import os
import sys
import fileinput
import yaml
from yaml import loader

def configmap(namespace, workdir, imageName , home):
    Imagename=imageName.lower()
    os.chdir(workdir)
    os.chdir(workdir+'/'+imageName)
    file=os.listdir()
    print (file)
    for i in file:
        if '.env' in i:
            os.chdir(workdir+'/'+imageName)
            env = open(i,"r+").read() 
            data = open (workdir+'home_dir/'+Imagename+'-test-configmap.yaml',"w+")
            tab = ""
            data.write(tab+ str(env))
    os.chdir(workdir+'home_dir')
    o=os.listdir()
    if imageName+'-test-configmap.yaml' in o:
        for i, line in enumerate(fileinput.input(workdir+'home_dir/'+Imagename+'-test-configmap.yaml', inplace=1)):
            sys.stdout.write(line.replace('=', ': '))  

        configmap="""
        apiVersion: v1
        kind: ConfigMap
        metadata:
            name: {}-configmap
            namespace: {}
        data:
            master: refael """.format(Imagename, namespace, )
        os.chdir(workdir+'/home_dir/')
        with open(Imagename+'-configmap.yaml', 'w+' ) as file:
            docs = yaml.load(configmap,  Loader=yaml.BaseLoader)
            yaml.dump(docs, file, sort_keys=False)
        with open(workdir+'home_dir/'+Imagename+'-test-configmap.yaml','r+')as file:
            with open(workdir+'home_dir/'+Imagename+'-configmap.yaml','a+')as fil:
                a = yaml.load(file , Loader=loader.BaseLoader)
                yaml.dump(a,fil, sort_keys=False)
        list = os.popen('kubectl get configmap -n {}'.format(namespace))
        if Imagename in list :
            os.system('kubectl replace -f {}-configmap.yaml --validate=false'.format(Imagename))
        else:
            os.system('kubectl apply -f {}-configmap.yaml --validate=false'.format(Imagename))
    os.system('rm -rf {}/{}'.format(workdir, imageName))    