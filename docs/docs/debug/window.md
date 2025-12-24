---
sidebar_position: 2
---

# Window

Attributes related to the debugging of Nighty's window.

:::warning

"Attempting to reverse-engineer, decompile, or modify the software" goes against [Nighty's ToS](https://nighty.one/terms-of-service).
<br></br>**Use at your own risk!** Never share scripts that use these attributes publicly.

:::

:::info

Are you searching how to inject custom JavaScript? This feature is coming soon!

:::

## js_api
<p style={{ color: 'gray', marginBottom: '1%' }}>2.0.0</p>
```py
nightylib.debug.js_api: object
```
The hidden JS → Python API used by pywebview.

:::tip

You can inspect this API easily by running `dir(js_api)`.

:::

```py title="Example: hide the interface for 3 seconds"
from nightylib.debug import js_api
import time
js_api.hide()
time.sleep(3)
js_api.show()
```

## open_devtools
<p style={{ color: 'gray', marginBottom: '1%' }}>2.0.0</p>
```py
def nightylib.debug.open_devtools() -> bool
```
Opens the browser's default developer tools for the currently active Nighty window. Returns `True` on success.

:::warning

This feature is currently available on Windows only.

:::

```py title="Example: open devtools"
from nightylib.debug import open_devtools
open_devtools()
```