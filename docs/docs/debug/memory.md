---
sidebar_position: 1
---

# Memory

Attributes related to Nighty's memory.

**Required background:** All custom Python scripts executed in Nighty run in the same context as Nighty’s main script and share the same `globals()`. Naturally, this means you can do a bit of spying.

:::warning

"Attempting to reverse-engineer, decompile, or modify the software" goes against [Nighty's ToS](https://nighty.one/terms-of-service).
<br></br>**Use at your own risk!** Never share scripts that use these attributes publicly.

:::

## memory
<p style={{ color: 'gray', marginBottom: '1%' }}>2.0.0</p>
```py
nightylib.debug.memory: types.SimpleNamespace
```
A powerful attribute that provides access to an active class instance from the main Nighty thread.

This is especially useful because calling a method like `NotificationSender.sendToast(None, *args, **kwargs)` would fail if self is accessed. To prevent this, `memory` stores a single active instance per class, indexed by the class name.

```py title="Example: show a toast notification"
from nightylib.debug import memory
memory.NotificationSender.sendToast("Hello from NightyLib!", logo_url="https://nightylib.bjarnos.dev/img/NightyLib.png")
```

## dump_memory
<p style={{ color: 'gray', marginBottom: '1%' }}>2.0.0</p>
```py
def nightylib.debug.dump_memory() -> str
```
Dumps the entire memory as a formatted string, a much more clean alternative to `globals()`.

:::info

This function does not actually use `globals()`. It only captures classes and unbound functions, not any other types.

:::

:::info

All classes marked with an asterisk (`*`) have an instantiated version that can be accessed via [`memory`](#memory-1)!

:::

:::tip

You can also find a dump file [here](https://github.com/Bjarnos/NightyLib/blob/main/dump.txt), this may be outdated though!

:::

```py title="Example: copy a memory dump to clipboard"
import pyperclip
from nightylib.debug import dump_memory
pyperclip.copy(dump_memory())
```