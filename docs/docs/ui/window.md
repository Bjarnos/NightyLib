---
sidebar_position: 1
---

# Window

Attributes related to Nighty's pywebview <code>window</code> object.

**Required background:** The Nighty GUI is fully powered by the Python library [pywebview](https://pywebview.flowrl.com/).
This means the entire interface is built with HTML, CSS, and JavaScript, giving it all the capabilities of a standard website, while also integrating a Python backend.

:::tip

Devtools can help a lot when developing custom looks for Nighty. Go to the [Debug - Window](/docs/debug/window#open_devtools) section to learn how to open it.

:::

## window
<p style={{ color: 'gray', marginBottom: '1%' }}>2.0.0</p>
```py
nightylib.ui.window: webview.Window
```
The `window` object allows you to control Nighty’s window and appearance.

:::tip

For more details, see [pywebview's window documentation](https://pywebview.flowrl.com/api/#webview-window), which also explains how to inject custom JavaScript.

:::

```py title="Example: move the entire interface 50 pixels on the x axis"
from nightylib.ui import window
window.move(window.x + 50, window.y)
```
