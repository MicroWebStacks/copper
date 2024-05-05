# Runner
Service for running a list of actions workflow

# usage
example workflow is a list of actions, where each has an `action` field which is an MQTT service endpoint.
* The item will be published on the action topic
* the finish topic is awaited for e.g. `fetcher/fetch/finish`
* The next item is then published

```yaml
- action: fetcher/fetch
  type: github
  repository: MicroWebStacks/astro-big-doc
  ref: main
  filter: content/*
  resource: test-website
- action: markdown/build
  resource: test-website
  path: /fetch/test-website/content
```
