FROM docker:20.10.10-alpine3.14

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN apk add git
RUN apk add curl

##kubectl##
WORKDIR /usr/src/app
RUN apk add curl openssl bash --no-cache
RUN curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x ./kubectl \
    && mv ./kubectl /usr/local/bin/kubectl \
    && curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 \
    && chmod +x get_helm.sh && ./get_helm.sh

##az##
# RUN apk add py3-pip
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo make
RUN pip3 install azure-cli

# CMD az account set --subscription e0cc7faf-3760-4b0c-a9df-fecf8d900589
# CMD az aks get-credentials --resource-group Integration --name Integration
# CMD az login  --username "Ontario-135@greendreamteam.onmicrosoft.com" --password "refael316444058" --tenant "c9ad96a7-2bac-49a7-abf6-8e932f60bf2b" 

##app##

COPY . /app
WORKDIR /app
RUN chmod +x connect.sh
ENV FLASK_APP=index.py
# COPY config /app
# COPY ./requirements.txt /app/requirements.txt
# COPY ./connect.sh /app/connect.sh
RUN pip3 install  -r /app/requirements.txt
RUN [ "./connect.sh" ]
CMD [ "flask", "run", "--host=0.0.0.0"]
