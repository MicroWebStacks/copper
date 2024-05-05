# Copper
The basic material for creating pipelines

colelction of containers utilities providing services for websites and data management

![concept](./design/concept.drawio.svg)

# Usage
```bash
cd copper
docker compose up
```
publish on `fetcher/fetch` a list of items to fetch

```json
[
    {
        "type":         "github",
        "repository":   "HomeSmartMesh/website",
        "ref":          "main",
        "filter":       "content/3dprinting/*",
        "resource":     "markdown-content",
        "action":       "markdown/build"
    }
]
```

example response `fetcher/finish`

```json
[
  {
    "type": "github",
    "repository": "HomeSmartMesh/website",
    "ref": "main",
    "filter": "content/3dprinting/*",
    "resource": "markdown-content",
    "action": "markdown/build",
    "path": "/fetch/markdown-content",
    "total_files": 756,
    "filtered_files": 114,
    "size_bytes": 128598393,
    "size_text": "122 MB 656 KB",
    "duration": "0:00:33.198159",
    "duration_text": "33 s 198 ms"
  }
]
```
## parameters
* `dest` is optional if it is needed to specify a target path
```json
[
    {
        "dest": "repos/HomeSmartMesh/website",
    }
]
```

* `action` will publish the same completion result on the provided action topic which can trigger a request of a following service



![Broker](./design/broker.png)

# Concept

## service structure
a service consists of
* a docker container as a Dockerfile or folder
* an mqtt client to manage services and events
* optionally for bootstrapping a MANIFEST environemnt variable can be passed to use a local file

## broker API
* Services lifecycle management
    * start and stop a service
    * Lambda single shot a service for a single request
* Requests
    * subscribe to offer a service
    * publish to trigger
    * publish status and completion
* Resources
    * subscribe to consume
    * publish to produce

## content locations
* a core service within copper
* a local repo service
* a remote url service

## visualization
* collection of mosquitto logs allows to trace services publish and subscribe to generate a dependencies graph

## Events vs REST
two types of corss services interactions will be used :
* Event based
    * suitable for long running jobs
    * single instance
    * central MQTT broker

    A slow interaction is an an operation that
    * can require a long time to process such as more than 30s or minutes or hours.
    * is only initiated by a single service client
    * requests do not need to be queued
    * is needed sporadically or scheduled with jobs which preiod is necessarily bigger if not significantly bigger than the time it takes them to complete

* REST API
    * suitable for fast running jobs
    * multiple instances of independent clients
    * http REST API

    A fat interaction is an an operation that
    * completes necessarily within less any default request timeout config
    * can be initiated by any number of independent clients
    * requests need to be queued
    * is needed very frequently such as converting a high number of files

## docker in docker
as alternative to wrapping everything in a service API call, it is possible to execute docker commands from within docker with the Docker-in-Docker approach. This requires mounting the docker socket to communicate with the daemon.

# TODOs
* remove PyYaml could not isntall on windows and dependabot alert
* make filter optional and support glob variant
