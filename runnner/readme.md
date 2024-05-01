# Runner
Service for running an event based workflow

# Concept 
* The input format is a map of Stages and jobs where each provides a python functions entry point.

* Dependencies such as resources and artifacts do not need to be modeled as they are captured from the excution flow using framewrok getters and setters.

## triggers
* a local manifest file passed through an environment variable
* a manifest provided on the `runner/request` topic.
* fetch resource published in `fetcher/resources/runner-manifest`

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

