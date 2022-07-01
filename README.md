# deployment_practice
interview for Habitat
## Run instructions:
data pull service:
`docker build `
predict service:
``
## Development plan:
- Unfortunately, I have other projects to juggle at the moment, and I can't finish all I'd like to do with this. 
- A lot of this would be for a more important/larger project with high development time spent. Some of this would be cut for something that is this simple. 
- Next steps include:
- Terraform setup for all infrastructure. 
- aws eventbridge and lambda container setup for data pull service on time schedule.
- Testing for code
- documenting usage etc. 
- Setting test and production env variables for local(dev)/cloud(prod/testing) databases and object stores
- MLFlow server setup for future experimentation.  
- aws api gateway, fastAPI setup on lambda container for calling prediction task. fast API Spins up ec2 for prediction running for the smaller linear regression model . 
- vpc, networking etc. setup
- docker image repository setup on aws ecr. 
- github actions or equivalent setup for builds and tests and upload of images on push/merge to main.
- Possibly feature store setup. 
