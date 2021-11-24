from os import read, write, chdir, system 
from pathlib import Path
import yaml
import os
from configParser import configmap
def ci_cd(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass):
  data='''
  replicaCount: 1

  image:
    repository: {}
    pullPolicy: Always
    # Overrides the image tag whose default is the chart appVersion.
    tag: {}.{}

  imagePullSecrets: []
  nameOverride: ""
  fullnameOverride: ""
  configmap: {}
  '''
  dataService = """
    serviceAccount:
      # Specifies whether a service account should be created
      create: true
      # Annotations to add to the service account
      annotations: {}
      # The name of the service account to use.
      # If not set and create is true, a name is generated using the fullname template
      name: ""

    podAnnotations: {}

    podSecurityContext: {}
      # fsGroup: 2000

    securityContext: {}
      # capabilities:
      #   drop:
      #   - ALL
      # readOnlyRootFilesystem: true
      # runAsNonRoot: true
      # runAsUser: 1000

    service:
      type: ClusterIP
      port: 3000

    ingress:
      enabled: {}
      annotations: 
        kubernetes.io/ingress.class: addon-http-application-routing
        # kubernetes.io/ingress.class: nginx
        # kubernetes.io/tls-acme: "true"
      hosts:
        - host: {}
          paths:
          - path: /
            pathType: ImplementationSpecific
            backend:
              serviceName: chart-example.local
              servicePort: 3000
      tls: []
      #  - secretName: chart-example-tls
      #    hosts:
      #      - chart-example.local

    resources: {}
      # We usually recommend not to specify default resources and to leave this as a conscious
      # choice for the user. This also increases chances charts run on environments with little
      # resources, such as Minikube. If you do want to specify resources, uncomment the following
      # lines, adjust them as necessary, and remove the curly braces after 'resources:'.
      # limits:
      #   cpu: 100m
      #   memory: 128Mi
      # requests:
      #   cpu: 100m
      #   memory: 128Mi

    autoscaling:
      enabled: false
      minReplicas: 1
      maxReplicas: 100
      targetCPUUtilizationPercentage: 80
      # targetMemoryUtilizationPercentage: 80

    nodeSelector: {}

    tolerations: []

    affinity: {}

  """
 
  workdir='/home/refael/clones/cd-ui/src'
  a = repo.rsplit('.',1)[0]
  imageName = a.rsplit('/',3)[3]

  ##configmap##
  chdir(workdir+'/home_dir')
  file = os.listdir()
  c=os.listdir()
  if '{}-configmap.yaml' in c:
    configmap(namespace,workdir,imageName)

  ####ci####
  rep=repo.strip('https://')
  system('git clone https://{}:{}@{}t'.format(Ruser,Rpass,rep))
  chdir(imageName)
  system('git checkout '+branch)

  ####loop folder####
  p=os.listdir()
  for image in p:
      if os.path.isdir(image): 
          chdir(image)
          p=os.listdir()
          if 'Dockerfile' in (p):
              if ingress == p:
                ingress = True
              else: ingress = False 
              system('docker login {} -u {} -p {}'.format(reg,Duser,Dpass))
              system('docker build -t '+reg+':'+image+"."+tag+' .')
              system('docker push '+reg+':'+image+'.'+tag)
              ###deploy###
              Path(workdir+"/home_dir").mkdir(parents=True, exist_ok=True)
              chdir(workdir+"/home_dir")
              system("kubectl create ns {}".format(namespace))
              system("helm create "+image )
              confFile = image+"-configmap"
              file = open(image+"/values.yaml","w+")
              docs = yaml.load(data.format(reg, image, tag, confFile),  Loader=yaml.FullLoader)
              yaml.dump(docs, file, sort_keys=False)
              file = open(image+"/values.yaml","a+")
              docs = yaml.load(dataService.format("","","","",ingress,host,"","",""),  Loader=yaml.FullLoader)
              yaml.dump(docs, file,sort_keys=False)
              file.close()
              list = os.popen("helm list -n {} | awk '{{ print $1 }}'".format(namespace)).read()
              if image in (list):
                system("helm upgrade {} {}  -n {} ".format(image, image, namespace))
              else:
                system("helm install {} {}  -n {} ".format(image, image, namespace))
              chdir(workdir+'/'+imageName)
          else:
              chdir('./..')
  