# AWS-Vulnerable-Lambda
An AWS Lambda vulnerable application written in flask.

### Context 

AWS lambda is a serverless form for deploying your applications.It makes use of the use and throw functionality, where it creates a sandbox and then destroys it once it is done.

AWS lambda works by unzipping your code to a s3 bucket, launches a container in the cluster to represent the function you wrote and the event will be passed on to the function, to get the http request and response it makes use of the AWS API gateway.


### Security 

AWS lambda security issues arise due to improperly configured applications, vulnerable applications being run.It is an interesting space to look around as the box where the function being executed is being destroyed.

AWS lambda can be quite interesting when it is being cold started.

[AWS Lambda cold start & warm ups](https://serverless.com/blog/keep-your-lambdas-warm/).



### Research 

There has been some good research done into this by Rich Jones  [ Gone in 60 milliseconds ](https://media.ccc.de/v/33c3-7865-gone_in_60_milliseconds)

Blackhat Talk 2017 - [HACKING SERVERLESS RUNTIMES: PROFILING AWS LAMBDA, AZURE FUNCTIONS, AND MORE](https://www.blackhat.com/docs/us-17/wednesday/us-17-Krug-Hacking-Severless-Runtimes.pdf)


### Deployment

The vulnerable application makes use of zappa, which is used to deploy serverless applications (AWS Lambda) written in flask or django.

This requires you to create a amazon aws account and a user, copy the access token and the 

* pip install awscli
* virtualenv .venv && source .venv/bin/activate
* pip install -r requirements.txt
* set aws credentials.
* python deploy.py
