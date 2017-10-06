# AWS-Vulnerable-Lambda
An AWS Lambda vulnerable application written in flask.

### Context 

AWS lambda is a serverless form for deploying your applications.It makes use of the use and throw functionality, where it creates a sandbox and then destroys it once it is done.


### Security 

AWS lambda security issues arise due to improperly configured applications, vulnerable applications being run.It is an interesting space to look around as the box where the function being executed is being destroyed.

AWS lambda can be quite interesting when it is being cold started.

[AWS Lambda cold start & warm ups](https://serverless.com/blog/keep-your-lambdas-warm/).



### Research 

There has been some good research done into this by Rich Jones  [ Gone in 60 milliseconds ](https://media.ccc.de/v/33c3-7865-gone_in_60_milliseconds)

Blackhat Talk 2017 - [HACKING SERVERLESS RUNTIMES: PROFILING AWS LAMBDA, AZURE FUNCTIONS, AND MORE](https://www.blackhat.com/docs/us-17/wednesday/us-17-Krug-Hacking-Severless-Runtimes.pdf)