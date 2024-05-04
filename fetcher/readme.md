# Fetcher
Service for fetching data and storing it in cache. Fetcher is an MQTT client subscribed to the `fetcher/fetch` topic.

# Usage

publish on `fetcher/fetch`

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

example response `fetcher/completion`

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

