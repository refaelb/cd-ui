import os
import sys
import fileinput
import yaml
from yaml import loader
def configmap(namespace, workdir, imageName ):
    os.chdir(workdir)
    os.system('pwd')

    for root, dirs, files in os.walk(workdir+'/'+imageName):
        for file in files:
            if file.endswith('.env'):
                print(file)
                os.chdir(workdir+'/'+imageName)
                env = open(file,"r+").read() 
                data = open(workdir+"/home_dir/"+imageName+"-test-configmap.yaml","w+")
                tab = ""
                data.write(tab+ str(env))
                
    for i, line in enumerate(fileinput.input(workdir+'/home_dir/'+imageName+'-test-configmap.yaml', inplace=1)):
        sys.stdout.write(line.replace('=', ': '))  

    configmap="data:  "
    os.chdir(workdir+'/home_dir/')
    with open(imageName+'-configmap.yaml', 'w+' ) as file:
        docs = yaml.load(configmap,  Loader=yaml.BaseLoader)
        yaml.dump(docs, file, sort_keys=False)
    with open(workdir+'/home_dir/'+imageName+'-test-configmap.yaml','r+')as file:
        with open(workdir+'/home_dir/'+imageName+'-configmap.yaml','a+')as fil:
            a = yaml.load(file , Loader=loader.BaseLoader)
            yaml.dump(a,fil, sort_keys=False)
    for i, line in enumerate(fileinput.input(workdir+'/home_dir/'+imageName+'-configmap.yaml', inplace=1)):
        sys.stdout.write(line.replace('\n', '\n  '))  

    configmap="""
    master: refael
    apiVersion: v1
    kind: ConfigMap
    metadata:
        name: {}-ConfigMap
        namespace: {} """.format(imageName, namespace, )
    os.chdir(workdir+'/home_dir/')
    with open(imageName+'-configmap.yaml', 'a+' ) as file:
        docs = yaml.load(configmap,  Loader=yaml.BaseLoader)
        yaml.dump(docs, file, sort_keys=False)
    os.system('kubectl create configmap {} --from-file={}-configmap.yaml -n {}'.format(imageName, imageName, namespace))   
    

configmap('fre', '/home/refael/clones/cd-ui/src', 'SuperNova')