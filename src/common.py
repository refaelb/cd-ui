from os import read, write, chdir, system 
from pathlib import Path
import yaml
import os
from configParser import configmap
def ci_cd(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass):
  read = """
 #Enter your microsevice's name here.

name: {}
# If you want to overide the full name you can include the 'fullnameOverride' value
#fullname:
replicaCount: 1

images:
  ##########################################################
  #.pullPolicy value is not required,
  #Default value is 'Always',
  #Supported values are "Always", "IfNotPresent" and "Never"
  ##########################################################
  #pullPolicy: Always
  # PullSecrets: [test, test2]
  repository: {}
  tag: {}.{}

service:
  ports:
    - name: http
      port: "3000"
  #################################################################################
  #.type value is not required,
  #Default value is "ClusterIP",
  #supported values are "ClusterIP", "ExternalName", "LoadBalancer" and "NodePort".
  #################################################################################
  #type: ClusterIP
    # - name: http
    #   port: 80
      #############################################################
      #.protocol value is not required, its default value is "TCP".
      #Supported values are "TCP","SCTP" and "UDP"
      #############################################################
    #   protocol: TCP
    # - name: ssh
    #   port: 443
      #######################################################################
      #.targetPort value is not required, its default value is '.port's value.
      #######################################################################
      # targetPort: "5555"

configmap:
  configmaps: {}
  ##################################################################################
  #This option (autorestart_associated_deployments) uses the 'wave' project for k8s,
  #it adds an annotation named 'wave.pusher.com/update-on-config-change,
  #and sets it to "true".
  #for further information please refer to https://github.com/wave-k8s/wave
  ##################################################################################
  #  autorestart_associated_deployments: true
  # env:
  #   - name: DEMO_ENV
  #     value: "hi there"
  #   - name: DEMO_ENV_2
  #     value: "hi again"
#####################################################################
# If you want to add annotation to your serviceAccount,
#please uncomment the following 2 lines and add the dsired annotation.
#####################################################################
# serviceAccount:
#   annotations: "rer"


#####################################################################
# If you want to add volume,
#please uncomment the following lines and add the dsired annotation.
#####################################################################
# volume:
#   - name: azure
#     mountPath: /dist/
#     subPath: test
#   #   secretName: azure-secret
#   #   shareName: momentum/utils
#     type: configMap
#     configMapsName: test



####################################################################################
#Ingress funcionallity is disabled bydefault,
#to enable it, please uncomment the ingress block and fill it with your information.
####################################################################################

ingress:
  enabled: {}
  hosts:
  - host: {}
    paths:
      - path: {}
        service: test
        port: 80
####################################################################
#If you want to add tls verification to your ingress,
#please uncomment the following 4 lines and enter appropriate values
####################################################################
#  tls:
#    - hosts:
#      - examplehostname.com
#      secretName: tls-secret-example

#resources: rer


  """

  workdir='/home/refael/clones/cd-ui/'
  # workdir='/app'
  home='/home/refael/clones/cd-ui/'
  a = repo.rsplit('.',1)[0]
  imageName = a.rsplit('/',3)[3]

  ####ci####
  rep=repo.strip('https://')
  chdir(workdir)
  system('git clone https://{}:{}@{}t'.format(Ruser,Rpass,rep))
  chdir(imageName)
  system('git checkout '+branch)

  ####loop folder####
  pp=os.listdir()
  for image in pp:
      if os.path.isdir(image): 
          chdir(image)
          p=os.listdir()
          if 'Dockerfile' in (p):
              if ingress == image:
                ingress = True
              else: ingress = False 
              system('docker login {} -u {} -p {}'.format(reg,Duser,Dpass))
              system('docker build -t '+reg+':'+image+"."+tag+' .')
              system('docker push '+reg+':'+image+'.'+tag)
              # system('docker rmi $(docker images)')
              ###deploy###
              chdir(workdir+'/home_dir')
              f = open (image+'-values.yaml', 'a+')
              confFile = image+"-configmap"
              file = open(image+"-values.yaml","w+")
              docs = yaml.load(read.format(image,reg,image,tag,confFile,ingress,host,"peth"),  Loader=yaml.FullLoader)
              yaml.dump(docs, file, sort_keys=False)
              file.close()
              system("kubectl create ns {}".format(namespace))
              list = os.popen("helm list -n {} | awk '{{ print $1 }}'".format(namespace)).read()
              print(list)
              if image in list:
                system("helm upgrade {} common  -n {} -f {}-values.yaml".format(image,  namespace, image))
              else:
                system("helm install {} common  -n {} -f {}-values.yaml ".format(image,  namespace, image))
              chdir(workdir+'/'+imageName)
          else:
              chdir('./..')
  #configmap##
  configmap(namespace,workdir,imageName,home)