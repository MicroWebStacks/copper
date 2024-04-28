# Pipeline
Service for executing an event based dataflow.

# Concept 
* The input format is a map of Stages and jobs where each provides a python functions entry point.

* Dependencies such as resources and artifacts do not need to be modeled as they are captured from the excution flow using framewrok getters and setters.

* the service can be triggered by a manifest provided on the `pipeline/request` topic.

* the pipeline jobs can optionally be provided as part of the fetch list in a `cache/jobs` folder that can include the stages and jobs manifest

# Details
example manifest
```yaml
fetch:
  - type: github
    repository: HomeSmartMesh/website
    ref: main
    path: repos
    filter: content/**/*
    resource: markdown-content
pipeline:
  process:
    calculate-functions: pipeline.py#calculate
    compute-statistics: pipeline.py#compute
  build:
    generate-website: pipeline.py#build
```
* fetch is a list of resources to pass to the fetcher service
* the fetched resources will be populated in the `/cache` which is mapped to the containers of the services that need it

