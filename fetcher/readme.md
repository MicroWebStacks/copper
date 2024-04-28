# Fetcher
Service for fetching data and storing it in cache. Fetcher is an MQTT client subscribed to the `fetcher/request` topic.

# Testing

publish on `fetcher/request`

* `markdown-content`
```json
{
    "fetch_list": [
        {
            "type": "github",
            "repository":   "HomeSmartMesh/website",
            "ref":  "main",
            "path": "repos",
            "filter":   "content/3dprinting/**/*",
            "resource": "markdown-content"
        }
    ]
}
```

* `raspi-design`

```json
{
    "fetch_list": [
        {
            "type": "github",
            "repository":   "HomeSmartMesh/raspi",
            "ref":  "master",
            "path": "repos",
            "filter":   "design/*",
            "resource": "raspi-design"
        }
    ]
}
```

example response `fetcher/completion`

```json
[
    {
        "type": "github",
        "repository": "HomeSmartMesh/raspi",
        "ref": "master",
        "path": "repos",
        "filter": "design/*",
        "resource": "markdown-content",
        "total_files": 688,
        "filtered_files": 22,
        "size_bytes": 5920465,
        "size_text": "5 MB 661 KB",
        "duration": "0:00:03.293742",
        "duration_text": "3 s 293 ms"
    }
]
```
