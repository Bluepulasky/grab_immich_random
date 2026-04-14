# grab_immich_random

please put your API key inside a config.local.yaml

structure:
```yaml
immmich:
  api_key:
```

## Implementation Overview

### Template yml

```html
- widgets: 
    - type: custom-api
        title: Random Immich Photo
        url: http://<localhost>:8085/immich/random
        cache: 6h
        template: |
        <a href="http://<localhost>:2283/photos/{{ .JSON.String "id" }}" target="_blank" style="display:block; text-decoration:none;">
            <div style="width:100%; aspect-ratio:1/1; overflow:hidden; border-radius:4px;">
            <img src="http://<localhost>:2283/api/assets/{{ .JSON.String "id" }}/thumbnail?size=preview" style="width:100%; height:100%; object-fit:cover;">
            </div>
            <p style="text-align:center; font-size:12px; color:#a0b4d0; margin-top:6px;">{{ .JSON.String "date" }}</p>
        </a>
