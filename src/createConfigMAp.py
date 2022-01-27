from email.mime import image
import os
from yaml import loader
from webhook import creaeteWebhook
def configmap(namespace, workdir, imageName ):
    Imagename=imageName.lower()
    os.chdir(workdir)
    os.chdir(workdir+'/'+imageName)
    file=os.listdir()
    print (" ")
    for i in file:
        if '.env' in i:
            os.chdir(workdir+'/'+imageName)
            os.system('kubectl create configmap {} --from-env-file={} --dry-run=client -o yaml > {}/home_dir/{}-configmap.yaml'.format(Imagename, i, workdir, i))
            list = os.popen('kubectl get configmap -n {}'.format(namespace))
            if Imagename in list :
                os.system('kubectl replace -f {}/home_dir/{}-configmap.yaml '.format(workdir, i))
            else:
                os.system('kubectl apply -f {}/home_dir/{}-configmap.yaml '.format(workdir, i))
    os.system('rm -rf {}/{}'.format(workdir, imageName))    
