# MQTT test

publish on `fetcher/request`

```json
{
    "fetch_list": [
        {
            "type": "github",
            "repository":   "HomeSmartMesh/website",
            "ref":  "main",
            "path": "repos",
            "filter":   "content/3dprinting/**/*"
        }
    ]
}
```

smaller content

```json
{
    "fetch_list": [
        {
            "type": "github",
            "repository":   "HomeSmartMesh/raspi",
            "ref":  "master",
            "path": "repos",
            "filter":   "design/*"
        }
    ]
}
```
