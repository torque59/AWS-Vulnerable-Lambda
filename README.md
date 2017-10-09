# AWS-Vulnerable-Lambda
An AWS Lambda vulnerable application written in flask.

### Context 

AWS lambda is a serverless platform for deploying your applications.It makes use of the use and throw functionality, where it creates a sandbox and then destroys it once it is done.

AWS lambda works by unzipping your code to a s3 bucket, launches a container in the cluster to represent the function you wrote and the event will be passed on to the function, to take care of the http request and response it makes use of the AWS API gateway.


### Security 

AWS lambda security issues arise due to improperly configured applications or vulnerable applications being run.It is an interesting space to look around.You could escalate from the function code to the inner aws architecture which might be being used.

AWS lambda can be quite interesting when it is being kept warm. [AWS Lambda cold start & warm ups](https://serverless.com/blog/keep-your-lambdas-warm/).



### Research 

There has been some awesome research done into AWS lambda, some of these are i would highly recommend to read upon:

* Infiltration by Rich Jones  [ Gone in 60 milliseconds ](https://media.ccc.de/v/33c3-7865-gone_in_60_milliseconds)

* Blackhat Talk 2017 - [HACKING SERVERLESS RUNTIMES: PROFILING AWS LAMBDA, AZURE FUNCTIONS, AND MORE](https://www.blackhat.com/docs/us-17/wednesday/us-17-Krug-Hacking-Severless-Runtimes.pdf)


### Deployment

The vulnerable application makes use of zappa, which is used to deploy serverless applications (AWS Lambda) written in flask or django.

#### Configure your zappa_settings

* Change the s3 bucket name to a unique one preferably which is not used.
* Incase you use a different aws-region mention it in the file as well.

This requires you to create a amazon aws account and a user with lambda,s3 and api gateway permissions enabled, copy the access token and the paste it within ~/.aws/credentials.

* pip install awscli
* virtualenv .venv && source .venv/bin/activate
* pip install -r requirements.txt
* set aws credentials.(Create a new user in your aws account and add it in ~/.aws/credentials)
* bash deploy.sh
* Use the url in the format - https://url/dev/?ping=ls

** This is by no means meant for deploying at production, use it at your own risk.


### Screenshots

![alt text](https://i.imgur.com/tiGlinR.png "App Sample")



