# grab_immich_random

## Implementation Overview

### Custom API Details

- **Type**: custom-api
- **Title**: Random Immich Photo
- **URL**: [http://LOCALHOST:<port>/immich/random](http://LOCALHOST:<port>/immich/random)
- **Cache Duration**: 6 hours

### Template

```html
<a href="http://LOCALHOST:2283/photos/{{ .JSON.String "id" }}" target="_blank" style="display:block; text-decoration:none;">
    <div style="width:100%; aspect-ratio:1/1; overflow:hidden; border-radius:4px;">
        <img src="http://LOCALHOST:2283/api/assets/{{ .JSON.String "id" }}/thumbnail?size=preview" style="width:100%; height:100%; object-fit:cover;">
    </div>
    <p style="text-align:center; font-size:12px; color:#a0b4d0; margin-top:6px;">{{ .JSON.String "photo_date" }}</p>
</a>