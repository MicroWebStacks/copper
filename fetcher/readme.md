# Init
docker network create my-network

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

