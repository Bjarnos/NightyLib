---
sidebar_position: 5
---

# Sensitive

Attributes related to sensitive files in Nighty's %APPDATA%.

:::warning

"Attempting to reverse-engineer, decompile, or modify the software" goes against [Nighty's ToS](https://nighty.one/terms-of-service).
<br></br>**Use at your own risk!** Never share scripts that use these attributes publicly.

:::

## token
<p style={{ color: 'gray', marginBottom: '1%' }}>2.0.0</p>
```py
nightylib.debug.token: str
```
The Nighty license key of the current user.

## settings
<p style={{ color: 'gray', marginBottom: '1%' }}>2.0.0</p>
```py
nightylib.debug.settings: nightylib.util.EditableJSON
```
The current user’s Nighty settings, formatted as an editable object.

```py title="Example: change the current user's prefix"
from nightylib.debug import settings
settings.prefix = "!"
```

:::tip

Check out the docs of the `EditableJSON` class [here](/docs/util/files#editablejson).

:::

```json title="Example dumped config as of 24-12-2025"
{
  "prefix": ".",
  "deletetimer": 40,
  "riskmode": false,
  "dmlogger": "off",
  "nitrosniper": true,
  "theme": "nighty",
  "logins": {
    "unalived.hunter": {
      "token": "MT...ns",
      "date_added": "21 December 2025, at 11:25:01",
      "active": true,
      "app": {
        "id": "14...76",
        "token": "MT...kM"
      }
    }
  },
  "spotify_username": null,
  "session": "windows",
  "private": true,
  "nsfw": false,
  "nighty_discoverable": null,
  "forward": false,
  "web": false
}
```